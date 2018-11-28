#include <iostream>
#include <set>

using namespace std;

typedef pair<int, int> ipair;
typedef multiset<ipair> ipset;

typedef ipset::const_iterator _it;

void assign(_it depart, _it departend, _it arrive, _it arriveend, ipset& depart_set, ipset& arrive_set)
{
	_it temp = depart;
	depart++;
	
	int limit = temp->second;
	depart_set.erase(temp);
	
	for (; (arrive != arriveend) && (limit > arrive->first); arrive++) ;
	if (arrive != arriveend)
	{
		assign(arrive, arriveend, depart, departend, arrive_set, depart_set);
	}
}

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int t, na, nb;
		cin >> t >> na >> nb;
		
		ipset A, B;
		int An[100] = {0}, Bn[100] = {0};
		
		for (int nai = 0; nai < na; nai++)
		{
			int h1, h2, m1, m2;
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			A.insert( ipair(h1*60+m1, h2*60+m2 + t) );
		}
		for (int nbi = 0; nbi < nb; nbi++)
		{
			int h1, h2, m1, m2;
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			B.insert( ipair(h1*60+m1, h2*60+m2 + t) );
		}
		
		if (A.size() == 0 || B.size() == 0)
		{
			cout << "Case #" << i + 1 << ": " << A.size() << " " << B.size() << endl;
			continue;
		}
		
		int train = 1;
		int asol, bsol;
		asol = bsol = 0;
		// int aindex = 0, bindex = 0;
		ipset::const_iterator ait, aend = A.end(), bit, bend = B.end();
		while (A.size() > 0 && B.size() > 0)
		{
			ait = A.begin();
			bit = B.begin();
			
			if (ait->first < bit->first)
			{
				asol++;
				assign( ait, aend, bit, bend, A, B );
			}
			else
			{
				bsol++;
				assign( bit, bend, ait, aend, B, A );
			}
		}
		asol += A.size();
		bsol += B.size();
		cout << "Case #" << i + 1 << ": " << asol << " " << bsol << endl;
	}
	return 0;
}
