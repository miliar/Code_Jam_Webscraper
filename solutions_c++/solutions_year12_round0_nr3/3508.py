#include <iostream>
#include <fstream>
#include <hash_map>
using namespace std;

int leng(int src) {
	int flag = 0;
	while(src) {
		src /= 10;	
		flag++;
	}
	return flag;
}

int rotate(int src, int bit) {
	int rs = 0;
	int length = leng(src);
	int mul = 1;
	for(int i=0; i<bit; i++) mul*=10;
	int div = 1;
	for(int i=0; i<length-bit; i++) div*=10;
	rs = src/div + src%div*mul;
	return rs;
}

int main() {
	ifstream fin("./C-small-attempt0.in");
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
	int A,B;
	fin>>T;
	for(int cases = T; cases!=0; --cases) {
		fin>>A>>B;		
		int result = 0;
		int length = leng(A);
		for(int i=A; i<=B; i++){
			hash_map<int,int> m;
			for(int j=1; j<length; j++) {				
				int tmp = rotate(i,j);
				if(tmp>i && tmp<=B && m.insert(pair<int,int>(tmp,j)).second )
					result++;
			}
		}
		fout<<"Case #"<<T - cases + 1<<": "<<result<<endl;
	}
	return 0;
}