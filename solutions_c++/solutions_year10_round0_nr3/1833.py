#include <fstream>
using namespace std;

ifstream fin("c:\\pro\\C-large.in");
ofstream fou("c:\\pro\\output3_l.txt");

int N, K, R;
int g[2002];
int next[1002];
int w[1002];


unsigned long long work()
{
	for (int i=0; i<N; i++){
		int tmp=0;
		int tmpip=i;
		for (int j=i; j<i+N; j++){
			if (tmp+g[j]>K){
				tmpip=j % N;
				break;
			}
			tmp+=g[j];
		}
		next[i]=tmpip;
		w[i]=tmp;
	}

	bool vis[1002];
	memset( vis, 0 , sizeof(vis));
		
	unsigned long long ans =0;
	int current = 0;
	while(!vis[current] && R>0  ){
		ans+=w[current];
		vis[current]=true;
		current = next[current];
		R--;
	}
	
	memset( vis, 0 , sizeof(vis));
	long long repw=0;
	int len = 0;
	while (!vis[current]){
		vis[current]=true;
		current=next[current];
		len++;
		repw+=w[current];
	}

	ans += repw * (R/len);
	R=R % len;

	memset( vis, 0 , sizeof(vis));
	while(!vis[current] && R>0  ){
		ans+=w[current];
		vis[current]=true;
		current = next[current];
		R--;
	}
		
	return ans;
}


int main()
{
	int T;
	fin >> T;
	for (int i=1; i<=T; i++){
		fou << "Case #" << i << ": ";
		fin >> R >> K >> N;
		for (int j=0; j<N; j++){
			fin >> g[j];
			g[N+j]=g[j];
		}
		
		fou << work() << endl;
	}
	
	return 0;
}