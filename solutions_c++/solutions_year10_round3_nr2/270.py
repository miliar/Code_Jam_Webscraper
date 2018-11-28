#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

long long out(long long cnt)
{
	long long temp=1;
	long long pow=0;
	while(temp<=cnt)
	{
		temp*=2;
		pow++;
		//cerr << "t";
	}
	return pow;
}

void iter(long long ind)
{
   	long long l,p,c;
	cin >> l >> p >> c;
	cerr << l << " " << p << " " << c << endl;

	long long cnt=0;
	long long temp=l;
	while(1)
	{
		temp = temp*c;
		if (temp<p) cnt++;
		else break;
		//if (temp==0) break;
		cerr << temp << " " << p << endl;
	}

	cout << "Case #" << ind << ": " << out(cnt) << endl;	
}

int main()
{
	long long t;
	cin >> t;

	for(long long i=0; i<t; ++i)
	{
		iter(i+1);
		cerr << t << " " << i << endl;
	}

	return 0;
}
