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

int num[4000000];
int zhan[10000000];

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int i,j,l,t,m,top,bottom,n,p,ans;
    set<int> st;
    scanf("%d",&t);
    for (l=0;l<t;l++)
    {
        scanf("%d",&n);
        memset(num,0,sizeof(num));
        top=0;bottom=0;
        ans=0;
        st.clear();
        for (i=0;i<n;i++)
        {
            scanf("%d%d",&p,&m);
            num[p+2000000]=m;
            if (m>=2)
            {
                zhan[bottom]=p+2000000;
                st.insert(p+2000000);
                bottom++;
            }
        }
        while (top<bottom)
        {
            num[zhan[top]-1]+=num[zhan[top]]/2;
            num[zhan[top]+1]+=num[zhan[top]]/2;
            ans+=num[zhan[top]]/2;
            num[zhan[top]]%=2;
            //printf("%d",ans);
            if ((num[zhan[top]-1]>=2)&&(st.find(zhan[top]-1)==st.end()))
            {
                zhan[bottom]=zhan[top]-1;
                st.insert(zhan[top]-1);
                bottom++;
            }
            if ((num[zhan[top]+1]>=2)&&(st.find(zhan[top]+1)==st.end()))
            {
                zhan[bottom]=zhan[top]+1;
                st.insert(zhan[top]+1);
                bottom++;
            }
            st.erase(zhan[top]);
            top++;
            //printf("%d",top);
        }
        printf("Case #%d: %d\n",l+1,ans);
    }
	return 0;
}

