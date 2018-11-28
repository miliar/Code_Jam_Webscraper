#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
	int n, s, q;
	int rst;
	int j;

	string in;

	set <string> ori;
	set <string> dat;

	getline(cin, in);

	n = atoi(in.c_str());

	for(int i=1;i <= n; ++i)
	{
		ori.clear();
		dat.clear();
		rst = 0;

		getline(cin, in);

		s = atoi(in.c_str());

		for(j=0 ; j <s; ++j)
		{
			getline(cin, in);
			ori.insert(in);
		}

		getline(cin, in);

		q = atoi(in.c_str());

		for(j=0; j<q ; ++j)
		{
			getline(cin, in);
			dat.insert(in);

			if(dat.size() == ori.size())
			{
				dat.clear();
				dat.insert(in);
				rst++;
			}
		}

		cout << "Case #" << i << ": " << rst << endl;

	}

	return 0;
}
