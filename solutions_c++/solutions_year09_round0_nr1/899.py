#include<iostream>
using namespace std;
char i[5000][16],str[421];
int f[15][26];
int main()
{
	int a,s,d,l,m,n,p,c,l2,b;
	scanf("%d%d%d",&l,&m,&n);
	for(a=0;a<m;a++) scanf("%s",i[a]);
	for(a=0;a<n;a++)
	{
		scanf("%s",str);
		l2=strlen(str);
		for(s=0;s<l;s++) for(d=0;d<26;d++) f[s][d]=0;
		p=0;
		b=0;
		for(s=0;s<l2;s++)
		{
			if( str[s]=='(' ) b=1;
			if( str[s]==')' ){ p++; b=0; }
			if( isalpha(str[s]) )
			{
				f[p][str[s]-'a']=1;
				if( b==0 ) p++;
			}
		}
		c=0;
		for(s=0;s<m;s++)
		{
			for(d=0;d<l;d++) if( !f[d][i[s][d]-'a'] ) break;
			if( d==l ) c++;
		}
		printf("Case #%d: %d\n",a+1,c);
	}
	return 0;
}
