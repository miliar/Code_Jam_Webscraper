#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
    int Case,hash[300];
    char c;
    string s[1000];
    memset(hash,0,sizeof(hash));
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    scanf("%d\n",&Case);
    for(int i=1;i<=Case;i++){
        while((c=getchar())&&c!='\n')
            s[i]+=c;
        s[i]+='\0';
    }
    string samin,samout;
    samin="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    samout="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    for(int i=0;i<samin.size();i++)
        hash[samin[i]]=samout[i];
    hash['q']='z';
    hash['z']='q';
    for(int i=1;i<=Case;i++){
        for(int j=0;j<s[i].size();j++)if(s[i][j]!=' '){
            s[i][j]=hash[s[i][j]];
        }
        printf("Case #%d: %s\n",i,s[i].c_str());
    }
}
