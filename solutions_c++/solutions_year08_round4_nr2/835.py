#include <iostream>
using namespace std;

long n,m,a,x1,y1,x2,y2;
long i,j,kk,casen;
bool v;
bool suc;

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>casen;
	for (kk=1;kk<=casen;kk++)
	{
		cin>>n>>m>>a;
		cout<<"Case #"<<kk<<": ";
		if (a>n*m) cout<<"IMPOSSIBLE"<<endl;
		else
		{
			v=true;
			for (x1=0;x1<=n && v==true;x1++)
				for (y1=0;y1<=m && v==true;y1++)
					for (x2=0;x2<=n && v==true;x2++)
						for (y2=0;y2<=n && v==true;y2++) if (abs(x1*y2-x2*y1)==a)
						{
							v=false;
							cout<<"0 0 "<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<endl;
						}
			if (v==true) cout<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}



