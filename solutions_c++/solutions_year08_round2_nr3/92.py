#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <deque>
#include <memory.h>
using namespace std;
typedef long long lint;
void shift(deque<int> & a, int n){
	reverse(a.begin(),a.begin()+n);
	reverse(a.begin()+n,a.end());
	reverse(a.begin(),a.end());
}
int main(){
	ifstream in("C-small-attempt0.in");
	ofstream out("output.txt");
	int N;
	in >> N;
	for(int t = 0; t<N; ++t){
		int K, n;
		in >>K >> n;
		vector<int> b(n);
		for(int i = 0; i< n; ++i){
			in >> b[i];
			--b[i];
		}
		vector<int> a(K);
		for(int i = 0; i< K; ++i)
			a[i] = i;
		deque<int> ans;

		ans.push_back(a.back());
		a.pop_back();

		while (!a.empty()){
			int v = a.back();
			a.pop_back();
			int k = ans.size()+1-(v%(ans.size()+1));
			ans.push_front(v);
			shift(ans,k);
		}


		out<<"Case #"<<t+1<<": ";
		for(int i = 0; i< b.size(); ++i)
			out<< ans[b[i]]+1<< " ";
		out<<endl;
	}
	return 0;
}