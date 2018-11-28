#include <stdio.h>

int main()
{
    //freopen("C:\\Users\\S@BB!R\\Desktop\\input.txt","r",stdin);
    //freopen("C:\\Users\\S@BB!R\\Desktop\\output.txt","w",stdout);
    
    int kase,i,j=1;
    char str[110];
    scanf("%d", &kase);
    getchar();
    while(kase--)
    {
        gets(str);
        printf("Case #%d: ", j++);
        for(i=0;str[i];i++)
        {
            if(str[i]=='a')printf("y");
            else if(str[i]=='y')printf("a");
            else if(str[i]=='o')printf("k");
            else if(str[i]=='e')printf("o");
            else if(str[i]=='z')printf("q");
            else if(str[i]=='q')printf("z");
            else if(str[i]=='b')printf("h");
            else if(str[i]=='c')printf("e");
            else if(str[i]=='d')printf("s");
            else if(str[i]=='f')printf("c");
            else if(str[i]=='g')printf("v");
            else if(str[i]=='h')printf("x");
            else if(str[i]=='i')printf("d");
            else if(str[i]=='j')printf("u");
            else if(str[i]=='k')printf("i");
            else if(str[i]=='l')printf("g");
            else if(str[i]=='m')printf("l");
            else if(str[i]=='n')printf("b");
            else if(str[i]=='p')printf("r");
            else if(str[i]=='r')printf("t");
            else if(str[i]=='s')printf("n");
            else if(str[i]=='t')printf("w");
            else if(str[i]=='u')printf("j");
            else if(str[i]=='v')printf("p");
            else if(str[i]=='w')printf("f");
            else if(str[i]=='x')printf("m");
            else printf("%c", str[i]);
        }
        printf("\n");
    }
    return 0;
}
            
