#include <iostream>
using namespace std;
int n,i,j,a1,a2,b1,b2,sum,cases,ncase;

int gcd(int x, int y)
{
	if (y==0)
		return 1;
	if (x>=2*y)
		return 1;
	else
		return 1-gcd(y,x%y);
}
int main()
{
	freopen("C-small-attempt0.in.txt","r",stdin);
	freopen("C-small-attempt0.out.txt","w",stdout);
	cin >> cases;
	for (ncase=1; ncase<=cases; ncase++)
	{
		cin >> a1 >> a2;
		cin >> b1 >> b2;
		sum = 0;
		for (i=a1; i<=a2; i++)
			for (j=b1; j<=b2; j++)
				if (i<j)
					sum+=gcd(j,i);
				else
					sum+=gcd(i,j);
		cout << "Case #" << ncase << ": " << sum << endl;
	}
	return 0;
}