#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char *argv[])
{
    freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1", "w", stdout);
    char s[200];
    int n, i, j, len;
    scanf("%d",&n);
    gets(s);
    for(i=1;i<=n;i++){
        printf("Case #%d: ",i);
        gets(s);
        len=strlen(s);
        for(j=0;j<len;j++){
            if(s[j] == ' ')printf("%c",s[j]);
            else if(s[j] == 'a')printf("y");
            else if(s[j] == 'b')printf("h"); 
            else if(s[j] == 'c')printf("e"); 
            else if(s[j] == 'd')printf("s"); 
            else if(s[j] == 'e')printf("o"); 
            else if(s[j] == 'f')printf("c"); 
            else if(s[j] == 'g')printf("v"); 
            else if(s[j] == 'h')printf("x"); 
            else if(s[j] == 'i')printf("d"); 
            else if(s[j] == 'j')printf("u"); 
            else if(s[j] == 'k')printf("i"); 
            else if(s[j] == 'l')printf("g"); 
            else if(s[j] == 'm')printf("l"); 
            else if(s[j] == 'n')printf("b"); 
            else if(s[j] == 'o')printf("k"); 
            else if(s[j] == 'p')printf("r"); 
            else if(s[j] == 'q')printf("z"); 
            else if(s[j] == 'r')printf("t"); 
            else if(s[j] == 's')printf("n"); 
            else if(s[j] == 't')printf("w"); 
            else if(s[j] == 'u')printf("j"); 
            else if(s[j] == 'v')printf("p");
            else if(s[j] == 'w')printf("f"); 
            else if(s[j] == 'x')printf("m"); 
            else if(s[j] == 'y')printf("a"); 
            else printf("q");                
        }
        printf("\n");  
    }
    fclose(stdin);
	fclose(stdout);
    return 0;
}
