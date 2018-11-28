#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;

const int MAXM=10010;
const int LIM=1000000;

int N;
int M,V;
bool g[MAXM],c[MAXM];
int f[MAXM][2];

int init(){
	cin>>M>>V;
	for(int i=0;i<(M-1)/2;++i){
		cin>>g[i]>>c[i];
	}
	for(int i=(M-1)/2;i<M;++i){
		cin>>g[i];
		c[i]=0;
	}
	memset(f,0,sizeof(f));
	return 0;
}

int solve(){
	for(int i=M-1;i>=0;--i){
		f[i][0]=LIM;
		f[i][1]=LIM;
		if(i*2+1>=M){
			f[i][g[i]]=0;
			f[i][1-g[i]]=LIM;
		}else{
			if(g[i] && c[i]){		//AND gate and Changable
				if(f[2*i+1][1]+f[2*i+2][1]<f[i][1]) f[i][1]=f[2*i+1][1]+f[2*i+2][1];
				if(f[2*i+1][1]+f[2*i+2][0]+1<f[i][1]) f[i][1]=f[2*i+1][1]+f[2*i+2][0]+1;
				if(f[2*i+1][0]+f[2*i+2][1]+1<f[i][1]) f[i][1]=f[2*i+1][0]+f[2*i+2][1]+1;

				if(f[2*i+1][1]+f[2*i+2][0]<f[i][0]) f[i][0]=f[2*i+1][1]+f[2*i+2][0];
				if(f[2*i+1][0]+f[2*i+2][1]<f[i][0]) f[i][0]=f[2*i+1][0]+f[2*i+2][1];
				if(f[2*i+1][0]+f[2*i+2][0]<f[i][0]) f[i][0]=f[2*i+1][0]+f[2*i+2][0];
			}else if(g[i] && (!c[i])){	//AND gate and Unchangable
				if(f[2*i+1][1]+f[2*i+2][1]<f[i][1]) f[i][1]=f[2*i+1][1]+f[2*i+2][1];

				if(f[2*i+1][1]+f[2*i+2][0]<f[i][0]) f[i][0]=f[2*i+1][1]+f[2*i+2][0];
				if(f[2*i+1][0]+f[2*i+2][1]<f[i][0]) f[i][0]=f[2*i+1][0]+f[2*i+2][1];
				if(f[2*i+1][0]+f[2*i+2][0]<f[i][0]) f[i][0]=f[2*i+1][0]+f[2*i+2][0];
			}else if((!g[i]) && c[i]){	//OR gate and Changable
				if(f[2*i+1][1]+f[2*i+2][0]<f[i][1]) f[i][1]=f[2*i+1][1]+f[2*i+2][0];
				if(f[2*i+1][0]+f[2*i+2][1]<f[i][1]) f[i][1]=f[2*i+1][0]+f[2*i+2][1];
				if(f[2*i+1][1]+f[2*i+2][1]<f[i][1]) f[i][1]=f[2*i+1][1]+f[2*i+2][1];

				if(f[2*i+1][0]+f[2*i+2][0]<f[i][0]) f[i][0]=f[2*i+1][0]+f[2*i+2][0];
				if(f[2*i+1][0]+f[2*i+2][1]+1<f[i][0]) f[i][0]=f[2*i+1][0]+f[2*i+2][1]+1;
				if(f[2*i+1][1]+f[2*i+2][0]+1<f[i][0]) f[i][0]=f[2*i+1][1]+f[2*i+2][0]+1;
			}else if((!g[i]) && (!c[i])){	//OR gate and Unchangable
				if(f[2*i+1][1]+f[2*i+2][0]<f[i][1]) f[i][1]=f[2*i+1][1]+f[2*i+2][0];
				if(f[2*i+1][0]+f[2*i+2][1]<f[i][1]) f[i][1]=f[2*i+1][0]+f[2*i+2][1];
				if(f[2*i+1][1]+f[2*i+2][1]<f[i][1]) f[i][1]=f[2*i+1][1]+f[2*i+2][1];

				if(f[2*i+1][0]+f[2*i+2][0]<f[i][0]) f[i][0]=f[2*i+1][0]+f[2*i+2][0];
			}
		}
	}
	return 0;
}

int show(int n){
	cout<<"Case #"<<n<<": ";
	if(f[0][V]>=LIM) cout<<"IMPOSSIBLE";
	else cout<<f[0][V];
	cout<<endl;
	return 0;
}

int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>N;
	for(int time=0;time<N;++time){
		init();
		solve();
		show(time+1);
	}
	return 0;
}
