/*
* A large
* @author Mircea Dima
*/
#include <cstdio>
#include <string>
#include <fstream>

using namespace std;

string dex[10001];
string a;
string x[32];

int L, n, m;
int nr;

void solve(int t)
{
    int i,j,k;
    int nrsol = 0;
    nr = 0;
    for(i = 0; i < 30; ++i)
	x[i].clear();

    for( i = 0; i < a.size(); )
    {
	if(a[i] == ')') ++i;
	if(a[i] == '(')
	{
	    ++nr;
	    for(j = i + 1; a[j] !=')'; ++j)
		x[nr] += a[j];
	    i = j;
	}
	else x[++nr] = a[i++];
    }
   

    for(i = 0 ; i < n; ++i)
    {
	int ok = 1;
	for(j = 0; j < dex[i].size(); ++j)
	{
	    int oki = 0;
	    for(k = 0; k < x[j+1].size(); ++k)
		if(dex[i][j] == x[j+1][k]) 
		{
		    oki = 1; 
		    break;
		}
	    
	    if(oki == 0) { ok = 0; break;}
	}
	if(ok) ++nrsol;
    }	

    printf("Case #%d: %d\n", t,nrsol);
}

int main()
{
    ifstream f("a.in");
    freopen("a.out","w",stdout);
    f>>L>>n>>m;

    int i;
    for(i = 0; i < n; ++i)
	f >> dex[i];
    
    for(i = 1; i <= m; ++i)
    {
	f >> a;
        solve(i);
    }	

    return 0;
}

