#include <iostream>
using namespace std;

int l, p, c;

__int64 solve()
{
	__int64 k, x, res;
	k = 1;
	x = 0;
	while(l * k * c < p)
	{
		k *= c;
		x++;
	}
	k = 1;
	res = 0;
	while(k <= x)
	{
		k *= 2;
		res++;
	}
	return res;
}


int main()
{
	int i, case_num, t;
	cin>>t;
	for(case_num = 1; case_num <= t; case_num++)
	{
		cin>>l>>p>>c;	
		cout<<"Case #"<<case_num<<": "<<solve()<<endl;

	}
	return 0;
}