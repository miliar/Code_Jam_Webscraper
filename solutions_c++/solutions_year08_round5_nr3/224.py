#include <iostream>
#include <vector>

using namespace std;
#define pb push_back
#define LL long long

int P[11][11][1<<12];
char C[11][11];
int M,N;
int rec(int x,int y,int mask)
{
	if(x==M) return 0;
	if(y==N) return rec(x+1,0,mask);
	if(P[x][y][mask]!=-1) return P[x][y][mask];
	if(C[x][y]=='x') return rec(x,y+1,(mask<<1)&((1<<(N+1))-1));
	P[x][y][mask] = rec(x,y+1,(mask<<1)&((1<<(N+1))-1));
	if( (y == 0 || !(mask&1)) && (y==0 || !((mask>>N)&1)) && (y==N-1 || !((mask>>(N-2))&1)))
	P[x][y][mask]=max(P[x][y][mask], 1+rec(x,y+1,((mask<<1)+1)&((1<<(N+1))-1)));
	return P[x][y][mask];
}


int main()
{
	int TT;
	scanf("%d",&TT);
	int c=0;
	while(TT--)
	{
		for(int i=0;i<11;i++) for(int j=0;j<11;j++) for(int k=0;k<(1<<12);k++)
			P[i][j][k]=-1;
		cin>>M>>N;
		for(int i=0;i<M;i++)
			for(int j=0;j<N;j++) 
				cin>>C[i][j];
		cout<<"Case #"<<++c<<": "<<rec(0,0,0)<<"\n";
	}
	return 0;
}
