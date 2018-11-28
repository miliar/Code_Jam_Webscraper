#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
using namespace std;
typedef long long ll;
#define M 26
#define INF 1<<30
char st[M];
string str;
char s1[200]="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
char s2[200]="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
void gao()
{
    int len=strlen(s1);
    for(int i=0;i<len;i++)
    {
        if(s1[i]!=' ')
        st[s1[i]-'a']=s2[i];
    }
    st['q'-'a']='z';
    st['z'-'a']='q';
}
int main()
{
    gao();
    int n;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&n);
    getchar();
    for(int cas=1;cas<=n;cas++)
    {
        printf("Case #%d: ",cas);
        getline(cin,str);
        int len=str.length();
        for(int i=0;i<len;i++)
        {
            if('a'<=str[i] && str[i]<='z')
            cout<<st[str[i]-'a'];
            else
            cout<<str[i];
        }
        puts("");
    }
	return 0;
}
