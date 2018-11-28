#include<iostream>
#include<algorithm>
#include<iomanip>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<vector>
using namespace std;
struct _cmp{
	bool operator()(const int a, const int b)const{ return a > b; }
};
struct _cmp2{
	bool operator()(const int a, const int b)const{ return a < b; }
};

int main(){
	int N, P, K, L, f, s;
	long long total ;
	vector<int> padSize;
	vector<int> fre;
	cin >> N;
	for(int i = 0 ; i < N ; i++){
		padSize.clear();
		fre.clear();
		total = 0;
		cin >> P >> K >> L;
		for(int j = 0 ; j < L ; j++){
			cin >> f;
			fre.push_back(f);
		}
		for(int j = 0 ; j < K ; j++)
			padSize.push_back(0);
		sort(fre.begin(), fre.end(), _cmp() );
		for(int j = 0 ; j < fre.size() ; j++){
			s = padSize.front();
			//pop_heap( padSize.begin(), padSize.end() );
			//padSize.pop_back();
			padSize.erase( padSize.begin() );
			total +=  fre[j] * (s+1);
			if(s < P-1){
				padSize.push_back(s+1);
				sort(padSize.begin(), padSize.end(), less<int>());
				//push_heap( padSize.begin(), padSize.end(), greater<int>() );
			}

		}
		cout << "Case #" << i+1 << ": " << total << endl;
	}
}
