#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);	
	int ntest;
	cin >> ntest;

	for (int test = 1;test <= ntest; ++test){
		string s;
		cin >> s;
		bool ok = true;
		for (int i = 1;i < s.size(); ++i)
			if (s[i-1] < s[i]){
				ok = false;
				break;
			}
		printf("Case #%i: ",test);

		if (ok){
			s += "0";
			sort(s.begin(),s.end());
			
			//reverse(s.begin(),s.end());
			if (s[0] == '0'){
				int t = -1;
				for (int i = 1;i < s.size(); ++i)
					if (s[i] != '0'){
						t = i;
						break;
					}
				swap(s[t],s[0]);
				
			}
			cout << s << endl;
		}
		else{
			string best = "a";

			for (int i = 0;i < s.size()-1; ++i){
				
				for (int j = i+1;j < s.size(); ++j)
					if (s[j] > s[i]){
						string cur = s;
						swap(cur[j],cur[i]);
						sort(cur.begin()+i+1,cur.end());
						if (cur < best)
							best = cur;
					}
			}
			cout << best << endl;
		}
	}
	
	return 0;
}