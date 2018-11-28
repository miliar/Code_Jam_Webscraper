#include <stdio.h>

#define MAXL 15
#define MAXD 5000


using namespace std;
int l;
int d;
int n;
int cont;
typedef char** diccionario;
typedef char*   cadena;
diccionario dic;//;=new  char*[MAXD];
cadena entrada;
int token(int min)
{
   // printf("min:%i",min);
    if(entrada[min]=='(')
        while(entrada[++min]!=')');
  //  printf(",\tmax:%i\n",min);
    return min;
}
void analizar(int min,int max,int index,int j)
{
    if(index==l)
    {
    //    for(int ii=0;ii<index;ii++) printf("%c",dic[j][ii]);printf("\n");
        cont++;
        return;
    }
    int maxx=0;
    int minn=max+1;
    maxx=token(minn);
    if(min==max)
    {
        if(dic[j][index]==entrada[min])
        {
            //printf("%c\tAnalizar (%i,%i,%i,%i)\n",entrada[min],minn,maxx,index+1,j);
         //   for(int ii=0;ii<=index;ii++) printf("%c",dic[j][ii]);printf("\n");
            analizar(minn,maxx,index+1,j);
        }
        return;
    }
    else
    {
        for(int k=min+1;k<max;k++)
        {
            if(dic[j][index]==entrada[k])
            {
                //printf("%c\tAnalizar (%i,%i,%i,%i)\n",entrada[min],minn,maxx,index+1,j);
               // for(int ii=0;ii<=index;ii++) printf("%c",dic[j][ii]);printf("\n");
                analizar(minn,maxx,index+1,j);
            }
        }
        return;
    }

}
int main()
{
    int index=0;
    int max=0;
    int min=0;
    freopen("input.in","r",stdin);
    scanf("%i %i %i",&l,&d,&n);

    dic=new  char*[d];
    for(int i=0;i<d;i++)
        dic[i]=new char[l];
    for(int i=0;i<d;i++)
        scanf("%s",dic[i]);

   /* for(int i=0;i<d;i++)
        printf("%s\n",dic[i]);
*/
    entrada=new char[MAXL*MAXL*MAXL];
    FILE *fil=fopen("large.out","w");
    for(int i=0;i<n;i++)
    {

        cont=0;
        scanf("%s",entrada);
        max=token(min);
        for(int j=0;j<d;j++)
            analizar(min,max,index,j);
 //       printf("Case #%i: %i\n",i+1,cont);
        fprintf(fil,"Case #%i: %i\n",i+1,cont);

      //  printf("min:%i,\tmax:%i\n",min,max);
       // min=max+1;
    }
    fclose(fil);
    return 0;
}
