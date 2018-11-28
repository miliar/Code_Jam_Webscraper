#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
	int num_inputs;
	cin >> num_inputs;

	for(int input=0;
		input<num_inputs;
		++input)
	{
		cout << "Case #" << input+1 << ": ";

		int ns, nq;
		cin >> ns;
		cin.ignore();

		map<string, int> se;
		for(int si=0; si<ns; ++si)
		{
			string line;
			getline(cin, line);
			se.insert(make_pair(line, 0));
		}

		cin >> nq;
		cin.ignore();

		vector<string> qu;
		for(int qi=0; qi<nq; ++qi)
		{
			string line;
			getline(cin, line);
			qu.push_back(line);
		}

		int switches=0;
		int currq=0;

		while(currq<nq) 
		{
			bool end = false;

			// calc distances
			map<string, int>::iterator bestdist = se.begin();
			for(map<string, int>::iterator it = se.begin();
				it != se.end();
				++it)
			{
				it->second = -1;
				
				for(int q=currq; q<nq; ++q)
					if(qu[q] == it->first) { it->second=q-currq; break; }

				if(it->second == -1){ end=true;	break; }

				if(it->second > bestdist->second)
					bestdist=it;
			}

			if(end) break;

			currq += bestdist->second;

			if(currq != nq) ++switches;
		}

		std::cout << switches << std::endl;

	}

	return 0;
}
