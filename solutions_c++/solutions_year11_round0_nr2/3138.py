#include <iostream>
using namespace std;
#include <vector>

char change[200][200];
bool clearPair[200][200];

int main(){
	int n;
	cin >> n;

	for(int ni = 1 ; ni <= n ; ni++){
		memset( change, -1, sizeof(change) );
		memset( clearPair, 0, sizeof(clearPair) );
		int m1,m2,m3;
		cin >> m1;
		for(int i = 0 ; i < m1; i++){
			string str;
			cin >> str;
			change[ str[0] ][ str[1]] = str[2];
			change[ str[1] ][ str[0]] = str[2];
		}
		cin >> m2;
		for(int i = 0 ; i < m2; i++){
			string str;
			cin >> str;
			clearPair[ str[0] ][ str[1]] = true;
			clearPair[ str[1] ][ str[0]] = true;
		}
		cin >> m3;
		string input;
		if( m3 > 0 ) cin >> input;
		else{
			cout << "Case #"<< ni <<": []\n";
			continue;
		}

		vector<int> s;
		s.clear();
		s.push_back(input[0]);

		for(int i = 1; i < m3; i++){
			int now = input[i];
			if( !s.empty()){
				int prev = s.back();
				while( change[prev][now] > 0 ){
					now = change[prev][now];
					s.pop_back();
					if( s.empty() ) break;
					prev = s.back();
				}
			}
			s.push_back(now);
			for(int j = 0; j < s.size()-1; j++)
				if( clearPair[s[j]][now] )
				{
					s.clear();
					break;
				}
		}

		if( s.empty() ){
			cout << "Case #"<< ni <<": []\n";
			continue;
		}
		cout << "Case #"<< ni <<": [";

		for(int i = 0; i < s.size()-1; i++)
			cout << (char)(s[i]+'A') << ", ";
		cout << (char)(s[s.size()-1]+'A');

		cout << "]\n";
	}
}

