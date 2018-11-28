#include<stdio.h>
#include<string.h>
#include<vector>
#include<string>
using namespace std;
char str[103],res[29][29],cnt[29];
vector<int> v2[29];
string str1;
bool chckbase(char ch)
{
    return ch=='Q'||ch=='W'||ch=='E'||ch=='R'||ch=='A'||ch=='S'||ch=='D'||ch=='F';
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int test,cas,a,i,b,n,sz,k,j;
    char ch;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        memset(res,0,sizeof(res));
        memset(cnt,0,sizeof(cnt));
        scanf("%d",&a);
        for (i=0;i<a;i++)
        {
            scanf("%s",str);
            res[str[0]-'A'][str[1]-'A']=res[str[1]-'A'][str[0]-'A']=str[2];
        }
        scanf("%d",&b);
        for (i=0;i<b;i++)
        {
            scanf("%s",str);
            v2[str[0]-'A'].push_back(str[1]-'A');
            v2[str[1]-'A'].push_back(str[0]-'A');
        }
        scanf("%d",&n);
        scanf("%s",str);
        str1="";
        sz=0;
        for (k=0;k<n;k++)
        {
            str1.push_back(str[k]);
            if (str[k]>='A'&&str[k]<='Z') cnt[str[k]-'A']++;
            sz++;
            if (sz>=2&&chckbase(str1[sz-1])&&chckbase(str1[sz-2])&&res[str1[sz-1]-'A'][str1[sz-2]-'A'])
            {
                ch=res[str1[sz-1]-'A'][str1[sz-2]-'A'];
                cnt[str1[sz-1]-'A']--;
                cnt[str1[sz-2]-'A']--;
                str1.erase(str1.begin()+sz-1);
                sz--;
                str1.erase(str1.begin()+sz-1);
                sz--;
                str1.push_back(ch);
                sz++;
                if (ch>='A'&&ch<='Z') cnt[ch-'A']++;
            }
            for (i=0;i<26;i++)
            {
                if (cnt[i])
                {
                    for (j=0;j<v2[i].size();j++)
                    {
                        if (cnt[v2[i][j]]) break;
                    }
                    if (j<v2[i].size()) break;
                }
            }
            if (i<26)
            {
                str1.clear();
                sz=0;
                for (i=0;i<26;i++) cnt[i]=0;
            }
        }
        printf("Case #%d: [",cas);
        for (i=0;i<sz-1;i++) printf("%c, ",str1[i]);
        if (sz) printf("%c",str1[sz-1]);
        printf("]\n");
        for (i=0;i<26;i++) v2[i].clear();
    }
    return 0;
}
