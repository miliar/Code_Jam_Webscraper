#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<queue>
#include<cstdio>
#include<set>
#include<map>
#include<cstdlib>
#include<cstring>
#include<stack>
#include <fstream>

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define ABS(a) (a>0?a:-a)

#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define ULL unsigned long long
#define LL long long
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))

using namespace std;

int arr[26] = {24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};

int main()
{
    freopen("small-a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    scanf("%d",&t);
    getchar();
    FOR(test,1,t)
    {
        string a;
        getline(cin,a);
        cout<<"Case #"<<test<<": ";
        char ch;
        REP(i,SZ(a)) cout<<(ch = (a[i]!=' ')?(char)(arr[a[i]-'a']+'a'):' ');
        cout<<endl;
    }

return 0;
}
