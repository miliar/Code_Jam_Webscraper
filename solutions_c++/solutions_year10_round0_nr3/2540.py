#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("c.in");
//#define cin fin

int R,k,N;
int sum;
int group[1000];
void solve(){
    int x = 0, i, j;
    int boat, times;
    sum = 0;
    for(i=0;i<R;i++){
	boat = 0;
	times = 0;

	for(j=0;j<N;j++){
	    if(boat+group[x] > k)
		break;
	    boat+=group[x];
	    x = (x+1)%N;
	}
	/*
	if(x==0){//repeat
	    if(R/(i+1)*j > 0){
		boat = (R/j)*boat;
		i = (R/j)*(1+i);
	    }
	}
	*/
	sum+=boat;
    }
}

int main(){
    int C;
    cin>>C;
    int i, j;
    for(i = 0; i < C; i ++){
	cin>>R>>k>>N;
	for(j = 0; j < N; j ++){
	    cin>>group[j];
	}
	solve();
	cout<<"Case #"<<i+1<<": "<<sum<<endl;
    }
    return 0;
}
