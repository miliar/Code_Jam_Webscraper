

#include <sstream>
#include <string>
#include <iostream>
using namespace std;

int Tri(int p){
	int rv = 1;
	for(int i=0;i<p;++i)
		rv*=3;
	return rv;
}

int main()
{
	int n;
	cin>>n;
	for(int t=1;t<=n;++t)
	{
		string xstr;
		cin>>xstr;
		int ans = 0;
		const int sz = xstr.size();
		for(int b=Tri(sz-1)-1;b>=0;--b)
		{
			long long sum = 0;
			long long nxd = xstr[0]-'0';
			int preOp = 1;//~+

			int opss = b;
			for(int dc=1;dc<sz;++dc)
			{
				int op = opss%3;
				if(0==op){
					nxd = nxd * 10 + (xstr[dc]-'0');
				}
				else if(1==op){
					if(1==preOp)
						sum += nxd;
					else
						sum -= nxd;
					preOp = op;
					nxd = xstr[dc]-'0';
				}
				else{
					if(1==preOp)
						sum += nxd;
					else
						sum -= nxd;
					preOp = op;
					nxd = xstr[dc]-'0';
				}
				opss/=3;
			}
			if(1==preOp)
				sum += nxd;
			else
				sum -= nxd;

			if( !sum ||
				0==sum%2 ||
				0==sum%3 ||
				0==sum%5 ||
				0==sum%7 )
				++ans;
		}

		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}
