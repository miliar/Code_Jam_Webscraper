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

char a[6000][20];
char d[20][500];
int len[20];

int main()
{
    int i,j,k,l,ans,ll,dd,n;
    char s[1000];
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d%d%d",&ll,&dd,&n);
    for (i=0;i<dd;i++)
    {
        scanf("%s",a[i]);
    }
    for (i=0;i<n;i++)
    {
        scanf("%s",s);
        k=0;
        for (j=0;j<ll;j++)
        {
            l=0;
            if (s[k]=='(')
            {
                k++;
                while (s[k]!=')')
                {
                    d[j][l]=s[k];
                    l++;k++;
                }
                len[j]=l;
                k++;
            }
            else
            {
                d[j][0]=s[k];
                len[j]=1;
                k++;
            }
        }
        ans=0;
        for (j=0;j<dd;j++)
        {
            for (k=0;k<ll;k++)
            {
                for (l=0;l<len[k];l++)
                    if (a[j][k]==d[k][l]) break;
                if (l==len[k]) break;
            }
            if (k==ll) ans++;
        }
        printf("Case #%d: %d\n",i+1,ans);

    }
	return 0;
}

