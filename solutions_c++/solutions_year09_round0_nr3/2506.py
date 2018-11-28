#include <stdio.h>

using namespace std;
typedef char* cadena;
cadena entrada=new char[101];
cadena frase="welcome to code jam";
int cont;
int j;
void analizar(int index,int start)
{
    if(index==19) {cont++;return;}
    for(int i=start;i<j;i++)
    {
        if(entrada[i]==frase[index])
        {
            analizar(index+1,i+1);
        }
    }
    return;
}
int main()
{
    int n;
    int c;
    int index=0;
    freopen("input.in","r",stdin);
    scanf("%i",&n);
    FILE *f=fopen("small.out","w");
    while(getchar()!='\n');
    for(int i=1;i<=n;i++)
    {
        j=-1;
        do
        {
            c=getchar();
            entrada[++j]=c;
        }while(c!='\n' && c!=EOF);
        cont=0;
        analizar(index,index);
        fprintf(f,"Case #%i: ",i);
        if(cont<10)    fprintf(f,"000");
        else  if(cont<100)    fprintf(f,"00");
        else  if(cont<1000)    fprintf(f,"0");
        fprintf(f,"%i\n",cont);
    }
    fclose(f);
    return 0;
}
