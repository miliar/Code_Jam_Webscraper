#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

bool a[200][200];
bool b[200][200];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,l,t,n,m;
	int x1,x2,y1,y2;
	bool p;
	int ans;
	cin>>t;
	for(l=1;l<=t;++l)
	{
		for(i=1;i<=100;++i)
			for(j=1;j<=100;++j)
				a[i][j] = b[i][j] = false;
		cin>>n;
		for(k=0;k<n;++k)
		{
			cin>>x1>>y1>>x2>>y2;
			for(i=x1;i<=x2;++i)
				for(j=y1;j<=y2;++j)
				{
					a[i][j] = true;
					b[i][j] = true;
				}
		}
			ans = 0;
			p = true;
			while(p)
			{
				p = false;
				for(i=1;i<=100;++i)
					for(j=1;j<=100;++j)
						if(a[i][j])
						{
							p = true;
							if(b[i-1][j] == false && b[i][j-1] == false)
								a[i][j] = false;
						}
						else
							if(b[i-1][j] == true && b[i][j-1] == true)
								a[i][j] = true;
				for(i=1;i<=100;++i)
					for(j=1;j<=100;++j)
						b[i][j] = a[i][j];
				if(p)
					++ans;
			}
			cout<<"Case #"<<l<<": "<<ans<<endl;

	}
	return 0;
}