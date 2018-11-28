#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <memory.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector <int> vi;

int T;
int c, d, n;

char x[50][50];
bool y[50][50];

char res[150];
int resn;
char s[150];

int main()
{
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    memset(x, -1, sizeof(x));
    memset(y, 0, sizeof(y));
    resn = 0;
    scanf("%d", &c);
    for (int i = 0; i < c; ++i)
    {
    	scanf("%s", s);
    	x[s[0] - 'A'][s[1] - 'A'] = s[2];
    	x[s[1] - 'A'][s[0] - 'A'] = s[2];
    }
    scanf("%d", &d);
    for (int i = 0; i < d; ++i)
    {
    	scanf("%s", s);
    	y[s[0] - 'A'][s[1] - 'A'] = true;
    	y[s[1] - 'A'][s[0] - 'A'] = true;
    }
    scanf("%d %s", &n, s);
    for (int i = 0; i < n; ++i)
    {
    	res[resn++] = s[i];
    	if ( resn > 1 && x[res[resn-1]- 'A'][res[resn - 2] - 'A'] != -1 )
    	{
    		res[resn - 2] = x[res[resn-1]- 'A'][res[resn - 2] - 'A'];
    		--resn;
    	}
    	for (int i = resn-2; i >= 0; --i)
    	{
    		if (y[res[i] - 'A'][res[resn-1] - 'A'])
    			resn = 0;
    	}
    }
  	printf("Case #%d: ", t + 1);
  	printf("[");
  	for (int i = 0; i < resn; ++i)
  	{
  		printf("%c", res[i]) ;
  		if (i < resn - 1)
  			printf(", ");
  	}
  	printf("]\n");
  }
	return 0;
}          