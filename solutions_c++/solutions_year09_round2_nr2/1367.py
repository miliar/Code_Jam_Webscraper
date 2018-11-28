#include<iostream>
#include<vector>
#include<set>
#include<string>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>
#include<limits>

using namespace std;

int main() {
	int T;
	cin>>T;
	int c=1;
	while(T--) {
		int N;
		cin>>N;
		stack<int> s;
		while(N) {
			s.push(N%10);
			N /= 10;
		}
		vector<int> v;
		while(!s.empty()) {
			v.push_back(s.top());
			s.pop();
		}
		if(next_permutation(v.begin(),v.end())==0) {
			int temp;
			for(int i=0;i<v.size();i++) {
				if(v[i]!=0) {
					temp = v[i];
					v[i] = 0;
					break;
				}
			}
			vector<int> v2;
			v2.push_back(temp);
			for(int i=0;i<v.size();i++) {
				v2.push_back(v[i]);
			}
			v = v2;
		}
		N = 0;
		for(int i=0;i<v.size();i++) {
			N = N*10 + v[i];
		}
		cout<<"Case #"<<c++<<": "<<N<<"\n";
	}
	return 0;
}
