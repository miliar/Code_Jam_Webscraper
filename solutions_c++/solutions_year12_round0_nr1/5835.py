#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int t,i,j;
    char a[101],b[101],c[]="yhesocvxduiglbkrztnwjpfmaq";
    scanf("%d\n",&t);
    for(i=1;i<=t;i++)
    {
        cin.getline(a,101);
        j=0;
        printf("Case #%d: ",i);
        while(a[j]!='\0')
        {
            if(a[j]!=' ')
                printf("%c",b[j]=c[a[j]-'a']);
            else
                printf("%c",b[j]=a[j]);
            j++;
        }
        printf("\n");
    }
    return 0;
}
