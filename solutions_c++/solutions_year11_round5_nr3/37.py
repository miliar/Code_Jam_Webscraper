#include <iostream>
using namespace std;
char tbl[100][100];
int R,C;
int n;
int next[10000][2];
int in_deg[10000];
int out_deg[10000];
int temp[10000];
int V(int i,int j){
	while (i<0)
		i+=R;
	while (i>=R)
		i-=R;
	while (j<0)
		j+=C;
	while (j>=C)
		j-=C;
	return i*C+j;
}
int parent[20000];
int par(int v){
	return parent[v]==v?v:parent[v]=par(parent[v]);
}
void join(int v,int w){
	parent[par(v)]=par(w);
}
int main(){
	int tnum,tcou=0;cin>>tnum;
	while (tnum--){
		try{
			cin>>R>>C;
			n=R*C;
			memset(in_deg,0,sizeof in_deg);
			for (int i=0;i<R;++i)
				for (int j=0;j<C;++j){
					out_deg[V(i,j)]=2;
					cin>>tbl[i][j];
					if (tbl[i][j]=='-'){
						next[V(i,j)][0]=V(i,j-1);
						next[V(i,j)][1]=V(i,j+1);
					}
					else if (tbl[i][j]=='|'){
						next[V(i,j)][0]=V(i-1,j);
						next[V(i,j)][1]=V(i+1,j);
					}
					else if (tbl[i][j]=='/'){
						next[V(i,j)][0]=V(i-1,j+1);
						next[V(i,j)][1]=V(i+1,j-1);
					}
					else if (tbl[i][j]=='\\'){
						next[V(i,j)][0]=V(i-1,j-1);
						next[V(i,j)][1]=V(i+1,j+1);
					}
				}
			while (true){
				bool good=false;
				memset(temp,0,sizeof temp);
				for (int i=0;i<n;++i)
					for (int j=0;j<out_deg[i];++j)
						++temp[next[i][j]];
				for (int i=0;i<n;++i)
					if (temp[i]==0 && in_deg[i]==0)
						throw -1;
				for (int i=0;i<n;++i)
					for (int j=0;j<out_deg[i];++j){
						if (temp[next[i][j]]==1 && in_deg[next[i][j]]==0){
							++in_deg[next[i][j]];
							out_deg[i]=0;
							good=true;
						}
					}
				if (!good)
					break;
			}
			memset(temp,0,sizeof temp);
			for (int i=0;i<n;++i)
				for (int j=0;j<out_deg[i];++j)
					++temp[next[i][j]];
			for (int i=0;i<n;++i)
				if (temp[i]!=0 && temp[i]!=2){
					cout<<"What?"<<i<<temp[i]<<endl;
				}
			for (int i=0;i<n;++i)
				parent[i]=i;
			memset(temp,-1,sizeof temp);
			for (int i=0;i<n;++i)
				for (int j=0;j<out_deg[i];++j){
					if (temp[next[i][j]]==-1)
						temp[next[i][j]]=i;
					else
						join(temp[next[i][j]],i);
				}
			int ans=1;
			for (int i=0;i<n;++i)
				if (out_deg[i]==2 && par(i)==i)
					ans=(ans*2)%1000003;
			cout<<"Case #"<<++tcou<<": "<<ans<<endl;
		}
		catch(int){
			cout<<"Case #"<<++tcou<<": 0"<<endl;
		}
	}
	return 0;
}
