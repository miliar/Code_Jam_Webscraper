#include<iostream>
#include<vector>

using namespace std;


bool check(char ch,string str)
{
	string s;
	s.push_back(ch);

	size_t nOffset = str.find (s, 0);

	    // Check if the substring was found...
	if (nOffset != string::npos) {
	        //cout << "found:" << nOffset;
		return true;
	} else {
	        return false;
		//cout << "not found." << endl;
	}
}
int main()
{
	int L,D,N;
	cin >> L >> D >> N;

	vector<string> list;
	vector< vector <string> > pattern(N);
	
	for(int i=0;i<D;i++) {
		string s;
		cin >> s;
		list.push_back(s);
	}

	for(int i=0;i<N;i++) {
		string s;
		cin >> s;
		pattern[i].push_back(s);

	}

/*	
	for(int i=0;i<D;i++) {
		cout << list[i] << endl;
	}
*/

	for(int i=0;i<N;i++) {
		string str = pattern[i][0];
		string substr;
		
		for(int j=0;j<str.size();) {
			if(str[j] == ')') {
				pattern[i].push_back(substr);
				substr.clear();
				j++;
				

			} else if(str[j] == '(') {
				while(str[++j] != ')'  ) {
					substr+=str[j];
				}
				
			} else {

				while(str[j] != '(' && j != str.size()) {
					substr+=str[j];
					pattern[i].push_back(substr);
					j++;
					substr.clear();
				}
			}
		}
	}
/*
	for(int i=0;i<D;i++) {
		string str=list[i];
		int count = 0;
		for(int j=0;j<N;j++) {
			//vector<string> v = pattern[j];
			
			for(int k=0;k<str.size() ;k++) {
				if(!check(str[k],pattern[j][k+1])) {
					break;
				}
				if(k==str.size()-1) count++;

			}
		
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
*/
	for(int i=0;i<N;i++) {
		vector<string> v = pattern[i];
		int count =0;
		for(int j=0;j<D;j++) {
			string str = list[j];
			for(int k=0;k<L;k++) {
				if(!check(str[k],v[k+1])) {
					break;
				}
				if(k==str.size()-1) count++;
			}

		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
/*	cout << " output" << endl;
	for(int i=0;i<N;i++) {
		for(int j=0;j<pattern[i].size();j++) {
			cout << pattern[i][j] << " " ;
		}
		cout << endl;
	}
	*/
	return 0;
}
