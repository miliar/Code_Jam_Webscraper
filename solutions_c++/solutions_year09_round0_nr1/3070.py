#include<stdio.h>
#include<string.h>
char words[5000][15];
char test[15][60];
int num[15];
//char test2[50];
//char one[17];
int main()
{
    int l,d,n,i,j,a,count;
    char flag='0';
    char brak='0';
    char match='1';
    FILE *f1=fopen("A-large.in","r");
    FILE *f2=fopen("A-largea.out","w");
    fscanf(f1,"%d%d%d",&l,&d,&n);
    for(i=0;i<d;i++)
    {
     fscanf(f1,"%s",&words[i]);
    }
    fscanf(f1,"%c",&test[0][0]);
for(a=0;a<n;a++)
{
    brak='0';
    j=0;
    i=0;
    while(true)
    {
           j=0;
     fscanf(f1,"%c",&test[i][j]);
     if(test[i][j] == '\n')
     break;
     if(test[i][j] == '(')
     brak='1';
     j++;
     
     while(brak == '1')
     {
     fscanf(f1,"%c",&test[i][j]);
     j++;
     if(test[i][j-1] == ')')
     brak='0';
     }
     num[i]=j;
     i++;
     
     //printf("%s\n",test2);
    }
/*for(i=0;i<num[0];i++)
{
 printf("%c",test[0][i]);
}
printf("\n");*/
count=0;
    for(i=0;i<d;i++)
    {
    match='1';
     for(j=0;j<l;j++)
     {
            if(strchr(test[j],words[i][j]) != NULL && strchr(test[j],words[i][j]) >= test[j] && strchr(test[j],words[i][j]) < test[j]+num[j])
            {
             //printf("i = %d j =%d\n",i,j);       
            }
            if(strchr(test[j],words[i][j]) == NULL || strchr(test[j],words[i][j]) < test[j] || strchr(test[j],words[i][j]) >= test[j]+num[j])
            {
                match='0';
                break;
            }
     }
     if(match == '1')
     {
      count++;
     }
    }
    fprintf(f2,"Case #%d: %d\n",a+1,count);
}
   /* while(test2[i] != '\n')
    {
    scanf("%c",&test[i]);
    i++;
    }*/
    delete num;
    delete test;
    delete words;
    scanf("%8d");
}
