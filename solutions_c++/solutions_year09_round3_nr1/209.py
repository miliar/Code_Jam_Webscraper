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
char s[100];
int taken[50];
int ta[57];
int sy[100];
int f(char ss)
{
    if(isdigit(ss))return ss-'0';
    return ss-'a'+10;
}
int main()
{

//	freopen("A.in","r",stdin);
//	freopen("C:\\data\\A-small.in","r",stdin);freopen("C:\\data\\A-small.out","w",stdout);
	freopen("C:\\data\\A-large.in","r",stdin);freopen("C:\\data\\A-large.out","w",stdout);	
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
   int t;
   scanf("%d",&t);
   for(int cas=1;cas<=t;++cas)
   {
    scanf("%s",&s);        
    memset(taken,0,sizeof(taken));
    int S=strlen(s);
    vector<int> l;
    for(int i=0;i<50;++i)if(taken[i]==0)l.push_back(i);
    swap(l[0],l[1]);                  
    int p=0,h=1;
    memset(ta,255,sizeof(ta));
    for(int i=0;i<S;++i)
    if(ta[f(s[i])]==-1)
    {
         ta[f(s[i])]=l[p++];
         sy[i]=ta[f(s[i])];
     if(h<sy[i])h=sy[i];         
    }
    else
    {
         sy[i]=ta[f(s[i])];
     if(h<sy[i])h=sy[i];         
    }
    h++;
    long long ret=0;
    long long ba=1;
    for(int i=S-1;i>=0;--i)
    {
     ret=ret+ba*sy[i];
     ba*=h;
    }
    printf("Case #%d: %lld\n",cas,ret);
   }
    return 0;
}
