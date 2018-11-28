#include <string>
#include <fstream>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;

const int INF = 2000;

ifstream fin("A.in");
ofstream fout("A.out");

int main()
{
int CTEST;
fin >> CTEST;
for (int test=0; test<CTEST; test++) {
	int S;
	fin >> S;
	vector<string> s;
		char buf[104];
		fin.getline(buf,101);
	for (int i=0; i<S; i++) {
		string eng;
		char buf[104];
		fin.getline(buf,101);
		s.push_back(string(buf));
	}
	
	int Q;
	fin >> Q;
	vector<string> q;
		fin.getline(buf,101);
	for (int i=0; i<Q; i++) {
		string query;
		char buf[104];
		fin.getline(buf,101);
		string newQ = string(buf);
		if (q.size()==0
			||q[q.size()-1] != newQ)
				q.push_back(newQ);
	}
	
	if (q.size() <= 1) {
		fout << "Case #" << test+1 << ": " << 0 << endl;
		continue;
	}
	vector<vector<int> > count(S,vector<int>(q.size(),0));
	for (int i=0; i<s.size(); i++)
		if (q[0]==s[i])
			count[i][0] = INF;
	for (int j=1; j<q.size(); j++)
		for (int i=0; i<s.size(); i++) {
			if (q[j]==s[i]) {
				count[i][j] = INF;
				continue;	
			}
			int minCur = count[i][j-1];
			for (int k=0; k<s.size(); k++)
				if (k!=i && count[k][j-1]+1 < minCur)
					minCur = count[k][j-1]+1;
			count[i][j] = minCur;
		}
	int minCount = INF;
	for (int i=0; i<S; i++)
		minCount = min(minCount, count[i][q.size()-1]);
	fout << "Case #" << test+1 << ": " << minCount << endl;
}
return 0;
}