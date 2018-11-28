//Q2009 pA
#include <stdio.h>
#include <string.h>
int main()
{
	char list[5001][16],line[501];
	bool map[16][26]={0},p,yn;
	int l,d,n,x,y,z,i,s,len;
	FILE *fin=fopen("A-small.in","r"), *fout=fopen("A-small.out","w");
	fscanf(fin,"%d%d%d",&l,&d,&n);
	fgets(line,500,fin);
	for(x=0;x<d;++x)
		fgets(list[x],15,fin);
	for(y=1;y<=n;++y)
	{
		fgets(line,500,fin);
		len=strlen(line);
		memset(map,0,sizeof(map));
		s=i=p=0;
		for(x=0;x<len;++x)
		{
			if('a'<=line[x] && line[x]<='z')
			{
				map[i][line[x]-'a']=1;
				if(!p)
					++i;
			}
			else if(line[x]=='(')
				p=1;
			else if(line[x]==')')
			{
				p=0;
				++i;
			}
		}
		for(x=0;x<d;++x)
		{
			yn=1;
			for(z=0;z<l;++z)
			{
				if(!map[z][list[x][z]-'a'])
				{
					yn=0;
					break;
				}
			}
			if(yn)
			{
				++s;
			}
		}
		fprintf(fout,"Case #%d: %d\n",y,s);
	}
	return 0;
}
