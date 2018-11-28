
#include <iostream>

using namespace std;


int reg(int t){
	if (t%3 == 0)
	    return t/3;
	return t/3+1;
}

int sur(int t){
	int n = t/3;
	if (t%3 == 2){
		if (n+2 > 10)
			return -1;
		return n+2;
	}
	if (n-1 < 0 || n+1 > 10)
		return -1;
	return n+1;
}



int main (){
	 
	 
	//cerr << "Hello Google" << endl;
	
	/* TEST:
	for (int k = 0; k <= 30; k++){		
		cout << k << "   " << reg(k) << "  " << sur(k) << endl;
	}
	*/
	
	int res;
	int T, N, S, p;
	// read no test cases
	cin >> T;	
	for (int i=1; i<= T ; i++){
		//read N, S and P
		res = 0;
		//cerr << "i=" << i << endl;
		cin >> N >> S >> p;	
		//cerr << N << " " << S << " " << p << endl;			
		//for every score		
		for (int k = 0; k<N; k++){
			int t;
			cin >> t;
			//cerr << t << "   " << reg(t) << "  " << sur(t) << endl;
			if (reg(t) >= p){
				res++;
				//cerr << "reg" << endl;
			}
			else{
				if (sur(t) >= p && S > 0){
					res++;
					S--;
					//cerr << "sur" << endl;
				}
			}
		}
		cout << "Case #" << i << ": " << res << endl;

	}//case T 
	

	return 0;
}
