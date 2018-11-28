#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <climits>
using namespace std;

int main(){
	int cases;
	cin >> cases;
	for(int i=0;i<cases;i++){
		
		int n, s, p, t;
		int ok, surprisable;
		int result;
		
		ok = 0;
		surprisable = 0;
		
		cin>>n;
		cin>>s;
		cin>>p;
		 
		for(int j=0;j<n;j++){
			cin>>t;
			if( t >= (p*3-2) ) { ok++;}
			else {
				if( t >= (3*p-4) && t>=p) {
					surprisable++;
				};
			}
		}
		result = ok + min(surprisable,s);
		
		cout << "Case #" << i+1 << ": " << result << endl;
		
	}
	return 0;
}