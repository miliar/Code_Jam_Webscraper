#include<algorithm>
#include<cstdio>
#include<iostream>
#include<vector>
#include<cmath>
#include<map>
#include<sstream>
#include<cstring>
#include<string.h>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("outf.txt","w",stdout);
	int test;
	scanf("%d",&test);
	for(int x=0;x<test;x++)
	{
		string a,b;int a1,b1,res=0;
		cin >> a >> b;stringstream ss(a);ss >> a1;stringstream sb(b);sb >> b1; 
		for(int i=a1;i<=b1;i++){
			stringstream ti;ti << i;a=ti.str();a+=a;
			for(int j=i+1;j<=b1;j++){
				stringstream tj;tj << j;b=tj.str();
				if( strstr (a.c_str(),b.c_str()))res++;
			}
		}
		printf("Case #%d: %d\n",x+1,res);
	}
		
	return 0;
}