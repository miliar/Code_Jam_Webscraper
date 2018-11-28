#include <iostream>

using namespace std;

int main(){
	int t,n;
	char ch;
	int npos;
	
	int opos;
	int bpos;
	
	int otime;
	int btime;
	
	cin >> t;
	
	for(int i = 0; i < t; i++){
		cin >> n;
		
		opos = 1;
		bpos = 1;
		
		otime = 0;
		btime = 0;
		for(int j = 0; j < n; j++){
			cin >> ch;
			cin >> npos;
			
			if(ch == 'O'){
				otime += ((opos>npos)?(opos-npos):(npos-opos)) + 1;
				opos = npos;
				if(otime<=btime) otime = btime + 1;
			}else{
				btime += ((bpos>npos)?(bpos-npos):(npos-bpos)) + 1;
				bpos = npos;
				if(btime<=otime) btime = otime + 1;
			}
		}
		
		cout << "Case #" << (i+1) << ": " << ((otime<btime)?btime:otime) << endl;
	}
	
	return 0;
}