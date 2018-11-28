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
    int C;
    int t[200];
    ms(t,-1);
    string a1="ejp mysljylc kd kxveddknmc re jsicpdrysi",b1="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",c1="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string s,a="our language is impossible to understand",b="there are twenty six factorial possibilities",c="so it is okay if you want to just give up";

    t['a']='y',t['o']='e',t['z']='q';

    int n=a.size();
    for(int i=0;i<n;i++)
        t[a1[i]]=a[i];

    n=b.size();
    for(int i=0;i<n;i++)
        t[b1[i]]=b[i];

    n=c.size();
    for(int i=0;i<n;i++)
        t[c1[i]]=c[i];


    for(int i='a';i<='z';i++)
        if(t[i]==-1){
            t[i]='z';
         //   cout<<(char)t[i]<<" ";
        }
       // else    cout<<(char)t[i]<<" ";
  //  cout<<"\n";

    cin>>C;
    ofstream fout("test.txt");
    getline(cin, s);
    for(int q=1;q<=C;q++){

        getline(cin,s);
        n=s.size();
        cout<<"Case #"<<q<<": ";
        for(int i=0;i<n;i++)
            cout<<(char)t[s[i]];
        cout<<"\n";
    }

    return 0;
}
