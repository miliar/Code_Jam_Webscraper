#include <iostream>
#include <string>
#include <set>
#include <fstream>
using namespace std;

string engine, query;
set<string> str, tmp;

int main()
{
    int N, S, Q, otest = 0;
    int i, j, k, cnt;
    ifstream in("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\a.in");
    ofstream out("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\a.out");
    in >> N;
    while(otest++ < N) {
		in >> S;
		getline(in, query);
		str.clear();
		for(i = 0; i < S; i++)  {
			getline(in, engine);
   			str.insert(engine);
		}
		in >> Q;
		getline(in, query);
		cnt = 0;
		tmp = str;
		for(i = 0; i < Q; i++)	{
			getline(in, query);
			if(tmp.count(query) > 0)   tmp.erase(query);
			if(tmp.empty()) {
				cnt++;
				tmp = str;
				tmp.erase(query);
			}
		}
		out << "Case #" << otest << ": " << cnt << endl;
	}
	return 0;
}
