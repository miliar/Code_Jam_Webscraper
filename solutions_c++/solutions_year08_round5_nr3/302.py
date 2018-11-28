#include<ctime>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define CLR(a,x) memset((a),(x),sizeof((a)))
#define dout if(1) cout
const double TOLL=1e-9;
typedef istringstream iss; typedef ostringstream oss; typedef long long int lli;
int t,M,N;
bool ok[100][100];
bool student[100][100];
bool canplace[100][100];

bool valid(int r,int c)
{
	if(r<0 || c<0 || r>=M || c>=N || !ok[r][c]) return false;
	return true;
}
void placestd(int r,int c)
{
	canplace[r][c]=false;
	student[r][c]=true;
	int dr[]={0,0,-1,-1};
	int dc[]={-1,1,-1,1};
	for(int i=0;i<4;i++)
	{
		int nr=r+dr[i]; int nc=c+dc[i];
		if(!valid(nr,nc)) continue;
		canplace[nr][nc]=false;
	}
}
bool check(int r,int c)
{
	int dr[]={0,0,-1,-1};
	int dc[]={-1,1,-1,1};
	for(int i=0;i<4;i++)
	{
		int nr=r+dr[i]; int nc=c+dc[i];
		if(!valid(nr,nc)) continue;
		if(student[nr][nc]) return false;
	}
	return true;
}

int main()
{
	cin>>t;
	int cn=0;
	while(t--)
	{
		cin>>M>>N;
		CLR(ok,false);
		for(int i=0;i<M;i++) for(int j=0;j<N;j++)
		{
			char x; cin>>x;
			if(x=='.') ok[i][j]=true;
			else ok[i][j]=false;
		}
		int rv=0;
		
		for(int row=0;row<M;row++) for(int col=0;col<N;col++) if(ok[row][col])
		{
			CLR(student,false);
			CLR(canplace,true);
			int trv=1; 
			placestd(row,col);
			
			for(int i=0;i<M;i++) for(int j=0;j<N;j++) if(canplace[i][j] && ok[i][j] && check(i,j))
			{
				trv++; placestd(i,j);

			}
			rv=max(rv,trv);
		}
		cn++;
		cout<<"Case #"<<cn<<": "<<rv<<endl;

	}
	
	return 0;
}
