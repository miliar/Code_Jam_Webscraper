#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	cin >>n;
	for (int i=0; i<n; ++i){
		cout <<"Case #" <<i+1 <<": ";
		int t,s,p;
		cin >>t >>s >>p;
		vector <int> v(t),x(t),y(t),z(t),c(t);
		for (int j=0; j<t; ++j)
		{
			cin >>v[j];
			int ost=v[j]%3;
			x[j]=y[j]=z[j]=v[j]/3;
			if (ost>0)
				z[j]++;
			if (ost>1)
				++y[j];
			if (z[j]==y[j] && v[j]>1)
				c[j]=z[j]+1;
			else
				c[j]=z[j];
		}
		int count=0,rash=0;
		for (int j=0; j<t; ++j){
			if (z[j]>=p)
				++count;
			else
				if (c[j]==p && rash<s){
					++count;
					++rash;
				}
		}
		cout <<count <<endl;
	}
	return 0;
}