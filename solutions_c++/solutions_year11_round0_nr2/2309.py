#include <iostream>
#include <vector>
#include <map>
#include <stdlib.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t=1; t<=T; t++){
		int combN, opposN, N;
		vector<string> combine;
		vector<string> opposed;

		cin >> combN;
		for(int n=0; n<combN; n++){
			string str;
			cin >> str;
			combine.push_back(str);
			char s = str[0];  str[0] = str[1];  str[1] = s;
			combine.push_back(str);
		}
		combN *= 2;
		
		cin >> opposN;
		for(int n=0; n<opposN; n++){
			string str;
			cin >> str;
			opposed.push_back(str);
			char s = str[0];  str[0] = str[1];  str[1] = s;
			opposed.push_back(str);
		}
		opposN *= 2;
		
		string res, input;
		cin >> N;
		cin >> input;
		res += input[0];
		for(int n=1; n<N; n++){
			bool comb = false;
			int len = res.length();
			for(int i=0; i<combN; i++){
				if (input[n] == combine[i][0]  &&  res[len-1] == combine[i][1]){
					res[len-1] = combine[i][2];
					comb = true;
					break;
				}
			}
			if (!comb){
				res += input[n];
				for(int i=0; i<opposN; i++){
					if (input[n] == opposed[i][0]){
						int pos = res.find(opposed[i][1]);
						if (pos != string::npos){
							res.erase();
							break;
						}
					}
				}
			}
		}
	
		cout << "Case #" << t << ": [";
		int len = res.length();
		if (len > 0){
			cout << res[0];
			for(int i=1; i<len; i++)  cout << ", " << res[i];
		}
		cout << ']' << endl;
	}
	
	return 0;
}

