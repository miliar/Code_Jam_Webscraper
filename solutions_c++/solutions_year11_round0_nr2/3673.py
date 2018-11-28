#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <vector>
using namespace std;

int main()
{
	string line;
	getline(cin, line);

	int T = atoi(line.c_str());
	for(int tcase=1; tcase <= T; ++tcase)
	{
		int has;
		string combine, com, rcom, opp, ropp;
		getline(cin, line);
		istringstream is(line);

		is >> has; if(has) is >> combine;
		is >> has; if(has) is >> opp;
		com = combine.substr(0,2);
		rcom = com; swap(rcom[0], rcom[1]);
		ropp = opp; swap(ropp[0], ropp[1]);

		int len;
		string elements;
		is >> len;
		is >> elements;

		string eset="";
		eset += elements[0];
		for(int i=1; i < len; ++i)
		{
			char e = elements[i];
			if(eset.empty())
			{
				eset+=e;
				continue;
			}
			string last2=""; last2+=eset[eset.size()-1]; last2+=e;
			if( last2 == com || last2 == rcom )
			{
				eset[ eset.size()-1 ] = combine[2];
				continue;
			}
			if( e == opp[0] || e == opp[1] )
			{
				char o = e==opp[0] ? opp[1] : opp[0];
				int begin = eset.find(o);
				if( begin != string::npos )
					eset = "";
				else
					eset += e;
				continue;
			}
			eset += e;
			
		}
		cout << "Case #" << tcase << ": [";
		for(int i=0; i<(int)eset.size()-1; ++i)
			cout << eset[i] << ", ";
		if(!eset.empty())
			cout << eset[eset.size()-1];
		cout << "]" << endl;
	}

	return 0;
}
