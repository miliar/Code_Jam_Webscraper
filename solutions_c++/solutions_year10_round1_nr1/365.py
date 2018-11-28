#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> rotate(vector<string> vs){
	int n = vs.size();
	vector<string> res;
	for(int i=0;i<n;i++){
		string s;
		for(int j=n-1;j>=0;j--) s += vs[j][i];
		res.push_back(s);
	}
	return res;
}

vector<string> gravity(vector<string> vs){
	int n = vs.size();
	for(int i=0;i<n;i++){
		int bot = n-1;
		for(int j=n-1;j>=0;j--){
			if(vs[j][i] != '.'){
				swap(vs[j][i], vs[bot][i]);
				bot--;
			}
		}
	}
	return vs;
}

int check(vector<string> vs, int K){
	int n = vs.size();
	string red(K, 'R'), blue(K, 'B');
	for(int i=0;i<n;i++){
		string s;
		for(int j=0;j<n;j++) s += vs[j][i];
		vs.push_back(s);
	}
	for(int i=-n+1;i<n;i++){
		int x = i, y = 0;
		string s;
		while(x<0) x++, y++;
		while(0<=x&&x<n&&0<=y&&y<n){
			s += vs[y][x];
			x++, y++;
		}
		vs.push_back(s);
	}
	for(int i=0;i<2*n;i++){
		int x = i, y = 0;
		string s;
		while(x>=n) x--, y++;
		while(0<=x&&x<n&&0<=y&&y<n){
			s += vs[y][x];
			x--, y++;
		}
		vs.push_back(s);
	}
	int res = 0;
	for(int i=0;i<vs.size();i++){
		if(vs[i].find(red)!=string::npos) res |= 1;
		if(vs[i].find(blue)!=string::npos) res |= 2;
	}
	return res;
}

void print(vector<string> vs){
	int n = vs.size();
	for(int i=0;i<n;i++) cout << vs[i] << endl;
}

int main(){
	int TEST; cin >> TEST;
	string ans[4] = {"Neither", "Red", "Blue", "Both"};
	for(int test=1;test<=TEST;test++){
		int N, K; cin >> N >> K;
		vector<string> vs(N);
		for(int i=0;i<N;i++) cin >> vs[i];
//		print(gravity(rotate(vs)));
		int num = check(gravity(rotate(vs)), K);
		printf("Case #%d: %s\n", test, ans[num].c_str());
	}
}