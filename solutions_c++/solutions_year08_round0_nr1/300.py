#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int N;
	
	char line[256];
	gets(line);
	N = atoi(line);
	for (int i=1; i<=N; ++i) {
		//cerr << "#" <<  i << endl;
		int S; 
		gets(line);
		S = atoi(line);
		vector <string> eng;
		vector <int> Qopt;
		for (int j=0; j<S; ++j) {
			
			gets(line);
			//cerr << "E=[" << line << "]" << endl;
			eng.push_back(line);
			Qopt.push_back(0);
		}
		//cerr << "#Q?" <<endl;
		int Q;
		gets(line);
		Q = atoi(line);
		for (int q=0; q<Q; ++q) {
			string qry;
			gets(line);
			qry = line;
			//cerr << "Q=[" << qry << "]" << endl;
			vector <int> Q2 = Qopt;
			for (int j=0; j<S; ++j) {
				if (eng[j] == qry)
					Q2[j] = 1000000;
				else {
					for (int k=0; k<S; ++k) 
						if (Qopt[k]+1 < Q2[j])
							 Q2[j] = Qopt[k]+1;
				}
			}
			Qopt = Q2;
		}
		int res = Qopt[0];
		for (int j=0; j<S; ++j) if (Qopt[j] < res) res = Qopt[j];
		cout << "Case #" << i << ": " << res << endl;
	}
}
