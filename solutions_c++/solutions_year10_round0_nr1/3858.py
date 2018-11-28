#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<cstring>
#include<string>
#include<map>
#include<queue>
#include<cmath>
#include<vector>
#include<bitset>
#include<sstream>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);


	int t,cas=1,a[123]={0};
	cin>>t;
	//a[1]=1;
//	for(int i=1;i<31;i++)
	//	a[i+1]=2*a[i]+1,cout<<a[i]<<endl;;
	while(t--)
	{
		
		long long n,k;
		cin>>n>>k;
		k++;
		printf("Case #%d: ",cas++);
		if(k%(1<<n)==0)
		{
			puts("ON");
		}
		else puts("OFF");

	}


}
