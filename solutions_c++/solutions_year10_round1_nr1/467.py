#pragma warning(disable:4996)
#pragma warning(disable:4010)//注释
#include<iostream>
#include<cstdio>
#include<ctime>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<cmath>
#include<cstring>
#include<map>
#include<string>
using namespace std;
const int sup=100;
char joi[sup][sup];
char fin[sup][sup];
int n,k;
int main()
{
	int len;
	int t;

	freopen("A.in","r",stdin);
	freopen("A.txt","w",stdout);
	scanf("%d",&t);
	for(int pzj=1;pzj<=t;++pzj)
	{
		scanf("%d %d",&n,&k);
		for(int i=0;i<n;++i)
			fill(fin[i],fin[i]+n,'.');
		for(int i=0;i<n;++i)
		{
			int k=0;
			scanf("%s",joi[i]);
			len=strlen(joi[i]);
			for(int j=len-1;j>=0;--j)
				if('.'!=joi[i][j])
				{
					fin[i][len-k-1]=joi[i][j];
					++k;
				}
		}
		//for(int i=0;i<n;++i)
			//printf("%s\n",fin[i]);
		printf("Case #%d: ",pzj);
		int r=0,b=0;
		string stra;
		string strb;
		string strc;
		string strd;
		string red="";
		string blue="";
		for(int i=0;i<k;++i)
		{
			red+="R";
			blue+="B";
		}
		bool find=0;

		bool bl=0,re=0;
		for(int jj=0;jj<n;++jj)
		{
			strc="";
			for(int i=0,j=jj;j<n&&i<n;++i,++j)
				strc+=fin[i][j];
			if(strc.find(red)<strc.length())
			{
				if(strc.find(blue)<strc.length())
				{
					find=1;
					printf("Both\n");
					break;
				}
				else
				{
					//cout<<strc<<endl;
					re=1;
				}
			}
			else if(strc.find(blue)<strc.length())
			{
				bl=1;
			}
		}
		if(find)
			continue;
		strc="";
		for(int jj=0;jj<n;++jj)//反对角线
		{
			strc="";
			for(int i=0,j=jj;j>=0&&i<n;++i,--j)
				strc+=fin[i][j];
			if(strc.find(red)<strc.length())
			{
				
				if(strc.find(blue)<strc.length())
				{
					find=1;
					printf("Both\n");
					break;
				}
				else
					re=1;
			}
			else if(strc.find(blue)<strc.length())
			{
				bl=1;
			}
		}

		if(find)
			continue;
	strc="";
		for(int jj=0;jj<n;++jj)//反对角线
		{
			strc="";
			for(int i=n-1,j=jj;i>=0&&j<n;--i,++j)
				strc+=fin[j][i];
			if(strc.find(red)<strc.length())
			{
				
				if(strc.find(blue)<strc.length())
				{
					find=1;
					printf("Both\n");
					break;
				}
				else
					re=1;
			}
			else if(strc.find(blue)<strc.length())
			{
				bl=1;
			}
		}
		
		if(find)
			continue;

		strc="";
		for(int i=0;i<n;++i)
		{
			stra="";
			strb="";
			strc="";
			strd="";
			for(int j=0,ii=i;j<n&&ii<n;++j,++ii)
				strc+=fin[ii][j];
			if(strc.find(red)<strc.length())
			{
			
				if(strc.find(blue)<strc.length())
				{
					find=1;
					printf("Both\n");
					break;
				}
				else
					re=1;
			}
			else if(strc.find(blue)<strc.length())
			{
				bl=1;
			}
			for(int j=0,ii=i;j<n&&ii<n;++j,++ii)
				strc+=fin[ii][j];
			for(int j=0;j<n;++j)
			{
				stra+=fin[i][j];
				strb+=fin[j][i];
			}
			//int ri=stra.find(red);
			if(stra.find(red)<stra.length() || strb.find(red)<strb.length())
			{
		
				if(stra.find(blue)<stra.length() || strb.find(blue)<strb.length())
				{
					find=1;
					printf("Both\n");
					break;
				}
				else
				{
					//cout<<i<<"\n";
					re=1;
					//cout<<stra<<" " <<strb<<endl;
				}
			}
			else if(stra.find(blue)<stra.length() || strb.find(blue)<strb.length())
			{
				bl=1;
			}
				
		}
		if(find)
			continue;
		else if(re && bl)
		{
			printf("Both\n");
			continue;
		}
		if(re)
			printf("Red\n");
		else if(bl)
			printf("Blue\n");
		else if(!find)
			printf("Neither\n");
	}
	return 0;
}