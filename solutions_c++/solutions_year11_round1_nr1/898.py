#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	long long N, pd,pg;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		cin >> N >> pd >> pg;
		long long D = 1;
		if((pd%2)) D = 4;
		else if(pd%4) D = 2;
		else D = 1;
		if(pd%5) D *= 25;
		else if (pd%25) D*=5;
		else D*=1;
		long long ct = D;
		long long cw = D*pd/100;
		D = 1;
		if((pg%2)) D = 4;
		else if(pg%4) D = 2;
		else D = 1;
		if(pg%5) D *= 25;
		else if (pg%25) D*=5;
		else D*=1;
		long long tt = D;
		long long tw = D*pg/100;
		bool wrong = false;
		if(pd != 100 && pg == 100) wrong = true;
		if(pd != 0 && pg == 0) wrong = true;
		if(ct > N) wrong = true;
		if(wrong)
		{
			cout << "Case #" << i << ": " << "Broken" << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << "Possible" << endl;
		}
	}
}
