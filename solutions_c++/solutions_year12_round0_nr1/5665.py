#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;





int main(){
    char save[27]="yhesocvxduiglbkrztnwjpfmaq";
    int n;
    scanf("%d",&n);
    int z=1;
    FILE *f = fopen("A.out","w+");
    while(n--)
    {
    getchar();
     char s[100]="";
     scanf("%[^\n]s",s);
     fprintf(f,"Case #%d: ",z++);
     for(int i=0;i<strlen(s);i++)
     {
             if(s[i] != ' ')fprintf(f,"%c",save[s[i]-'a']);
             else fprintf(f," ");
             }
     fprintf(f,"\n");          
    }    
    
    return 0;
    }
