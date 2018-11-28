#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <sstream>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair<int, int> pii;

int T;

char c[110][110];
char s[110];
int n;

double wp[110];
double owp[110];
double oowp[110];

int main()
{
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    scanf("%d", &n);
    gets(s);
    for (int i = 0; i < n; ++i)
    	gets(c[i]);
    for (int i = 0; i < n; ++i)
    {
    	wp[i] = 0.0;
    	int x = 0;
    	int y = 0;
    	for (int j = 0; j < n; ++j)
    	{
    		if ( c[i][j] == '0' )
    			++y;
    		else if ( c[i][j] == '1' )
    		{
    			++y;
    			++x;
    		}
    	}
    	wp[i] = (double)x / y;

    	double wwp = 0.0;
    	for (int j = 0; j < n; ++j)
    	{
    		if (j != i && c[i][j] != '.')
    		{
    			int xx = 0;
    			int yy = 0;
    			for (int k = 0; k < n; ++k)
    			{
    				if ( k != i )
    				{
    					if (c[j][k] == '0')
    						++yy;
    					else if (c[j][k] == '1')
    					{
    						++yy;
    						++xx;
    					}
    				}
    			}
    			wwp += (double)xx / yy;
    		}
    		
    	}
    	owp[i] = wwp / y;
    }
    for (int i = 0; i < n; ++i)
    {
    	oowp[i] = 0.0;
    	int x = 0;
    	for (int j = 0; j < n; ++j)
    		if ( c[i][j] != '.')
    		{
    			++x;
    			oowp[i] += owp[j];
    		}
    	oowp[i] /= x;
    }
    
  	printf("Case #%d:\n", t+1);
  	for (int i = 0; i < n; ++i)
  		printf("%.9f\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
  }
  return 0;
}