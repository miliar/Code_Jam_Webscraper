#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set> 
#include <map>
#include <iomanip>
using namespace std;

#define FOR0(i,n) for(int i=0;i<n;i++)
#define ALL(c) c.begin(),c.end()
#define TR(it,c) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define FORE(x,c) TR(__I,c)if(bool __B=1)for(typeof(*__I) x=*__I;__B;__B=0)
#define FOR1(i,n) for(int i=1;i<=n;i++)
#define IT(c) typeof(c.begin())
#define REP(n) for(int __z=0;__z<n;__z++)

typedef long long int lli;
typedef pair<int,int> ii;
typedef long double ld;

char M[55][55];
int main()
{
    int T;
    cin >> T;
    
    FOR1(q,T)
    {
	int r,c;
	cin >> r >> c;
	FOR0(i,r) FOR0(j,c) cin >> M[i][j];
	bool imp = false;
	// first row
	for(int j=0;j<c;j++)
	{
	    if(M[0][j]=='#')
	    {
		if(j==c-1 or M[0][j+1]!='#')
		{
		    imp = true;
		    break;
		}
		M[0][j] = '/'; 
		M[0][j+1] = '\\';
		j++;
	    }
	}
	// cout << imp << endl;
	// FOR0(j,c) cout << M[0][j];
	// cout << endl;

	for(int i=1;i<r;i++)
	{
	    for(int j=0;j<c;j++)
	    {
		if(M[i-1][j] == '/')
		{
		    if(M[i][j] == '.' or M[i][j+1] == '.')
			imp = true;
		    M[i][j] = '\\'; M[i][j+1] = '/';
		    j++;
		}
		else if(M[i-1][j] == '\\')
		{
		    j++;		   
		}
	    }
	    for(int j=0;j<c;j++)
	    {
		if(M[i][j]=='#')
		{
		    if(i==r-1 or j==c-1 or M[i][j+1]!='#')
		    {
			imp = true;
			break;
		    }
		    M[i][j] = '/'; 
		    M[i][j+1] = '\\';
		    j++;
		}
	    }

	    // cout << imp << endl;
	    // FOR0(j,c) cout << M[i][j];
	    // cout << endl;

	}

	if(imp)
	{
	    cout << "Case #"<<q<<":\n";
	    cout << "Impossible\n";
	}
	else
	{
	    cout << "Case #"<<q<<":\n";
	    FOR0(i,r)
	    {
		FOR0(j,c) cout << M[i][j];
		cout << endl;
	    }
	}
    }
    return 0;
}
