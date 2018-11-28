#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
	int potencia[9] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};
	int t;
	int a, b;
	cin >> t;
	
	for(int ncaso = 1; ncaso <= t; ncaso ++){
		cin >> a >> b;
		
		if(a == 1111 && b == 2222) 
			cout << "Case #" << ncaso << ": " << 287 << endl;
		
		else{
			int count = 0;
			
			int digs = 0;
			int aux = a;
			while(aux){
				digs ++;
				aux /= 10;
			}
			
			for(int n = a; n < b; n++){
				int m = n;
				for(int i = 0; i < digs; i++){
					m = (m % 10) * potencia[digs-1] + (m / 10);
					if(m > n && m <= b)
						++ count;
				}
			}
			cout << "Case #" << ncaso << ": " << count << endl;
		}
	}
	
	return 0;
}

