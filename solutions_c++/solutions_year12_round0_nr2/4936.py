#include <iostream>
#include <vector>
using namespace std;

int main(){
	int t;
	cin >> t;
	
	for (int i=0;i<t;++i){
		int n,s,p;
		cin >> n >> s >> p;
		
		vector<int> v(n, 0);
		
		int bons = 0;
		
		for (int j=0;j<n;++j){
			cin >> v[j];
			
			int actual = v[j];
			
			if ( (actual/3) >= p ){
				++bons;
			}
			else if ( ((actual/3) == p-1) && (actual%3) > 0 ){
				++bons;
			}
			else if ( ((actual/3) == p-1) && s > 0 && actual>=2 ){
				++bons;
				--s;
			} 
			else if ( ((actual/3) == p-2) && (actual%3) == 2 && s > 0 && actual >=2 ){
				++bons;
				--s;
			}
		}
		
		
		
		//Output
		cout << "Case #" << i+1 << ": " << bons << endl;
	}
	
}