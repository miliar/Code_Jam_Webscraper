#include <iostream>
#include <string>
#include <set>

using namespace std;

string dict[5001];
set <char> patterns[501][16];

int main(){
	int l, d, n;
	cin>>l>>d>>n;
	for(int i = 0; i < d; i++)
		cin>>dict[i];

	for(int i = 0; i < n; i++){
		string p;
		cin>>p;

		int pos = 0, par = 0;
		for(int j = 0; j < p.size(); j++){
			if(p[j] == '(') par = 1;
			else if(p[j] == ')') {par = 0; pos++;}
			else {
				patterns[i][pos].insert(p[j]);
				if(!par) pos++;
			}
		}
	}

	for(int i = 0; i < n; i++){
		int nWords = 0;
		for(int j = 0; j < d; j++){
			int k = 0;
			for(k = 0; k < l; k++){
				/*cout<<dict[j][k]<<" pattern:";
				for( set<char>::const_iterator iter = patterns[i][k].begin(); iter != patterns[i][k].end();
				       ++iter ) {
				    cout << *iter << ' ';
				}
				cout<<endl;*/
				
				if(!patterns[i][k].count(dict[j][k])) break;
			}
			if(k == l) nWords++;
		}
		cout<<"Case #"<<i+1<<": "<<nWords<<endl;
	}
	return 0;
}
