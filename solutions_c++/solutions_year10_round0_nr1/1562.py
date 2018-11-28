// Snapper Chain.cpp : 定义控制台应用程序的入口点。
//


#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	//freopen("debug\\in.txt","r",stdin);
	//freopen("debug\\out.txt","w",stdout);
	int repeat,cases;
	cases=1;
	int m,n,t;
	cin>>repeat;
	while(repeat--)
	{
		
		cin>>m>>n;
		printf("Case #%d: ",cases++);
		t=pow(2,1.0*m);
		if(n%t!=t-1)
			printf("OFF\n");
		else printf("ON\n");
	}
	return 0;
}

