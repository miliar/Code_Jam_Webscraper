//Author  :   MAK(Kader)
//Problem no:  
//Title:  Cse DU

//#pragma warning(disable:4786)
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cctype>
#include<iostream>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
//-------------------------------------------------------
typedef pair<int,int> ii;
typedef vector<int> vi;
#define pb push_back
#define sz(c) (c).size()
#define all(c) (c).begin(),(c).end()
#define vtr(c,i) for(vi::iterator i=c.begin();i!=c.end();i++)
#define INF  (1<<30)
#define EPS  1e-8
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

int chess[520][520];
int mp[200],M,N;
void reset(){

	int i;
	for( i=0;i<10;i++)
		mp[i+'0']=i;
	int v=10;
	for(i='A';i<='F';i++){
		mp[i]=v;
		v++;
	}

}

void makeChess(int put,int i,int j){

	int k;
	for(k=0;k<4;k++){
	
		if(put&(1<<k))
			chess[i][j*4+(4-k-1)]=1;
		else 
			chess[i][j*4+(4-k-1)]=0;
	}
}
void show(){
	int i,j;
	for(i=0;i<M;i++){
		for(j=0;j<N;j++)
			cout<<chess[i][j]<<" ";
		cout<<endl;
	}
}
bool isChess(int i,int j,int l){


	if(l==1&& chess[i][j]!=-1) return true;
	if(l==1) return false;
	int L=l-1,k;

	for(k=0;k<=L;k++){		
		if(chess[i+L][j+k]+chess[i+L-1][j+k]!=1)
			return false;
		if(chess[i+k][j+L]+chess[i+k][j+L-1]!=1)
			return false;
	}

	if(isChess(i,j,l-1))
		return true;
	return false;

}
bool is(int i,int j,int l){

	if(i+l-1>=M)return false;
	if(j+l-1>=N) return false;
	return isChess(i,j,l);
}
void sett(int a,int b,int k){

	int i,j;
	for(i=a;i<a+k;i++)
		for(j=b;j<b+k;j++)
			chess[i][j]=-1;

}
int out[513];
void process(){

	int i,k,j;
	CLR(out);

	for(k=min(M,N);k>=1;k--)
		for(i=0;i<M;i++)
			for(j=0;j<N;j++)
			if(is(i,j,k)){
			
				sett(i,j,k);
				out[k]++;
				
			}
		

			int res=0;
			for(i=33;i>=1;i--)
				if(out[i])
					res++;
			cout<<res<<endl;

	for(i=33;i>=1;i--)
		if(out[i])
			cout<<i<<" "<<out[i]<<endl;
}
int main()
{
	freopen("code_jam/C-small-attempt0.in","rt",stdin);
	freopen("code_jam/out.txt","wt",stdout);
	//only small

	reset();
	char str[100];
	int T,i,j,cas=1;
	cin>>T;
	while(T--){
		cin>>M>>N;
		for(i=0;i<M;i++)
		{
			for(j=0;j<N/4;j++){
				scanf("%1s",str);
				makeChess(mp[str[0]],i,j);
			}
		}
		//show();
		printf("Case #%d: ",cas++);
		process();
	
	}
	return 0;
}
