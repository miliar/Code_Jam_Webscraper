#include <iostream>
#include <vector>

using namespace std;
#define pb push_back
#define LL long long

#define M 10007

int P[101][101];
bool Q[101][101];
int H,W;
int rec(int x,int y)
{
if(x==W && y==H) return 1;
if(x>W || y>H) return 0;
if(Q[x][y]) return 0;
if(P[x][y]!=-1) return P[x][y];
P[x][y] = (rec(x+2,y+1) + rec(x+1,y+2))%M;
return P[x][y];
}	
int main()
{
	int TT;
	scanf("%d",&TT);
	int c=0;
	while(TT--)
	{
		for(int i=0;i<101;i++) for(int j=0;j<101;j++) {
			P[i][j]=-1;
			Q[i][j]=0;
		}
		int R;
		cin>>H>>W>>R;
		H--;W--;
		for(int i=0;i<R;i++)
		{
			int x,y;
			cin>>y>>x;
			y--;x--;
			Q[x][y]=1;
		}
		cout<<"Case #"<<++c<<": "<<rec(0,0)<<"\n";
	}
	return 0;
}
