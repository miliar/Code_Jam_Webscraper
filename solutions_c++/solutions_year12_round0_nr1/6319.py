#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#define maxn 100000
#define pi pair<int,int>
#define vi vector<int>
#define pb push_back
#define sz(x) sizeof((x))
#define setit(x,val) memset((x),(val),(sz(x)))
#define all(x) (x).begin(),(x).end()
#define rep(i,n,st) for(int (i)=(st);(i)<(n);(i)++)
#define ll long long int
#define SI ({int x;scanf("%d\n",&x);x;})
using namespace std;

int main()
{
    freopen("ditct.txt","w",stdout);
    freopen("in.txt","r",stdin);
    char lib[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t1=SI;
    int loc=0;
    char in[1000],tmp;
    int kase=1;
    while(t1--)
    {
        printf("Case #%d: ",kase++);
        while(scanf("%c",&tmp) && tmp!='\n')in[loc++]=tmp;
        in[loc]='\n';
        for(int i=0;i<loc;i++)
        {
        if(in[i]!=' ')
        printf("%c",lib[in[i]-'a']);
        else printf(" ");
        }
        printf("\n");
        loc=0;
    }
	return 0;
}
