#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#define INP_FILE "A-large.in"
#define OUT_FILE "output_A-large.in.txt"

#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define pb push_back
#define L(s) (int)s.size()
#define mp make_pair
#define pii pair<int,int>
#define x first 
#define y second
#define inf 1000000000
#define VI vector<int>
#define ll long long
#define all(s) (s).begin(),(s).end()
#define C(u) memset((u),0,sizeof((u)))
#define ull unsigned ll
#define uint unsigned int


int n,m;
char data[100][100];
int tiles;

bool check()
{
	int s;
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=m;j++)
			if (data[i][j]=='#')
			{
				s=0;
				if (data[i][j]=='#') s++;
				if (data[i+1][j]=='#') s++;
				if (data[i][j+1]=='#') s++;
				if (data[i+1][j+1]=='#') s++;
				if (s<4)
					return false;
				data[i][j]=data[i+1][j+1]='/';
				data[i+1][j]=data[i][j+1]='\\';
			}
	}
	return true;
}


int main()
{
	freopen( INP_FILE , "r" , stdin );
	freopen( OUT_FILE , "w" , stdout );
	int tstCnt;
	cin>>tstCnt;

	for(int tst=1;tst<=tstCnt;tst++)
	{
		cin>>n>>m;
		tiles=0;
		C(data);
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=m;j++)
			{
				cin>>data[i][j];
				if (data[i][j]=='#'){
					tiles++;
				}
			}
		}
		if ( (!check()) )
		{
			printf("Case #%d: \nImpossible\n",tst);
			continue;
		}

		printf("Case #%d:\n",tst);
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=m;j++)
			{
				cout<<data[i][j];
			}
			cout<<endl;
		}

		//printf("Case #%d: ",tst);
	}
}