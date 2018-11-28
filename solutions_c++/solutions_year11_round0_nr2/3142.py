#include <iostream>
using namespace std;
#include <vector>

int comb[26][26];
bool bomb[26][26];

int main(){
	int n;
	cin >> n;

	for(int ni = 0 ; ni < n ; ni++){
		memset( comb, -1, sizeof(comb) );
		memset( bomb, 0, sizeof(bomb) );
		int m1,m2,m3;
		cin >> m1;
		for(int i = 0 ; i < m1; i++){
			string str;
			cin >> str;
			comb[ str[0]-'A' ][ str[1]-'A'] = str[2]-'A';
			comb[ str[1]-'A' ][ str[0]-'A'] = str[2]-'A';
		}
		cin >> m2;
		for(int i = 0 ; i < m2; i++){
			string str;
			cin >> str;
			bomb[ str[0]-'A' ][ str[1]-'A'] = true;
			bomb[ str[1]-'A' ][ str[0]-'A'] = true;
		}
		cin >> m3;
		string input;
		if( m3 > 0 ) cin >> input;
		else{
			cout << "Case #"<< ni+1 <<": []\n";
			continue;
		}

		vector<int> s;
		s.clear();
		s.push_back(input[0]-'A');

		for(int i = 1; i < m3; i++){
			int now = input[i]-'A';
			if( !s.empty()){
				int prev = s.back();
				while( comb[prev][now] > 0 ){
					now = comb[prev][now];
					s.pop_back();
					if( s.empty() ) break;
					prev = s.back();
				}
			}
			s.push_back(now);
			for(int j = 0; j < s.size()-1; j++)
				if( bomb[s[j]][now] )
				{
					s.clear();
					break;
				}
		}

		if( s.empty() ){
			cout << "Case #"<< ni+1 <<": []\n";
			continue;
		}
		cout << "Case #"<< ni+1 <<": [";

		for(int i = 0; i < s.size()-1; i++)
			cout << (char)(s[i]+'A') << ", ";
		cout << (char)(s[s.size()-1]+'A');

		cout << "]\n";
	}
}

