#include<iostream>
using namespace std;
int main()
{
	//freopen("cin.txt","r",stdin);
	//freopen("cout.txt","w",stdout);
	//freopen("cin1.txt","r",stdin);
	//freopen("cout1.txt","w",stdout);
	freopen("cin2.txt","r",stdin);
	freopen("cout2.txt","w",stdout);
	int zu;
	cin>>zu;
	for(int ii=1;ii<=zu;ii++)
	{
		printf("Case #%d: ",ii);
		int m;
		cin>>m;
		int he = 0;
		int x = 0;
		int d = 1e9;
		for(int i=0;i<m;i++)
		{
			int z;
			cin>>z;
			he^=z;
			x+=z;
			d = min(d,z);
		}
		if(he==0)
		{
			printf("%d\n",x-d);
		}
		else
		{
			puts("NO");
		}

	}
}