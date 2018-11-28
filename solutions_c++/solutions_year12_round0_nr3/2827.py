#include <cctype>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <bitset>
#include <assert.h>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <ctime>

#define DEBUG_FLAG 1
#if DEBUG_FLAG
#define DBG(z) cout << #z << " : " << (z) << "\n";
#define DBY(x,y) cout << #x << " : " << (x) <<" , "<< #y << " : "<< (y) << "\n";
#define DBZ(x,y,z) cout << #x << " : " << (x) <<" , "<< #y << " : "<< (y) << " , " << #z << " : " << (z) << "\n";
#else
#define DBG(z)
#define DBY(x,y)
#define DBZ(x,y,z)
#endif

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ms(x,y) memset((x),(y),sizeof((x)))
#define all(c) c.begin(),c.end()
#define emp(a,i) (!((a) & (1<<(i))))
#define sh(a) (1<<(a))

#define PI 3.1415926535

using namespace std;
using namespace __gnu_cxx;

int main()
{
    //ofstream cout("test.txt");
    int t,a,b,d[10];
    cin>>t;
    d[0]=1;
    for(int i=1;i<9;i++)
        d[i]=d[i-1]*10;

    for(int q=1;q<=t;q++){
        cin>>a>>b;
        long long ans=0;
        int br=0,x=a;
        while(x)    x/=10,br++;
        for(int i=a;i<=b;i++){
            set<int> S;
            S.clear();
            for(int j=1;j<br;j++){
                x=(i%d[j])*d[br-j]+i/d[j];
                if(x<=b && x>i){
                    if(S.find(x)==S.end())    ans++,S.insert(x);
                   /* else   {
                        cout<<"ERROR\n";
                        DBY(x,i);
                    }
                    if(s[i].find(x)==s[i].end())    s[i].insert(x);
                    else{
                        cout<<"ERROR1\n";
                        DBY(x,i);
                    }*/
                 }
            }
        }
        cout<<"Case #"<<q<<": "<<ans<<"\n";
    }

    return 0;
}
