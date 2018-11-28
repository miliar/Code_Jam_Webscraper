#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int map[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int t;
char s[110];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a-small-1.out","w",stdout);
    
    int i,j;
    scanf("%d",&t);
    gets(s);
    int tt=1;
    while(t--)
    {
        gets(s);
        printf("Case #%d: ",tt++);
        for(i=0;i<strlen(s);i++)
        {
            if(s[i]<='z'&&s[i]>='a')
                printf("%c",map[s[i]-'a']);
            else
                printf("%c",s[i]);
        }
        puts("");
    }
    
    
    
    
    //system("pause");
    return 0;
} 
