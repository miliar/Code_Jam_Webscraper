#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>

using namespace std;

int main(){
	int T, N;
	cin>>T;
	for(int i=0; i<T; i++){
		cin>>N;
		vector<int> rpos(2, 1);
		vector<int> rtime(2,0);
		int curt=0;
		int rob=0;
		int res=0;
		char hall;
		int to;
		for(int j=0; j<N; j++){
			cin>>hall>>to;
			if(hall=='O'){ rob=0;} else {rob=1;}
			rtime[rob]+= abs(to-rpos[rob])+1;
			rpos[rob] = to;
			curt++;
			if(curt<rtime[rob])curt=rtime[rob]; else rtime[rob]=curt;
		}
		res=curt;
		cout<<"Case #"<<i+1<<": " <<res<<"\n";
	}
	
}
