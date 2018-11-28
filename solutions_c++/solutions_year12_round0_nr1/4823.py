# include <stdio.h>
# include <string.h>
//# include <ioseam>
//using namespace std;
int main()
{
    char s[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'},a[105];
    int c=0,t=0,i=0,j=0,l=0;
    freopen("1.in","r",stdin);
    freopen("2.out","w",stdout);
    scanf("%d ",&t);
    for(i=1;i<=t;i++)
    {
        gets(a);       //printf("%s",a);
       l=strlen(a);
       //printf("%d",l);
       printf("Case #%d: ",i);
        for(j=0;j<l;j++)
            {
                if(a[j]==' ')
                    printf(" ");
                else
                    {
                        c=a[j]-97;
                        printf("%c",s[c]);
                    }
            }
        printf("\n");
    }
    return 0;
}
