#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = numeric_limits<int>::max();

const int nmax = 55;
char a[nmax][nmax];
int n,k;

bool win(char p)
{
    for(int r=0;r<n;r++)
	for(int c=0;c<n;c++)
	{
	    if(r+k<=n)
	    {
		bool w = true;
		for(int i=0;i<k;i++)
		    if(a[r+i][c] != p)
		    {
			w = false;
			break;
		    }
		if(w)
		    return true;
	    }
	    if(c+k<=n)
	    {
		bool w = true;
		for(int i=0;i<k;i++)
		    if(a[r][c+i] != p)
		    {
			w = false;
			break;
		    }
		if(w)
		    return true;
	    }
	    if(r+k<=n && c-k+1>=0)
	    {
		bool w = true;
		for(int i=0;i<k;i++)
		    if(a[r+i][c-i] != p)
		    {
			w = false;
			break;
		    }
		if(w)
		    return true;
	    }
	    if(r+k<=n && c+k<=n)
	    {
		bool w = true;
		for(int i=0;i<k;i++)
		    if(a[r+i][c+i] != p)
		    {
			w = false;
			break;
		    }
		if(w)
		    return true;
	    } 
	}
    return false;
}

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
	scanf("%d%d",&n,&k);
	for(int r=0;r<n;r++)
	    scanf(" %s", a[r]);

	for(int r=0;r<n;r++)
	{
	    vector<char> v;
	    for(int c=0;c<n;c++)
		if(a[r][c] != '.')
		{
		    v.push_back(a[r][c]);
		    a[r][c] = '.';
		}
	    for(int c=n-1;!v.empty();c--)
	    {
		a[r][c] = v.back();
		v.pop_back();
	    }
	}

	/*for(int r=0;r<n;r++)
	{
	    for(int c=0;c<n;c++)
		printf("%c", a[r][c]);
	    printf("\n");
	}
	*/
	bool bwin = win('B');
	bool rwin = win('R');

	printf("Case #%d: ", test_case);
	if(bwin)
	    if(rwin)
		printf("Both");
	    else
		printf("Blue");
	else
	    if(rwin)
		printf("Red");
	    else
		printf("Neither");
	printf("\n");
    }
    return 0;
}
