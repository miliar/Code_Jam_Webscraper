#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<bitset>
#include<iostream>
#include<sstream>
#include<queue>
#include<cassert>
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
using namespace std;

typedef vector<int> VI;
typedef VI::iterator VIit;
typedef pair<int,int> PII;
typedef map<int,int> MII;
typedef MII::iterator MIIit;
typedef set<int> SI;
typedef SI::iterator SIit;
typedef long long LL;
const int DX[8]={1,-1,0,0,1,1,-1,-1};
const int DY[8]={0,0,1,-1,1,-1,1,-1};
const int intmax=0x7fffffff;
const int mod=1000000007;
char f1[1000],f2[1000];
char s1[]="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvy qee";
char s2[]="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upa zoo";
char s[1005];
int main()
{
    freopen("f1.in","r",stdin);
    freopen("f2.out","w",stdout);
    for(int i=0;s1[i];i++)
    {
        f1[s1[i]]=s2[i];
        f2[s2[i]]=s1[i];
    }
    f1['z']='q';
//    for(int i='a';i<='z';i++)
//        printf("%c->%c\n",i,f1[i]);
//    puts("-");
//    for(int i='a';i<='z';i++)
//        printf("%c->%c\n",i,f2[i]);
    int t;
    scanf("%d",&t);gets(s);
    for(int mt=1;mt<=t;mt++)
    {
        gets(s);
        printf("Case #%d: ",mt);
        for(int i=0;s[i];i++) printf("%c",f1[s[i]]);
        puts("");
    }
}
