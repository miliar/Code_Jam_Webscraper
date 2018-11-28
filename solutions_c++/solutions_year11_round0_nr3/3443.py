#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>
using namespace std;


template<class T> void print(int test_case,T answer){
	cout << "Case #" << test_case+1 << ": " << answer << endl;
}


int main(){
	int T,N;
	
	cin >> T;
	
	for(int i=0;i<T;++i){
		cin >> N;
		
		int _min = INT_MAX;
		
		int sum = 0,tmp,tmp2 = 0;
		for(int j=0;j<N;++j){
			cin >> tmp;
			_min = min( _min,tmp );
			sum += tmp;
			tmp2 ^= tmp;
		}
		if( tmp2 != 0 ){
			print( i,"NO" );
			continue;
		}
		print(i,sum - _min);
	}
	return 0;
}
