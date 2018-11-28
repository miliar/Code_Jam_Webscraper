/*Author : Punit Singh */
// Standard includes
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>
//Data Structures
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
using namespace std;
#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define INF		INT_MAX
#define ALL(x) 		x.begin(),x.end()
#define LET(x,a)	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v) 	IFOR(it,v.begin(),v.end())
#define pb 		push_back
#define sz(x) 		int(x.size())
#define mp 		make_pair
#define fill(x,v)	memset(x,v,sizeof(x))
typedef pair<int,int> PI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;
bool check(vector<string> &a,char x)
{
    int i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(a[i][j]!=x&&a[i][j]!='T')
                break;
        }
        if(j==4)
            return true;
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(a[j][i]!=x&&a[j][i]!='T')
                break;
        }
        if(j==4)
            return true;
    }
    for(i=0;i<4;i++)
        if(a[i][i]!=x&&a[i][i]!='T')
            break;
    if(i==4)
        return true;
    for(i=0;i<4;i++)
        if(a[i][3-i]!=x&&a[i][3-i]!='T')
            break;
    if(i==4)
        return true;
    return false;
}
int main()
{
    #ifdef TEST
 	freopen("A-large.in","r",stdin);
 	freopen("out.txt","w",stdout);
    #endif
    int t,ctr=1;
    bool empt;
    vector<string> a(4);
    scanf("%d",&t);
    while(ctr<=t)
    {
        rep(i,4)
        cin>>a[i];
        empt=false;
        rep(i,4)
        rep(j,4)
        if(a[i][j]=='.')
        {
            empt=true;
            break;
        }
        printf("Case #%d: ",ctr++);
        if(check(a,'X'))
            printf("X won\n");
        else if(check(a,'O'))
            printf("O won\n");
        else if(empt)
            printf("Game has not completed\n");
        else
            printf("Draw\n");
    }
    return 0;
}
