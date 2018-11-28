#include<stdio.h>
int main()
{
    char map[]="yhesocvxduiglbkrztnwjpfmaq";
    int t;
    scanf("%d",&t);
    char c;
    scanf("%c",&c);
    for(int i=0;i<t;i++)
    {
        char *in=new char[300];
        //getch();
        gets(in);
        int j=0;
        while(in[j]!='\0')
        {
            if(in[j]==' ')
            {
                j++;
                continue;
            }
            in[j]=map[in[j]-97];
            j++;
        }
        printf("Case #%d: ",i+1);
        puts(in);
        //printf("\n");
    }
    return 0;
}
