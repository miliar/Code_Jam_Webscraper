#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(){
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int N;
	in>>N;
	for(int t = 0; t<N; ++t){
		int S,Q;
		in >> S;
		vector<string> T(S);
		char buff[1000];
		in.getline(buff,200);
		for(int i = 0; i<S; ++i){
			in.getline(buff,200);
			T[i] = string(buff);
		}
		vector<int> A(S,0);
		in >> Q;
		in.getline(buff,200);
		for(int i = 0; i<Q; ++i){
			in.getline(buff,200);
			string V(buff);
			int c = int(find(T.begin(),T.end(),V)-T.begin());
			int l = (c<S) ? A[c] : 10000000;
			for(int j = 0; j<S; ++j)
				if (j == c){
					A[j] = 10000000;
				}
				else{
					A[j] = min(A[j],l+1);
				}
		}
		int res = *min_element(A.begin(),A.end());
		out<<"Case #"<<t+1<<": "<<res<<endl;
	}
	return 0;
}