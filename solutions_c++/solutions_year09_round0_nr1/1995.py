#include <iostream>
#include <string>
#include <vector>
#include <string.h>

using namespace std;

int main()
{
	long long int i, j, k;
	long long int j1, j2, cnt, cnt1, f;
	long long int N, D, L;
	cin >> L;
	cin >> D; 
	cin >> N;
	vector<string> v1, v2;
	string s;
	
	for(i = 0 ; i < D ; i++) {
		cin >> s;
		v1.push_back(s);
	}
	
	for( i = 0 ; i < N ; i++) {
		cin >> s;
		bool v3[30][30];
		memset(&v3, 0, 30*30);
		j1 = 0;
		for(k = 0; k < v1[0].size() ; k++){
			cnt = 0;
			if(s[j1] == '(') {
				for(j2 = j1+1 ; s[j2] != ')' && j2 < s.size() ; j2++) {
					v3[k][s[j2]-'a'] = true;
				}
				j1 = j2 + 1;
			} else {
				v3[k][s[j1]-'a'] = true;
					j1++;
			}
		}
		f = 0;
		for(j = 0 ; j < v1.size() ; j++){
			cnt = 0;
			for(j1 = 0 ; j1 < v1[j].size() ; j1++){
				if(v3[j1][v1[j][j1]-'a'])
					cnt++;
			}
			if(cnt == j1)
				f++;
		}
		cout << "Case #" << i+1 << ": " << f << endl;
	}	
	return 0;
}

