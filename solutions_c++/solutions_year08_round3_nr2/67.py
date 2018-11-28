# include <iostream>
# include <cstdio>
# include <cstdlib>
# include <algorithm>
# include <vector>
# include <string>
# include <cmath>

using namespace std;

long long LL[10000], A[4000000];


bool is(long long a){

	if(a==0) return true;
	int x[] = {2,3,5,7};

	for(int i = 0; i < 4; i++){
		while(a%x[i]==0) return true;
	}

	return false;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int TT;
	string inp;
	cin >> TT;
	
	getline(cin,inp);
	

	for(int tt = 1; tt <= TT; tt++){

		getline(cin,inp);
		int ans = 0;

		int D = pow(3.0, inp.length() - 1.0);
		int len = inp.length();
		for(int i = 0; i < D; i++){
			long long a = inp[0]-48;
			long long sum = 0;
			int last = 1;
			int d = i;

			for(int j = 1; j < len; j++){

				if(d % 3 == 0) a = 10 * a + (inp[j] - 48);
				if(d % 3 == 1 || d % 3 == 2){
					if(last == 1) sum += a;
					else sum -= a;

					last = d % 3;
					a = inp[j] - 48;
				}
				d /= 3;
			}

			if(last == 1) sum += a;
			else sum -= a;

			if(is(sum)) ans++;





		}

				cout << "Case #" << tt << ": " << ans << endl;	
	
		
	}

	


	return 0;
}