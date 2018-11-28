#line 5 "code.cpp"
#include <string>
#include <vector>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define sqr(x) (x)*(x)
#define For(i,n,m) for(int i=n;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef vector<vector<pair<int,int> > > adjL;
int table[600][600];
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	cin>>cases;
	for(int a=1;a<=cases;a++)
	{
		int r,c,d;
		cin>>r>>c>>d;
		rep(i,r)
			rep(j,c)
			{
				char digit;
				cin>>digit;
				table[i][j]=digit-'0';
			}
		int size=min(r,c);
		while(size>=3)
		{
			bool valid=false;
			rep(i,r-size+1)
				rep(j,c-size+1)
				{
					int xtotal=0,ytotal=0;
					rep(k,size)
						rep(l,size)
						{
							if(k!=0&&k!=size-1||l!=0&&l!=size-1)
							{
								xtotal+=table[i+k][j+l]*(l+l-(size-1));
								ytotal+=table[i+k][j+l]*(k+k-(size-1));
							}
						}
//					cout<<i<<' '<<j<<' '<<size<<' '<<xtotal<<' '<<ytotal<<endl;
					if(xtotal==0&&ytotal==0)
					{
						valid=true;
						break;
					}
				}
			if(valid)
				break;
			size--;
		}
		printf("Case #%d: ",a);
		if(size<3)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",size);
	}
	return 0;
}
// Powered by FileEdit
// Powered by TZTester 1.01 [25-Feb-2003]
// Powered by CodeProcessor
