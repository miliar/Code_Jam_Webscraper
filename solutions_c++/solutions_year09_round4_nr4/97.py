#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

struct plant{
	double x, y, r;
};

double eval(){
	int N;
	cin>>N;
	vector<plant> plants(N);
	for(int i=0; i<N; i++){
		cin>>plants[i].x>>plants[i].y>>plants[i].r;
	}
	if(N==1)
		return plants[0].r;
	if(N==2)
		return max(plants[0].r, plants[1].r);
	if(N==3){
		return min(min(
			max((plants[0].r+plants[1].r+hypot(plants[0].x-plants[1].x, plants[0].y-plants[1].y))/2, plants[2].r),
			max((plants[1].r+plants[2].r+hypot(plants[1].x-plants[2].x, plants[1].y-plants[2].y))/2, plants[0].r)),
			max((plants[2].r+plants[0].r+hypot(plants[2].x-plants[0].x, plants[2].y-plants[0].y))/2, plants[1].r)
		);
	}
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		cout<<eval()<<endl;
	}
	return 0;
}
