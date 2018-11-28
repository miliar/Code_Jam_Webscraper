#include<cstdio>
#include<cstring>


int main()
{

int num;
scanf("%d\n",&num);
char *str="welcome to code jam";

for(int i=0;i<num;i++)
{
char data[503];
gets(data);
int M[503][20]={0};
for(int j=0;j<503;j++)
M[j][19]=1;

for(int j=18;j>=0;j--)
for(int k=strlen(data)-1;k>=0;k--)
{
	for(int m=k;m<strlen(data);m++)
	if(data[m]==str[j]) M[k][j]=(M[k][j]+M[m+1][j+1])%10000;
}

printf("Case #%d: %04d\n",i+1,M[0][0]%10000);



}

return 0;
}
