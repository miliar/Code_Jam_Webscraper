#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;



int main(){
	string p[] = {
"005",
"027",
"143",
"751",
"935",
"607",
"903",
"991",
"335",
"047",
"943",
"471",
"055",
"447",
"463",
"991",
"095",
"607",
"263",
"151",
"855",
"527",
"743",
"351",
"135",
"407",
"903",
"791",
"135",
"647"

	};

 	int N,k;
	cin >> N;
	
	for(int I = 0; I < N; I++){
		cin >> k;
		//cout<<p[I]<<endl;
		cout<<"Case #"<<I + 1<<": "<<p[k-1]<<"\n";
	}
	return 0;
}

