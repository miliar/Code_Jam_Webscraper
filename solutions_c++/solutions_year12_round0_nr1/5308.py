#include<stdio.h>
#include<string.h>
#include<conio.h>


int arr[26]={0};
int temp;

void compute()
{
char str[3][50]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

char str1[3][50]={"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};

for(int k=0;k<3;k++)
{
        for(int i=0;i<strlen(str[k]);i++)
        {
                if(str[k][i]!=' ')
                {
                if(arr[(int)str[k][i]-97]==0)
                arr[(int)str[k][i]-97]=(int)str1[k][i]-97;
                }
        }
}
arr[24]=0;
arr[25]=16;
arr[16]=25;
}

int main()
{
compute();
int t,i,test;
freopen("A-small-attempt0.in","r",stdin);
freopen("aaa1.txt","w",stdout);
char temp[100];
scanf("%d",&t);
getchar();
for(test=1;test<=t;test++)
{
          gets(temp);
          printf("Case #%d: ",test);
          for(i=0;i<strlen(temp);i++)
          {
                                     
                                     if(temp[i]!=' ')
                                     printf("%c",(arr[((int)temp[i]-97)]+97));
                                     else printf("%c",temp[i]);
                                     
          }
          printf("\n");
}
getch();
return 0;
}
//freopen("example.txt","r",stdin);
//freopen("aaa.txt","w",stdout);
