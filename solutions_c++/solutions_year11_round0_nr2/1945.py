#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){
	ifstream fin("B-large.in");
	ofstream fout("outputL.out");
	int t;
	fin >> t;
	for(int i = 0; i < t; i++){
		int c, d, n;
		int gr[30][30] = {0};
		char comb[30][30] = {0};
		fin >> c;
		string s;
		for(int i = 0; i < c; i++){
			fin >> s;
			comb[s[0] - 'A'][s[1] - 'A'] = s[2];
			comb[s[1] - 'A'][s[0] - 'A'] = s[2];
		}
		fin >> d;
		for(int i = 0; i < d; i++){
			fin >> s;
			gr[s[0] - 'A'][s[1] - 'A'] = 1;
			gr[s[1] - 'A'][s[0] - 'A'] = 1;
		}
		fin >> n >> s;
		int idx = 0;
		string ans = "";
		for(int i = 0; i < n; i++){
			if(!idx){
				ans += s[i];
				idx++;
			}
			else{
				int k = comb[ans[idx - 1] - 'A'][s[i] - 'A'];
				if(k > 0)
					ans[idx - 1] = k;
				else{
					ans += s[i];
					idx++;
					for(int j = 0; j < idx; j++)
						if(gr[ans[j] - 'A'][s[i] - 'A']){
							ans.clear();
							idx = 0;
						}
				}
			}
		}
		fout << "Case #" << i + 1 << ": [";
		for(int i = 0; i < ans.length(); i++){
			if(i)
				fout << ", ";
			fout << ans[i];
		}
		fout << "]" << endl;
	}
	return 0;
}