#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
	int t;
	cin >> t;
	
	for(int ncaso = 1; ncaso <= t; ncaso ++){
		int n, s, p;
		cin >> n >> s >> p;
		int t[n];
		for(int i = 0; i < n; i ++)
			cin >> t[i];
		
		if(p == 0)
			cout << "Case #" << ncaso << ": " << n << endl;
		
		else{
			int count = 0;
			for(int i = 0; i < n; i ++){
				if(p == 1){
					if(t[i] != 0)
						++ count;
				}
				else if((float)t[i] / 3 > p-1)
					++ count;
				else if(s && (t[i] == (p - 1) * 3 || t[i] == (p - 1) * 3 - 1)){
					++ count;
					s --;
				}
			}
				
			cout << "Case #" << ncaso << ": " << count << endl;
		}
	}
	
	return 0;
}

