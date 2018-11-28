#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    int n,length;
    char str[101];
    char ch[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    scanf("%d\n",&n);
    for(int i=0;i<n;i++)
    {
        gets(str);
        length=strlen(str);
        for(int j=0;j<length;j++)
        {
            if(str[j]!=' ')
                str[j]=ch[str[j]-97];
        }
        
        printf("Case #%d: %s\n",i+1,str);
    }
  //  system("pause");
    return 0;
}
