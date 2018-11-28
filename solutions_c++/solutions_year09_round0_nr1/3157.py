#include<stdio.h>
using namespace std;
char libr[5005][16];
int result[1000]={0};
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int l,d,n;
    scanf("%d%d%d",&l,&d,&n);
    for(int a=0;a<d;a++){    scanf("%s",libr[a]);  }
    for(int m=0;m<n;m++)
    {
            char nuevo[1000];
            scanf("%s",nuevo);  
            int words[5005][100];
            for(int g=0;g<5005;g++){  for(int t=0;t<100;t++){  words[g][t]=0; } }
            int cont=0;
            for(int a=0;nuevo[a]!='\0';a++)
            {
                    if(nuevo[a]=='(')
                    {
                                     int b=a;
                          for(;nuevo[b]!=')';b++){  words[cont][nuevo[b]-'a']=1;  }
                          a=b;    cont++;
                    }
                    else
                    {
                        words[cont][nuevo[a]-'a']=1;  cont++;
                    }
            }
            for(int b=0;b<d;b++)
            {
                    int si=0;
                    for(int z=0;libr[b][z]!='\0';z++)
                    {
                            if(words[z][libr[b][z]-'a']!=1){ si++;   }
                    }
                    if(si==0){  result[m]++; }
            }
            
    }
    for(int a=0;a<n;a++)
    {
            printf("Case #%d: %d\n",a+1,result[a]);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
