#include<cstdio>
#include<algorithm>
#include<vector>
#define REP(i,n) for(int i=0;i<(n);i++)
#define PB push_back
#define ALL(c) (c).begin(),(c).end()
using namespace std;
const int MAXN = 30;
char s[MAXN];
vector<int> v;

void read(){
	scanf("%s",s);
	v.clear();
	for(int i=0;s[i];i++)
		v.PB(s[i] - '0');
}

void compute(){
	if(!next_permutation(ALL(v))){
		vector<int> p;
		for(int i=0;i<v.size();i++){
			if(v[i] !=0){
				p.PB(v[i]);
				p.PB(0);
				for(int j=0;j<i;j++)
					p.PB(0);
				for(int j=i+1;j<v.size();j++)
					p.PB(v[j]);
				v = p;
				break;
			}
		}
	}
}

void print(int cas){
	printf("Case #%d: ",cas+1);
	for(int i=0;i<v.size();i++)
		printf("%d",v[i]);
	printf("\n");
}

int main(){
	int t;
	scanf("%d",&t);
	REP(i,t){
		read();
		compute();
		print(i);
	}
	return 0;
}

