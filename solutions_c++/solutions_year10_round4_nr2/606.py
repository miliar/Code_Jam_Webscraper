#include<iostream>
#include<cstring>

using namespace std;

int p;
int price[1025];
int cnt[1024];

int stack[30][11];

void dfs(int i,int sp){
	int b=1<<p;
	if(i>=b){
		for(int j=0;j<cnt[i-b];j++)
			stack[sp][j]=-1;
		for(int j=cnt[i-b];j<=p;j++)
			stack[sp][j]=0;
	}
	else{
		dfs(i*2,sp);
		dfs(i*2+1,sp+1);
		for(int j=0;j<=p;j++)
			if(stack[sp+1][j]==-1)
				stack[sp][j]=-1;
			else if(stack[sp][j]!=-1)
				stack[sp][j]+=stack[sp+1][j];
		for(int j=1;j<=p;j++)
			if(stack[sp][j]!=-1){
				int v=stack[sp][j]+price[i];
				if(stack[sp][j-1]==-1 || stack[sp][j-1]>v)
					stack[sp][j-1]=v;
			}
	}
}

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>p;
		for(int j=0;j<(1<<p);j++){
			cin>>cnt[j];
			cnt[j]=p-cnt[j];
		}
		for(int j=1<<(p-1);j;j>>=1)
			for(int k=j;k<2*j;k++)
				cin>>price[k];
		dfs(1,0);
		cout<<"Case #"<<i<<": "<<stack[0][0]<<endl;
	}

}
