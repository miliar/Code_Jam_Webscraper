#include <iostream>

using namespace std;

int main() {
	int t, x = 0, n, s, p, ans;
	cin >> t;
	while(t--) { x++;
	ans  = 0;
	cin >> n >> s >> p; 
	int a = 0, a1 = 1;
	for(int i = 0; i < n; i++) {
		cin >> a;
		int b = (a/3);
		int c = b*3;
		int d = (b+1)*3;
		int e = 0;
		 if(b >= p) { ans++; e = 1;}
		if(e == 0) { if((c+1) == a && (b+1) >= p) { ans++; e = 1;}
			else if((c+2) == a && (b+1) >= p){ans++; e = 1;}
		}
		if(e == 0 && a1 <= s) {
			if(c > 0 && (c) == a && (b+1) >= p) { ans++; a1++;}
			else if((c+1) == a && (b+1) >= p) { ans++; a1++;}
			else if((c+2) == a && (b+2) >= p) { ans++; a1++;}
		}
	}
	cout << "Case #" << x <<": " << ans << endl;
	}
	return 0;
}
		
		
		
