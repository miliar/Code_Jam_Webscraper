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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int r[50];
char s[50];
int main()
{
//	freopen("C.in","r",stdin);
//	freopen("C:\\data\\A-small-attempt0.in","r",stdin);freopen("C:\\data\\A-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
	freopen("C:\\data\\A-large.in","r",stdin);freopen("C:\\data\\A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int cas=1;cas<=t;cas++)
	{
		printf("Case #%d: ",cas);
		int n;
		scanf("%d\n",&n);
		for(int i=0;i<n;++i)
		{
                r[i]=-1;
                scanf("%s\n",s);
		        for(int j=0;j<n;++j)
		        {
                       if(s[j]=='1' && r[i]<j)r[i]=j;
                }
        }
        int ret=0;
        for(int i=0;i<n;++i)
        {
         if(r[i]>i)
         {
          for(int j=i+1;j<n;++j)if(r[j]<=i)
          {
                  int k=j;
           while(k>i)
           {
           swap(r[k],r[k-1]);
           k--;          
           ret++;
           }
           break;
          }          
         }        
        }
        printf("%d\n",ret);
	}
	return 0;
}
