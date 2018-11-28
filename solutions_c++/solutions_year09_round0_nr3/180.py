#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

char p[100]="welcome to code jam";
char s[1000];
int d[1000][20];

int main()
{
    int i,j,l,t,len,n;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&t);
    gets(s);
    len=strlen(p);
    for (l=0;l<t;l++)
    {
        gets(s);
        n=strlen(s);
        memset(d,0,sizeof(d));
        d[0][0]=1;
        for (i=0;i<n;i++)
        {
            d[i+1][0]=1;
            for (j=0;j<len;j++)
            {
                d[i+1][j+1]=d[i][j+1];
                if (s[i]==p[j])
                {
                    d[i+1][j+1]+=d[i][j];
                    if (d[i+1][j+1]>=10000) d[i+1][j+1]-=10000;
                }
            }
        }
        printf("Case #%d: %04d\n",l+1,d[n][len]);
    }
	return 0;
}

