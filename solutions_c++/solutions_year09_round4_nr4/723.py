#include <iostream>
#include<fstream>
#include <string>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include<math.h>
#include<sstream>
#include <algorithm>
#include <windows.h>   
using namespace std;
//ofstream fo("G:\\ASmallAns.txt",ios_base::out);
//char anss[100] ={0};
//::sprintf(anss,"Case #%d: %0.8lf\n",n,ans[c]);
double a[100][3];
double Count(int x,int y)
{
	return a[x][2]+a[y][2]+sqrt((a[x][0]-a[y][0])*(a[x][0]-a[y][0])+(a[x][1]-a[y][1])*(a[x][1]-a[y][1]));
}
int main()
{
	int t,n,m,i;
	double ans,as;
	ofstream fo("G:\\BSmallAns.txt",ios_base::out);
	scanf("%d",&t);
	for (n=1;n<=t;n++)
	{
		scanf("%d",&m);
		for (i=0;i<m;i++)
		{
			scanf("%lf%lf%lf",&a[i][0],&a[i][1],&a[i][2]);
		}
		//fo<<"Case #"<<n<<": ";
		printf("Case #%d:",n);
		if (m==1)
			//fo<<a[0][2]<<endl;
			printf("%0.10lf\n",a[0][2]);
		else
		if (m==2)
		{
			if (a[0][2]>a[1][2])
				//fo<<a[0][2]<<endl;
				printf("%0.10lf\n",a[0][2]);
			else
				//fo<<a[0][1]<<endl;
				printf("%0.10lf\n",a[1][2]);
		}
		else
		{
			ans=0;
			as=Count(0,1);
			if (a[2][2]>as)
				as=a[2][2];
			if (as>ans)
				ans=as;
			as=Count(0,2);
			if (a[1][2]>as)
				as=a[1][2];
			if (as<ans)
				ans=as;
			as=Count(1,2);
			if (a[0][2]>as)
				as=a[0][2];
			if (as<ans)
				ans=as;
			char anss[100] ={0};
			//::sprintf(anss,"%0.10lf\n",ans/2);
			//fo<<anss;
			printf("%0.10lf\n",ans);
		}
	}
	return 0;
}