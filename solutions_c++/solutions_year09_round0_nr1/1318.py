#include<cstdio>
#include<cstring>

int main()
{

int L,D,num;
char words[5001][16];
scanf("%d %d %d\n",&L,&D,&num);
for(int j=0;j<D;j++)
scanf("%s\n",words[j]);

for(int i=0;i<num;i++)
{
int b[16]={0},pos=0,f=0;
char str[10000];

scanf("%s\n",&str);

	for(int j=0;j<strlen(str);j++)
	{
	if(str[j]=='(') { f=1; continue; }
	if(str[j]==')') { f=0;pos++; continue; }
	if(f==1) { b[pos]=b[pos]|(1<<(str[j]-97));  }
	else {  b[pos]=b[pos]|(1<<(str[j]-97)); pos++;  } 
	}

int c=0;
for(int j=0;j<D;j++)
{
int k=0;
for(k=0;k<L;k++)
if((1<<(words[j][k]-97)) & b[k]) continue; else break;
if(k==L) c++;
}	

printf("Case #%d: %d\n",i+1,c);

}


return 0;
}
