#include <iostream>
#include <vector>
using namespace std;

int main(){
	int n;
	cin >> n;
		
	for(int k=0; k<n; ++k){
		//cout << k + 1 << endl << endl;
		bool fin = true;
		bool win = false;
		vector<char> v(4,'Q');
		vector<char> h(4,'Q');
		vector<char> d(2,'Q');
		for(int i=0; i < 4; ++i){
			for(int j=0; j < 4; ++j){
				char a;
				cin >> a;
				if(a=='.') fin = false;
				if(i==0){
					v[j] = a;
					if(j==0) d[0] = a;
					if(j==3) d[1] = a;
				}
				else{
					if(v[j]!='N'){
						if(a!='T' && v[j]!=a) v[j]='N';
					}
					else if(v[j]=='T'){
						v[j] = a;
					}

					if(j==i){
						if(d[0]=='T') d[0] = a;
						if(a!='T' && d[0]!=a) d[0]='N';
						
					}
					if(j==(3-i)){
						if(d[1]=='T') d[1] = a;
						if(a!='T' && d[1]!=a) d[1]='N';
					}
				}
			
				if(j==0) h[i] = a;
				else{
					if(h[i]!='N'){
						if(a!='T' && h[i]!=a) h[i]='N';
					}
					else if(h[i]=='T'){
						h[i] = a;
					}
				}
			}
			if(h[i]=='X'){
				cout << "Case #" << k + 1 << ": X won" << endl;
				win = true;
			} 
			else if(h[i] == 'O'){
				cout << "Case #" << k + 1 << ": O won" << endl;
				win = true;
			}
		}

		for(int j=0; j < 4 and win == false; ++j){
			if(v[j]=='X'){
				cout << "Case #" << k + 1 << ": X won" << endl;
				win = true;
			} 
			else if(v[j] == 'O'){
				cout << "Case #" << k + 1 << ": O won" << endl;
				win = true;
			}
		}

		for(int j=0; j < 2 and win == false; ++j){
			if(d[j]=='X'){
				cout << "Case #" << k + 1 << ": X won" << endl;
				win = true;
			} 
			else if(d[j] == 'O'){
				cout << "Case #" << k + 1 << ": O won" << endl;
				win = true;
			}
		}

		if(win == false && fin == false) cout << "Case #" << k + 1 << ": Game has not completed" << endl;
		if(win == false && fin == true) cout << "Case #" << k + 1 << ": Draw" << endl;

		//for(int j = 0; j < 4; ++j) cout << v[j];
		//cout << endl;
		//for(int j = 0; j < 4; ++j) cout << h[j];
		//cout << endl;
		//for(int j = 0; j < 2; ++j) cout << d[j];
		//cout << endl;


	}
}
