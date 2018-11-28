#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

#define R 5000
#define C 20
using namespace std;



int main(void){
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int l,d,n;
	scanf("%d %d %d\n",&l,&d,&n);
	vector<string> v;
	bool buf[R][C];
	memset(buf,false,sizeof(buf));
	string str;
	for(int i=0;i<d;i++)
	{
		getline(cin,str);
		v.push_back(str);
	}
	int num=d;
	int r=0,c=0;
	for(int i=0;i<n;i++)
	{
		getline(cin,str);
		c=0;
		num=0;
		memset(buf,false,sizeof(buf));
		for(int j=0;j<str.length();j++)
		{
			if(str[j]=='(')
			{
				j++;
				do{
					for(int k=0;k<d;k++)
					{
						if(v[k][c]==str[j])buf[k][c]=true;
					}
					j++;

				}
				while(str[j]!=')');
				c++;
			}
			else{
				for(int k=0;k<d;k++)
				{
					if(v[k][c]==str[j])buf[k][c]=true;
				}
				c++;
			}
		}
	int s;
		for(int i=0;i<d;i++)
		{
			s=0;
			for(int j=0;j<l;j++)
			{
				s+=buf[i][j];
			}
			if(s==l)num++;
		}
		printf("Case #%d: %d\n",i+1,num);
	}
	

	return 0;
}