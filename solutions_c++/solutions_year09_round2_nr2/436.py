#include<cstdlib>
#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<cctype>
#include<algorithm>
using namespace std;

string Next(string N,vector<int> D)
{
	reverse(N.begin(),N.end());

	typedef map<pair<int,int>,int > m_t;
	m_t sorter;
	for(int from = 0;from < (int)N.size();++from){
		for(int to = from+1; to < (int)N.size(); ++to) {
			if(N[from] > N[to]){
				sorter[make_pair(to, int(N[from] - '0'))] = from;
			}
		}
	}

	if(sorter.empty()){
		char small = '9'+1;
		for(int k = 0;k < (int)N.size();++k)
			if(N[k] != '0' && N[k] < small){
				small = N[k];
			}

		ostringstream out;
		out << small;
		++D[0];
		--D[small - '0'];
		for(int k = 0;k <= 9;++k){
			for(int j = 0;j < D[k];++j)
				out << (char)('0' + k);
		}
		return out.str();
	}

	int to = sorter.begin()->first.first;
	int from = sorter.begin()->second;
	swap(N[to],N[from]);
	sort(N.begin(), N.begin()+to);
	reverse(N.begin(),N.begin()+to);
	reverse(N.begin(),N.end());
	return N;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 0;i < T;++i){
//		int N;
		string s;
		cin >> s;
//		N = atoi(s.c_str());
		vector<int> D(10,0);
		for(int k = 0;k < (int)s.size();++k)
			++D[s[k]-'0'];
		cout << "Case #" << i+1 << ": " << Next(s,D) << '\n';
		// string n = Next(s,D);
		// cerr << n << endl;
		// for(int k = 0;k < 20;++k){
		// 	n = Next(n,D);
		// 	cerr << n << endl;
		// }
	}
}
