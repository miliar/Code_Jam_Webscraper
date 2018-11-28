#include <iostream>
using namespace std;


int gcd(int a,int b)
{
	if(0 == b)
	{
		return a;
	}
	return gcd(b,a%b);
}
int main()
{
	freopen("F:\\code\\topcoder\\compete\\compete\\codejam_2011\\A-large.in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\codejam_2011\\result.txt","w",stdout);
	int caseNum = 0;
	int t;
	cin>>t;
	while(caseNum < t)
	{
		long long n;
		int d,g;
		cout << "Case #"<<caseNum + 1 << ": ";
		cin>>n>>d>>g;
		int dd;
		dd = gcd(100,d);
		dd = 100 /dd;
		if(n>=dd)
		{
			if(g == 100)
			{
				if(d == 100)
				{
					cout << "Possible";
				}
				else
				{
					cout << "Broken";
				}
			}else if(g == 0)
			{
				if(d == 0)
				{
					cout << "Possible";
				}
				else
				{
					cout << "Broken";
				}
			}
			else
			{
				cout << "Possible" ;
			}
		}
		else
		{
			cout << "Broken";
		}
		caseNum++;
		cout <<endl;
	}
}