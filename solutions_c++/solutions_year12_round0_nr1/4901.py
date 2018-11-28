//#include<conio.h>
#include<stdio.h>

int main()
{
    freopen("A-small-attempt8.in","r",stdin);
    freopen("result.txt","w",stdout);
    int t,i,k;
    char str[103];
    char a[27] = "yhesocvxduiglbkrztnwjpfmaq";
    
    scanf("%d\n",&t);
    
    k = 1;

    while(t--)
    {  
        gets(str);

        for(i=0;str[i]!='\0';i++)
        {
            if(str[i]!=' ')
            str[i] = a[str[i]-'a'];
        }
        printf("Case #%d: %s\n",k++,str);
    }
    
    //getch();
    return 0;
}
