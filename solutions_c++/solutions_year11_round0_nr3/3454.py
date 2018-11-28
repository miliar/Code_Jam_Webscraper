#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstring>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FOR( i,a,b ) for(int i=a;i<b;i++)
#define NS string::npos
#define VI vector <int>
#define sz size
#define PI <int ,int >
#define CLEAR(cab) memset(cab,0,sizeof cab)
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output_xor_large.txt","w",stdout);
   vector < int > v;
    int n,i,test,sum=0,num=0,m=10000000;
    v.resize(1100);
    scanf("%d",&test);
    int cs=0;

    while(test--)
    {
        cs++;
        scanf("%d",&n);
        sum=0;
        num=0;
        m=10000000;
    for(i=0;i<n;i++)
    {
        cin>>v[i];
        sum=sum+v[i];
        num=num^v[i];
        m=min(v[i],m);
    }
    if(num!=0)
    printf("Case #%d: NO\n",cs);
    else
    {
        printf("Case #%d: %d\n",cs,sum-m);
    }
    //cout<<endl;
    }

return 0;
}

