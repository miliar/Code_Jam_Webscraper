#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <queue>
using namespace std;
ifstream in ("input.in");
ofstream out ("output.out");
int main() {
	int T;
	in >> T;
	for (int z=0; z<T; z++) {
		int N, M;
		in >> N >> M;
		vector <string> lev[100];
		for (int i=0; i<N; i++) {
			string s;
			in >> s;
			int cnt=0, j=0;
			while (j<s.size()) {
				if (s[j]=='/') {
					cnt++;
					string tmp;
					int k;
					for (k=j+1; (k<s.size()) && (s[k]!='/'); k++);
					j=k;
					tmp = s.substr (0, j);
					bool flag=true;
					for (int k=0; k<lev[cnt].size(); k++)
						if (lev[cnt][k]==tmp) {
							flag=false;
							break;
						}
					if (flag) lev[cnt].push_back (tmp);
				}
				else j++;
			}
		}
		/*for (int i=0; i<5; i++) {
			for (int j=0; j<lev[i].size(); j++)
				out << lev[i][j] << " ";
			out << "\n";
		}*/
		int ans=0;
		for (int i=0; i<M; i++) {
			string s;
			in >> s;
			int cnt=0, j=0;
			while (j<s.size()) {
				if (s[j]=='/') {
					cnt++;
					string tmp;
					int k;
					for (k=j+1; (k<s.size()) && (s[k]!='/'); k++);
					j=k;
					tmp = s.substr (0, j);
					for (k=0; k<lev[cnt].size(); k++)
						if (lev[cnt][k]==tmp) break;
					if (k==lev[cnt].size()) {
						int work = 0;
						for (int h=0; h<s.size(); h++)
							if (s[h]=='/') work++;
						ans += work-cnt+1;
						/////////////////////
						int cnt=0, j=0;
			while (j<s.size()) {
				if (s[j]=='/') {
					cnt++;
					string tmp;
					int k;
					for (k=j+1; (k<s.size()) && (s[k]!='/'); k++);
					j=k;
					tmp = s.substr (0, j);
					bool flag=true;
					for (int k=0; k<lev[cnt].size(); k++)
						if (lev[cnt][k]==tmp) {
							flag=false;
							break;
						}
					if (flag) lev[cnt].push_back (tmp);
				}
				else j++;
			}
		
						/////////////////////
						break;
					}
				}
				else j++;
			}
		}
		out << "Case #" << z+1 << ": " << ans << "\n";
	}
	return 0;
}