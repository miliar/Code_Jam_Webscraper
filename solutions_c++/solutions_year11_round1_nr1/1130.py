#include<iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <vector>
#include <cstdio>
#include <fstream>
using namespace std;
int main()
{
	int t,i,p1,p2,j=0,num1;
	long long n;
	scanf("%d",&t);
	ofstream of("s.txt");
	while(t--)
	{
		j++;
		num1=1;
		scanf("%lld%d%d",&n,&p1,&p2);
		if(p1!=100&&p2==100||p2==0&&p1)
        {
			of<<"Case #"<<j<<": Broken"<<endl;
			printf("Case #%d: Broken\n",j);
			continue;
		}
		if(p1==0)
        {
			of<<"Case #"<<j<<": Possible"<<endl;
			printf("Case #%d: Possible\n",j);
		continue;
		}
		if(p1%2==0)
		{
			p1/=2;
			num1*=2;
			if(p1%2==0)
			{
			p1/=2;
			num1*=2;
            }
		}
		while(p1%5==0)
		{
			p1/=5;
			num1*=5;
			if(p1%5==0)
			{
			p1/=5;
			num1*=5;
            }
        }
        num1=100/num1;
		if(p1<=n&&num1<=n)
        {
			of<<"Case #"<<j<<": Possible"<<endl;
			printf("Case #%d: Possible\n",j);
		}
		else{
		of<<"Case #"<<j<<": Broken"<<endl;
        printf("Case #%d: Broken\n",j);
		}
	}
	//system("pause");
    return 0;
}
