#include <fstream>
#include <vector>
#include <algorithm>

int main(){
	using namespace std;
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int t;
	fin >> t;
	for(int i = 0; i < t; i++){
		int n, s, p;
		fin >> n >> s >> p;
		vector<int> A(n);
		for(int j = 0; j < n; j++){
			int tmp;
			fin >> tmp;
			A[j] = tmp;
		}
		sort(A.begin(), A.end());
		int r = 3 * p - 2;
		int l = 3 * p - 4;
		int cnt = 0;
		if(p == 0){
			cnt = A.size();
			fout << "Case #" << i + 1 << ": " << cnt << endl;
			continue;
		}
		if(p == 1){
			for(int j = 0; j < A.size(); j++){
				cnt += A[j] > 0;
			}
			fout << "Case #" << i + 1 << ": " << cnt << endl;
			continue;
		}
		for(int i = 0; i < A.size(); i++){
			if(A[i] >= r){
				cnt++;
			}
			if(A[i] < r && A[i] >= l && s){
				cnt++;
				s--;
			}
		}
		fout << "Case #" << i + 1 << ": " << cnt << endl;
	}
	return 0;
}