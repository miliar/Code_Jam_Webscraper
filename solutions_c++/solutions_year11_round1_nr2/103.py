#define _USE_MATH_DEFINES
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <list>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <numeric>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <stack>
#include <queue>
#include <ctime>
#include <NTL/ZZ.h>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
typedef complex <double> pt;

class GCJ {
public:
	vector <string> solve(int N, int M, vector <string> oD, vector <string> D[11], vector <int> Di[11], vector <string> L) {
		vector <string> res;

		int mask[10010][26];
		memset(mask, 0, sizeof(mask));
		for(int i=0; i<N; i++) {
			for(int j=0; j<(int)oD[i].size(); j++) {
				mask[i][oD[i][j]-'a']|=(1<<j);
			}
		}

		for(int li=0; li<M; li++) {
			vector <int> points(N);
			for(int i=1; i<=10; i++) {
				if(D[i].empty()) continue;
				if(D[i].size()==1) continue;
				set <vector <int> > group[2];
				vector <int> vi;
				for(int j=0; j<(int)D[i].size(); j++) vi.push_back(Di[i][j]);
				group[0].insert(vi);
				for(int j=0; j<(int)L[li].size(); j++) {
					set <vector <int> > &curgroup=group[j%2], &nextgroup=group[(j+1)%2];
					nextgroup.clear();
					if(curgroup.empty()) break;
					for(set <vector <int> >::iterator sti=curgroup.begin(); sti!=curgroup.end(); sti++) {
						vector <int> &curset=*sti;
						if(curset.size()==1) continue;
						map <int, vector <int> > tset;
						bool pointsplus=false;
						for(int k=0; k<(int)curset.size(); k++) {
							tset[mask[curset[k]][L[li][j]-'a']].push_back(curset[k]);
							if(mask[curset[k]][L[li][j]-'a']==0) points[curset[k]]++;
							else pointsplus=true;
						}
						for(map <int, vector <int> >::iterator mpi=tset.begin(); mpi!=tset.end(); mpi++) {
							if(mpi->second.size()>1) nextgroup.insert(mpi->second);
						}
						if(!pointsplus) {
							for(int k=0; k<(int)curset.size(); k++) {
								points[curset[k]]--;
							}
						}
					}
				}
			}
			int maxpoints=0, maxi=0;
			for(int i=0; i<N; i++) {
				if(maxpoints<points[i]) {
					maxpoints=points[i];
					maxi=i;
				}
			}
			res.push_back(oD[maxi]);
		}
		
		return res;
	}
};

int main() {
	string prb[12];
	ofstream ofs("output.txt");
	string s, filename;
	char key;
	int testcase;
	GCJ gcj;

	for(int i=0; i<12; i++) {
		prb[i].push_back('A'+i/2);
		if(i%2) prb[i]+="-large";
		else prb[i]+="-small-attempt";
		prb[i]+=".in.txt";
		cout << (char)('a'+i) << ". " << prb[i] << endl;
	}
	do {
		cout << "Choose the input file." << endl;
		cin >> key;
	} while(key-'a'<0 || key-'a'>=12);
	filename=prb[key-'a'];
	if((key-'a'+1)&1) {
		do {
			cout << "Choose number of attempt times." << endl;
			cin >> key;
		} while(key-'0'<0 || key-'9'>0);
		filename.insert(15, 1, key);
	}
	cout << "Filename is " << filename << endl;
	ifstream ifs(filename.c_str());

	clock_t start=clock();

	ifs >> testcase; ifs.ignore();
	for(int i=1; i<=testcase; i++) {
		int N, M;
		ifs >> N >> M;
		ifs.ignore();
		vector <string> oD;
		vector <string> D[11];
		vector <int> Di[11];
		for(int j=0; j<N; j++) {
			string s;
			getline(ifs, s);
			oD.push_back(s);
			D[s.size()].push_back(s);
			Di[s.size()].push_back(j);
		}
		vector <string> L(M);
		for(int j=0; j<M; j++) {
			getline(ifs, L[j]);
		}
		vector <string> w;
		w=gcj.solve(N, M, oD, D, Di, L);
		ofs << "Case #" << i << ":";
		for(int j=0; j<M; j++) {
			ofs << " " << w[j];
		}
		ofs << endl;
	}

	cout << (double)(clock()-start)/CLOCKS_PER_SEC << " sec" << endl;
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)