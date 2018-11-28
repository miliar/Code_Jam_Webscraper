#include <iostream>
#include <algorithm>

using namespace std;

const int MAXC = 1000000;

int main(){
    int t;
    cin >> t;
    
    for(int lp=1;lp<=t;++lp){
	int n;
	cin >> n;
	int xsum = 0;
	int sum = 0;
	int smallest = MAXC;
	
	for(int i=0;i<n;++i){
	    int candy;
	    cin >> candy;
	    xsum ^= candy;
	    sum += candy;
	    smallest = min(candy,smallest);
	}
	
	cout << "Case #" << lp << ": ";
	
	if(xsum == 0){
	    cout << sum - smallest << "\n";
	}
	else{
	    cout << "NO\n";
	}
    }
    return 0;
}