#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#define min(a,b){(a)<(b)?(a):(b)}
#define max(a,b){(a)>(b)?(a):(b)}

using namespace std;

int main()
{
    //freopen("Round_1A_B_small.in","r",stdin);
    //freopen("Round_1A_B_small.out","w",stdout);
    freopen("Round_1A_B_large.in","r",stdin);
    freopen("Round_1A_B_large.out","w",stdout);
    int times,count=0;
    cin>>times;getchar();
    while(times--)
    {
        int num,sur,m,tmp,ans=0;
        vector<int> val;
        cin>>num>>sur>>m;
        for(int i=0;i<num;i++){cin>>tmp;val.push_back(tmp);}
        for(int i=0;i<num;i++)
        {
            tmp=max((m-1)*3,0);
            if(val[i]>tmp) ans++;
            else if(val[i]>1 && val[i]>tmp-2 && sur){ans++,sur--;}
        }
        if(m==0) ans=num;
        cout<<"Case #"<<++count<<": "<<ans<<endl;
    }
    return 0;
}
