#include<iostream.h>

int main()
{
    char s[]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
    char str[1000];
    int T=0,i,j=1,k,c;
    cin>>T;
    cin.ignore();
    while(T>0)
    {
            
            gets(str);
            for(i=0;str[i]!=NULL;i++)
            {
                                     if(str[i]==' ')
                                                  continue;
                                     for(k=0;str[i]!=s[k];k++);
                                     str[i]='a'+k;
            }
            printf("Case #%d: ",j++);
            puts(str);
            T--;
    }
    return 0;
}
