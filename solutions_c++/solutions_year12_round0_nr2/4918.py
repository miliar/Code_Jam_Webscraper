#include <iostream>
#include <map>
#include <cstring>

using namespace std;

int abs(int x)
{
	return (x > 0) ? x : -x;
}
int main(){
	int t;
	cin >> t;
	
	for(int c = 0; c < t; c++){
		if(c>0)cout << endl;
		int n, s, p;
		cin >> n >> s >> p;
		
		int googlers = 0, tot;
		for(int i = 0; i < n; i++) {
			cin >> tot;
			
			if( (tot/3) >=	 p){
				googlers++;
				continue;
			}
			if(tot == 0 && p > 0)
				continue;
			
			int diff = abs((tot/3) - p),
					r = tot%3;
			if(diff <= 1 && diff <= r) {
				googlers++;
			} else if(diff == 1 && s-- > 0) {
				googlers++;
			} else if ( diff == 2 && (r==2) && s-- > 0) {
				googlers++;
			}
		}
		cout<< "Case #"<<c+1<<": " << googlers;
	}

}
