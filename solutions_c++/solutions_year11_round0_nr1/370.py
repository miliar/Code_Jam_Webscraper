#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#pragma comment(linker, "/STACK:167772160")
typedef long long int64;
using namespace std;
int tes,o,i,j,n,x1,x2,t1,t2,time,x[101];
char c[101];
int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>tes;
	for(o=0;o<tes;o++)
	{
		cin>>n;
		for(i=1;i<=n;i++)cin>>c[i]>>x[i];

		time=0;

		x1=1;x2=1;t1=0;t2=0;

		for(i=1;i<=n;i++)
		{
			if(c[i]=='B')
			{
				time=max(t1+abs(x[i]-x1)+1,time+1);
				x1=x[i];t1=time;
			}else
			{
				time=max(t2+abs(x[i]-x2)+1,time+1);
				x2=x[i];t2=time;
			}
		}
		cout<<"Case #"<<o+1<<": "<<time<<endl;
	}

}