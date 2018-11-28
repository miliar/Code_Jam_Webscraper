#include "iostream"
#include "sstream"
#include "fstream"
#include "vector"
#include "algorithm"
#include "ios"
#include "math.h"
#include "limits"

using namespace std;

ifstream in("C-small-attempt0.in");
ofstream out("out.txt");

bool f(int a){
	for(int i = 2; i <= a/2; i++){
		if(a%i == 0)
			return false;
	}
	return true;
}

int main(){
	int N = 0;
	in >> N;
	for(int i = 0; i < N; i++){
		long result = 0;
		//long long A, B, P;
		//in >> A >> B >> P;

		//vector<bool> b;
		//b.resize(B-A+1, 0);
		////Process
		//for(long long i = P; i < B; i++){
		//	if(!f(i))
		//		continue;
		//	//i - простое
		//	int temp = i;
		//	if(temp < A)
		//		while((temp+=i) < A) {}
		//	if(temp > B)
		//		continue;
		//	result++;
		//	for(int j = temp; j <= B; j+=i){
		//		b.at(j-A) = true;
		//	}
		//}
		//for(int i = 0; i < b.size(); i++){
		//	result += !b.at(i);
		//}

		int K = 0;
		in >> K;
		int n = 0;
		in >> n;
		vector<int> ind;
		for(int k = 0; k < n; k++){
			ind.push_back(0);
			in >> ind[k];
		}

		//Process;
		vector<int> cards;
		cards.resize(K);
		cards[0] = 1;
		int pos = 0;
		for(int k = 2; k <= K; k++){
			for(int i = 0; i < k; i++){
				if (pos >= K-1) pos = -1;
				while(cards.at(++pos) != 0) { if (pos >= K-1) pos = -1; }
			}
			cards.at(pos) = k;
		}

		//Output
		out << "Case #" << i+1 << ":";
		for(int i = 0; i < n; i++){
			out << " " << cards.at(ind[i]-1);
		}
		out << endl;
	}
}