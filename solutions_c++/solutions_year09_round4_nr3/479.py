#include <iostream>
#include <vector>
using namespace std;
#define INF 1000000000
vector <int> A[110];
bool U[110],OK[1<<20];
int C[1<<20];
int B[20],N;
void go(int x,int k,int y)
{
	if (!OK[y]) return;
	if (k==N)
	{
		C[x]=min(C[x],C[x-y]+1);
	} else
	{
		if (x>>k&1)
		{
			go(x,k+1,y);
			go(x,k+1,y+(1<<k));
		} else go(x,k+1,y);
	}
}
int main()
{
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int tt,ttt,K,i,j,k,cnt,x,y,nB;
	cin>>tt;
	for(ttt=1;ttt<=tt;ttt++)
	{
		cout<<"Case #"<<ttt<<": ";
		cin>>N>>K;
		for(i=0;i<N;i++) 
		{
			A[i]=vector<int>(K,0);
			for(j=0;j<K;j++) cin>>A[i][j];
		}
		for(i=0;i<N;i++)
		for(j=i+1;j<N;j++)
		if (A[i]>A[j]) swap(A[i],A[j]);
//		cout<<"sorted"<<endl;
//		for(i=0;i<N;i++) {for(j=0;j<K;j++) cout<<A[i][j]<<" "; cout<<endl;} cout<<endl;
		memset(U,false,sizeof(U));
		for(x=0;x<(1<<N);x++)
		{
			nB=0;
			for(i=0;i<N;i++) if (x>>i&1) B[nB++]=i;
			for(j=0;j<K;j++)
			{
				for(i=0;i+1<nB;i++) if (A[B[i]][j]>=A[B[i+1]][j]) break;
				if (i+1<nB) break;
			}
			if (j==K) OK[x]=true; else OK[x]=false;
//			if (OK[x]==true) cout<<x<<endl;
		}
		for(x=0;x<(1<<N);x++) C[x]=INF; C[0]=0;
		for(x=0;x<(1<<N);x++)
		{
			go(x,0,0);
//			for(y=0;y<=x;y++)
//			if ((x&y)==y&&OK[y])
//				C[x]=min(C[x],C[x-y]+1);
//			cout<<x<<" "<<C[x]<<endl;
		}
		cout<<C[(1<<N)-1]<<endl;
	}
//	system("pause");
	return 0;
}
