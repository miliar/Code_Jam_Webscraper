#include<cstdio>
#include<iostream>
using std::swap;
bool table[5000][15][26];
int main()
{
int len,d,n,i,j,k,t;
char word[16];
scanf("%d%d%d",&len,&d,&n);
getc(stdin);
for(i=0;i<d;++i)
	{
	gets(word);
	for(j=0;j<len;++j)
		table[i][j][word[j]-'a']=true;
	}
int candi[5000];
int nCandi;
char ch;
int num;
int list[5000];
for(t=1;t<=n;++t)
	{
	i=0;
	for(nCandi=0;nCandi<d;++nCandi)
		candi[nCandi]=nCandi;
	while((ch=getc(stdin))!='\n' && i<len)
		{
		num=0;
		if(ch=='(')
			while((ch=getc(stdin))!=')')
				list[num++]=ch-'a';
		else
			list[num++]=ch-'a';
		for(j=0;j<nCandi;)
			{
			for(k=0;k<num;++k)
				if(table[candi[j]][i][list[k]])
    				break;
			if(k==num)
				candi[j]=candi[nCandi-1],--nCandi;
			else ++j;
			}
		++i;
		}
	if(ch=='\n')
		printf("Case #%d: %d\n",t,nCandi);
	else
		{
		printf("Case #%d: 0\n",t);
		scanf("%*s"),getc(stdin);
		}	
	}
}
