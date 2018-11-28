#include <set>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{

	int c;
	cin  >> c;
	string tmp;
	for(int i=0;i<c;i++){
		int m;
		cin >> m;
		vector<string> names(m);
		getline(cin, tmp);
		for(int j=0;j<m;j++){
			getline(cin, names[j]);
			// cout << names[j] << endl;
		}
		int t;
		cin >> t;
		getline(cin, tmp);

		// cout << m << " " << t << endl;
		set<string> s;
		int cnt = 0;
		for(int j=0;j<t;j++){

			string str;
			getline(cin, str);
			s.insert(str);
			// cout << j << " " << s.size() << endl;
			if( s.size() == m ){
				cnt++;
				s.clear();
				s.insert(str);
			}

		}

		cout << "Case #" << (i+1) << ": " << cnt << endl;
	}

}



		
