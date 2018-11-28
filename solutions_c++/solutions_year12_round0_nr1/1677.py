#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
char str[200];
char ch[1000];
int main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    string s[4],t[4];
    s[1] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    t[1] = "our language is impossible to understand";

    s[2] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    t[2] = "there are twenty six factorial possibilities";

    s[0] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    t[0] = "so it is okay if you want to just give up";

    s[3] = "qz ";
    t[3] = "zq ";
    for(int i=0;i<4;i++)
        for(int j=0;j<s[i].size();j++)
            str[s[i][j]]=t[i][j];
    //for(int i='a';i<='z';i++)printf("%c",i);printf("\n");
    //for(int i='a';i<='z';i++)printf("%c",str[i]);

    int kase;
    scanf("%d",&kase);
    gets(ch);
    for(int kases=1;kases<=kase;kases++){
        gets(ch);
        printf("Case #%d: ",kases);
        for(int i=0;ch[i];i++)printf("%c",str[ch[i]]);
        printf("\n");
    }
	return 0;
}
