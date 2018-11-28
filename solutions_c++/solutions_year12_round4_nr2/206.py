#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef long long LINT;

void main()
{
	int t;
	cin>>t;
	for(int ii=0; ii<t; ii++)
	{
		int n,w,l;
		pair<int,int> r[1000];
		int xx[1000],yy[1000];
		cin>>n>>w>>l;
	
		for(int i=0; i<n; i++)
		{
			cin>>r[i].first;
			r[i].second=i;
		}

		sort(r,r+n);

		int x=0,y=0;
		int y1=0;
		for(int i=n-1; i>=0; i--)
		{
			if(x+r[i].first>w)
			{
				x=0;
				y+=y1+r[i].first;
			}
			if(y>l)
				cout<<"ERR";

			if(x==0)
			{
				x-=r[i].first;
				y1=r[i].first;
			}

			xx[r[i].second]=x+r[i].first;
			yy[r[i].second]=y;

			x+=r[i].first*2;
		}

		cout<<"Case #"<<ii+1<<": ";
		for(int i=0; i<n; i++)
			cout<<xx[i]<<' '<<yy[i]<<' ';
		cout<<endl;
	}
}