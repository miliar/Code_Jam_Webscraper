#include<cstdio>
#include<cstring>
#include<cctype>
using namespace std;
int a[]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
int T;
char s[1005];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    gets(s);
    for(int cas=1;cas<=T;cas++)
    {
        int i;
        printf("Case #%d: ",cas);
        gets(s);
        for(i=0;s[i];i++)
            if(isalpha(s[i])) printf("%c",a[s[i]-'a']+'a');
            else printf("%c",s[i]);
        printf("\n");
    }
    return 0;
}
