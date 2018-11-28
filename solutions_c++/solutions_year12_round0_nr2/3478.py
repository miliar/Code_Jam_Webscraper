#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ifstream fin("./B-large.in");
	ofstream fout("./output.out");
	if(!fin) {
		cerr<<"文件input打开失败"<<endl;
		return -1;
	}
	if(!fout) {
		cerr<<"文件output打开失败"<<endl;
		return -1;
	}

	int T;
	int N, S, p;
	fin>>T;
	for(int i = T; i!=0; --i) {
		fin>>N>>S>>p;
		vector<int> v;
		int result = 0;
		for(int i = N, tmp; i != 0; --i) {
			fin>>tmp;
			v.push_back(tmp);
		}
		sort(v.begin(), v.end());
		vector<int>::reverse_iterator iter = v.rbegin();
		for(; iter != v.rend(); iter++) {
			if(*iter >= max(3*p-2,p) ) {
				result++;
				continue;
			}

			if(S!=0 && *iter>= max(3*p-4,p) ) {
				result++;
				S--;
			}
		}
		fout<<"Case #"<<T-i+1<<": "<<result<<endl;
	}
	return 0;
}