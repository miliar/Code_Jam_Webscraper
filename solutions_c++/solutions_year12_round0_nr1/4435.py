#include<cstdio>

int hash[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    int test,ch;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d",&test);fgetc(stdin);
    
    for(int i=0;i<test;i++)
    {
            printf("Case #%d: ",i+1);
            while((ch=fgetc(stdin))!='\n' && ch!=EOF)
            {
                if(ch==' ')
                printf(" ");
                else
                printf("%c",hash[ch-'a']);
            }
            printf("\n");
    }
    
    return 0;
}
