#include "stdio.h"
#include "iostream"
#include "string.h"
#include "iomanip"
#include "cmath"
#include "memory.h"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"
#include "list"
#include "set"

using namespace std;
int cmp(const void *a,const void *b)
{
	char *l1=(char *)a;
	char *l2=(char *)b;
	return *l1-*l2;
}
int main()
{
	char c[30];
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>c;
		int len=strlen(c);
		int flag=0;
		int pos;
		for (int j=len-1;j>=1;j--)
		{
			if (c[j-1]<c[j])
			{
				pos=j-1;
				flag=1;
				break;
			}
		}
		if (flag)
		{
			char mini='9'+1;
			char cur;
			for (int j=pos+1;j<len;j++)
			{
				if (c[j]>c[pos]&&c[j]<mini)
				{
					mini=c[j];
					cur=j;
				}
			}
			char b[30]={};
			int ind=0;
			for (int j=pos;j<len;j++)
			{
				if (j==cur) continue;
				b[ind++]=c[j];
			}
			qsort(b,ind,sizeof(char),cmp);
			c[pos]=c[cur];
			for (int j=pos+1;j<len;j++)
				c[j]=b[j-pos-1];
			cout<<"Case #"<<i<<": ";
			cout<<c<<endl;
		}
		else
		{
			qsort(c,len,sizeof(char),cmp);
			if (c[0]=='0')
			{
				char p;
				for (int j=1;j<len;j++)
					if (c[j]!='0')
					{
						p=c[j];
						c[j]=c[0];
						c[0]=p;
						break;
					}
			}
				for (int j=len;j>=2;j--)
					c[j]=c[j-1];
				c[1]='0';
				c[len+1]=0;
				cout<<"Case #"<<i<<": ";
				cout<<c<<endl;
		}

	}
}