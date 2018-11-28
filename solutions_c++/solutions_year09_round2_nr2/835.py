#include <fstream>
#include <vector>
using namespace std;

ifstream IN("B-large.in");
ofstream OUT("B-large.out");

void print(vector<int> p){
	for (int i = 0; i < p.size(); i++){
		OUT << p[i];
	}
	OUT << endl;
}

bool last( vector<int> p ){
	for (int i = 1; i < p.size(); i++){
		if (p[i-1] < p[i]) return false;
	}
	return true;
}

int main(){
	int t, T, N;
	IN >> T;
	for (t = 1; t <= T; t++){
		IN.get();
		vector<int> p;
		while (!IN.eof() && IN.peek() != '\n'){
			char c = IN.get();
			if (c >= '0' && c <= '9')p.push_back(c-'0');
		}
		if (last(p)) p.insert(p.begin(), 0);
		next_permutation (p.begin(),p.end());
		OUT << "Case #" << t << ": ";
		print (p);
	}
}
