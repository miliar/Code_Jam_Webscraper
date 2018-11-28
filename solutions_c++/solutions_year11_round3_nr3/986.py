#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;
int d[105];
int main()
{
	ofstream of("s.txt");
	int t,i,j,k=0,l,h,n;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		scanf("%d%d%d",&n,&l,&h);
        for(i=0;i<n;i++)
			cin>>d[i];
		of<<"Case #"<<k<<": ";
		for(i=l;i<=h;i++)
		{
		for(j=0;j<n;j++)
		{
			if(i%d[j]==0||d[j]%i==0)
				continue;
			else
				break;
		}
		if(j==n)
		{
           of<<i<<endl;
		   break;
		}
		}
		if(i==h+1)
			of<<"NO"<<endl;
	}
        
	return 0;
}