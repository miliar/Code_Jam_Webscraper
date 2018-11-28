#include <iostream>
#include <algorithm>
#include <cstring>
#include <functional>

using namespace std;
int mat[30];
char res[30];
bool cmp(int a,int b)
{
	return a>b;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("1.out","w",stdout);
	int T,i,j,k,mm,ma,p,s,len,ss;
	int *pp;
	char str[30];
	scanf("%d",&T);
	
	for(i=1;i<=T;++i)
	{
		scanf("%s",str);
		len=strlen(str);
		j=len-1;
		k=0;
		while(j>=0)
		{
			mat[k]=str[j]-'0';
			if(k>0&&mat[k]<mat[k-1])
			{
				mm=mat[k];
				sort(mat,mat+k);
				pp=upper_bound(mat,mat+k,mm);
				ma=*pp;
				*pp=mm;
				for(p=0;p<j;++p)
					res[p]=str[p];
				res[p]=ma+'0';
				p++;
				s=0;
				for(;p<len;++p)
					res[p]=mat[s++]+'0';
				res[p]='\0';
				break;
			}
			k++,--j;
		}
		if(j<0)
		{
			sort(mat,mat+len);
			for(ss=0;ss<len;++ss)
			{
				if(mat[ss]!=0)
				{
					res[0]=mat[ss]+'0';
					mat[ss]=0;
					sort(mat,mat+len);
					break;
				}
			}
			for(p=1;p<=len;++p)
			{
				res[p]=mat[p-1]+'0';
			}
			res[p]='\0';
		}
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
	return 0;
}