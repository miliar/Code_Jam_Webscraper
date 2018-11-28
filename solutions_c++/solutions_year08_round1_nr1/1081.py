#include <iostream>
#include <list>

using std::cin;
using std::cout;
using std::endl;

using std::list;

int m_nInputs;

list<long> v1;
list<long> v2;

long CrossProduct()
{
	long ret = 0;
	list<long>::iterator jt = v2.begin();
	for (list<long>::iterator it = v1.begin(); it != v1.end(); ++it)
	{
		long a = *it;
		long b = *jt;
		ret += a * b;
		++jt;
	}
	return ret;
}

int main()
{
	cin >> m_nInputs;
	for (int i = 1; i <= m_nInputs; ++i)
	{
		v1.clear();
		v2.clear();
		int nScalars;
		cin >> nScalars;
		for (int j = 0; j < nScalars; ++j)
		{
			long a;
			cin >> a;
			v1.push_back(a);
			v1.sort();
		}
		for (int j = 0; j < nScalars; ++j)
		{
			long a;
			cin >> a;
			v2.push_back(a);
			v2.sort();
		}
		v2.reverse();
		cout << "Case #" << i << ": " << CrossProduct() << endl;
	}
	return 0;
}
