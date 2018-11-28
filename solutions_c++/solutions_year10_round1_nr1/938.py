#include<cstdio>
#include<cstring>
char s[55][55];
bool vic(int n,int k,char ch)
{
	int a,b,c,d;
	for(int row=0;row<n;++row)
		for(int col=0;col<n;++col)
			if(s[row][col]==ch)
			{
				a=b=c=d=1;
				for(int i=1;i<k;++i)
				{
					if(row+i<n&&s[row+i][col]==ch)
						++a;
					if(row+i<n&&col+i<n&&s[row+i][col+i]==ch)
						++b;
					if(col+i<n&&s[row][col+i]==ch)
						++c;
					if(row-i>=0&&col+i<n&&s[row-i][col+i]==ch)
						++d;
				}
				if(a==k||b==k||c==k||d==k)
					return true;
			}
	return false;
}
int main()
{
	FILE *in=fopen("A-large.in","r"),*out=fopen("A-large.out","w");
	int t;
	fscanf(in,"%d",&t);
	for(int c=1;c<=t;c++)
	{
		int n,k;
		fscanf(in,"%d%d",&n,&k);
		for(int l=0;l<n;++l)
		{
			fscanf(in,"%s",s[l]);
			int i,j;
			for(i=j=strlen(s[l]);i>=0;)
			{
				do
					--i;
				while(i>=0&&s[l][i]=='.');
				if(i>=0)
					s[l][--j]=s[l][i];
			}
			strnset(s[l],'.',j);
//			printf("%s\n\n",s[l]);
		}
		int r=vic(n,k,'R')?1:0;
		r+=vic(n,k,'B')?2:0;
		fprintf(out,"Case #%d: %s\n",c,r==0?"Neither":r==1?"Red":r==2?"Blue":"Both");
	}
	fclose(in);
	fclose(out);
	return 0;
}
