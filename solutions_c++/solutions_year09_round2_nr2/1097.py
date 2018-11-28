#include<iostream>
using namespace std;
char s[50];
char t[50];
int cmp(const void *a,const void *b)
{
    return *(char*)a>*(char*)b?1:-1;
}
int main()
{
    int cases;
    scanf("%d",&cases);
    while(getchar()!='\n');
    for(int cca=1;cca<=cases;cca++)
    {
         gets(s);
         int len=strlen(s);
         int i=len-2;
         int p=0;
         t[p++]=s[len-1];
         while(i>=0)
         {
             if(s[i]<s[i+1])
             break;
             t[p++]=s[i];
             i--;
         }
         printf("Case #%d: ",cca);
         if(i==-1)
         {
             qsort(t,p,sizeof(t[0]),cmp);
             for(int j=0;j<p;j++)
             if(t[j]!='0')
             {
                 printf("%c",t[j]);
                 t[j]='0';
                 break;
             }
             for(int j=0;j<p;j++)
             printf("%c",t[j]);
             printf("\n");
         }
         else
         {
             for(int k=0;k<i;k++)
             printf("%c",s[k]);
             qsort(t,p,sizeof(t[0]),cmp);
             for(int j=0;j<p;j++)
             if(t[j]>s[i])
             {
                 printf("%c",t[j]);
                 t[j]=s[i];
                 break;
             }
             for(int j=0;j<p;j++)
             printf("%c",t[j]);
             printf("\n");
         }
    }
}
                
