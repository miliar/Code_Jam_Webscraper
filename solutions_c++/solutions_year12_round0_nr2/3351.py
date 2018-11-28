#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

main()
{
	int t, i, j, n, s, p, y, ti;
	cin>>t;
	for(i=0; i<t; i++)
	{
		cin>>n>>s>>p;
		y=0;
		for(j=0; j<n; j++)
		{
			cin>>ti;
			if(ti>=3*p-2)
				y++;
			else if(ti>=3*p-4 && s>0 && ti >=2)
			{
				y++;
				s--;
			}	
		}
		cout<<"Case #"<<(i+1)<<": "<<y<<endl;
	}
}
