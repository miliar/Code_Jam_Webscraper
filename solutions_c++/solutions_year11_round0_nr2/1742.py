#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
#include<string>

using namespace std;

int main() {
	//ifstream cin("F:\\TDDOWNLOAD\\B-large.txt");
	//ofstream cout("F:\\TDDOWNLOAD\\out.txt");

	int t,Case,i,j;
	cin >> t;

	for ( Case = 1; Case <= t; Case++ ) {
		char comMark[26][26];
		int oppMark[26][26];

		for ( i = 0; i < 26; i++ ) {
			for ( j = 0; j < 26; j++ ) {
				comMark[i][j] = oppMark[i][j] = 0;
			}
		}

		int c;
		string comStr;
		cin >> c;
		for ( i = 0; i < c; i++ ) {
			cin >> comStr;
			comMark[comStr[0]-'A'][comStr[1]-'A'] =  comMark[comStr[1]-'A'][comStr[0]-'A'] = comStr[2];
		}

		int d;
		string oppStr;
		cin >> d;
		for ( i = 0; i < d; i++ ) {
			cin >> oppStr;
			oppMark[oppStr[0]-'A'][oppStr[1]-'A'] =  oppMark[oppStr[1]-'A'][oppStr[0]-'A'] = -1;
		}

		int n;
		string str;
		cin >> n;
		cin >> str;
		
		vector<int> ans;
		for ( i = 0; i < str.size(); i++ ) {
			if ( ans.empty() ) {
				ans.push_back ( str[i] );
			} else {
				if ( comMark[str[i]-'A'][ans[ans.size()-1] - 'A'] != 0 ) {
					ans[ans.size()-1] = comMark[str[i]-'A'][ans[ans.size()-1]-'A'];
				} else {
					bool flag = true;
					for ( j = 0; j < ans.size(); j++ ) {
						if ( -1 == oppMark[str[i]-'A'][ans[j]-'A'] ) {
							flag = false;
							break;
						}
					}

					if ( !flag ) {
						ans.clear();
					} else {
						ans.push_back( str[i] );
					}
				}
			}
		}

		cout << "Case #" << Case <<": ["; 

		for ( i = 0; i < ans.size(); i++ ) {
			if ( 0 == i ) {
				cout << (char)ans[i];
			} else {
				cout << ", " <<  (char)ans[i];
			}
		}

		cout << "]" << endl;
	}

	return 0;
}