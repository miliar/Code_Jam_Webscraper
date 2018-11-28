#include <fstream>
#include <map>
#include <string>

using namespace std;

int main(){
	using namespace std;
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int t;
	fin >> t;
	for(int i = 0; i < t; i++){ 
		map<string, bool> A;
		char s[10] = {0,0,0,0,0,0,0,0,0,0};
		int a, b;
		fin >> a >> b;
		int cnt = 0;
		for(int j = a; j <= b; j++){
			itoa(j, s, 10);
			string s1 = "";
			for(int k = 0; k < 10; k++){
				if(s[k] == 0) break;
				s1 += s[k];
			}
			for(int k = 1; k < s1.size(); k++){
				string tmp1, tmp2;
				tmp1.assign(s1.begin(), s1.begin() + k);
				tmp2.assign(s1.begin() + k, s1.end());
				string tmp = tmp2 + tmp1;
				if(!A[tmp + s1] && s1 != tmp && tmp[0] != '0'){
					int res = atoi(tmp.c_str());
					if(res >= a && res <= b){		
						A[tmp + s1] = true;
						A[s1 + tmp] = true;
						cnt++;
					}
				}
			}
		}
		fout << "Case #" << i + 1 << ": " << cnt << endl;
	}
	return 0;
}