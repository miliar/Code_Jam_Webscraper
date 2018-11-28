#include<stdio.h>
#include<iostream>
#include<map>
using namespace std;
int main()
{
	int t;
	int te=1;
	scanf("%d",&t);
	pair<int ,int> qw;
	while(te<=t)
	{
		int c,d;
		scanf("%d",&c);
		map<pair<int , int> , int > mp,de;
		//		char base[10]="QWERASDF";
		for(int i=0;i<26;i++)
		{
			for(int j=0;j<26;j++)
			{
				qw.first=65+i;
				qw.second=65+j;
				de[qw]=23;
				mp[qw]=23;
			}
		}
		int value;
		char s[1000];
		while(c--)
		{
			//			scanf("%c%c%c",&qw.first,&qw.second,&value);
			scanf("%s",s);
			qw.first=s[0];
			qw.second=s[1];
			value=s[2];
			mp[qw]=value;
		}
		scanf("%d",&d);
		while(d--)
		{
			scanf("%s",s);
			qw.first=s[0];
			qw.second=s[1];
			//scanf("%c%c",&qw.first,&qw.second);
			//	scanfp
			de[qw]=1;
			qw.first=s[1];
			qw.second=s[0];
			de[qw]=1;
		}
		int a[1000],cou=0;
		int n;
		scanf("%d",&n);
		int x;
		scanf("%s",s);
		for(int i=0;i<n;i++)
		{
			x=s[i];
			//	scanf("%c",&x);	
			if(cou==0)
			{
				a[cou]=x;
				cou++;
			}
			else
			{
				qw.first=a[cou-1];
				qw.second=x;
				int flag=0;
				if(mp[qw]!=23)
				{
					x=mp[qw];
					cou--;
					a[cou]=x;
					cou++;
					flag=1;
					//	a.push_back(x);
				}
				qw.second=a[cou-1];
				qw.first=x;
				if(mp[qw]!=23 && flag==0)
				{
					x=mp[qw];
					cou--;
					a[cou]=x;
					cou++;
					flag=1;
					//	a.push_back(x);
				}
				if(flag==0)
				{
					qw.first=x;
					int k=0;
					while(k<cou)
					{

						qw.second=a[k];
						if(de[qw]!=23)
						{

							cou=0;
							flag=1;
							break;
						}
						k++;
					}
				}
				if(flag==0)
				{
					a[cou]=x;
					cou++;
				}




			}
		}
		printf("Case #%d: [",te);
		for(int i=0;i<cou;i++)
		{
			if(i==0)
			{
				printf("%c",a[i]);
			}
			else
			{
				printf(", %c",a[i]);
			}
		}
		te++;
		printf("]\n");
	}
	return 0;
}
