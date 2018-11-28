#include<iostream>

using namespace std;


void print(int test_case,int answer){
	cout << "Case #" << test_case << ": " << answer << endl;
}


int main(){
	int T,N;
	
	cin >> T;
	
	for(int i=0;i<T;++i){
		cin >> N;
		int answer = 0;
		int pos[2] = {1,1};
		int hima[2] = {0,0};
		
		for(int j=0;j<N;++j){
			char ch;
			int bottom;
			cin >> ch >> bottom;
			
			//0:Blue 1:Orange
			int move = abs( bottom - pos[ch=='O'] ) - hima[ch=='O'];
			if( move < 0 ) move = 0;
			
			answer += move + 1;
			
			pos[ch=='O']  = bottom;
			hima[ch=='O'] = 0;
			hima[ch!='O'] += move + 1;
		}
		print( i+1,answer );
	}
	return 0;
}
