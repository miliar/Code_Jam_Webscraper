#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <math.h>

#define max(x,y) (x>y?x:y)
#define min(x,y) (x>y?y:x)

using namespace std;


int main(){
	int i=0, n;
	int line = 1;
	cin >> n;
	while(++i<=n){
		double result = 0;
		int j=0;
		int tate, yoko;
		vector<string> table;
		cin >> tate >> yoko;
		while(++j<=tate){
			string sbuf;
			cin >> sbuf;
			table.push_back(sbuf);
		}
		bool impossible=false;
		for(int k=0;k<tate;k++){
			for(int l=0;l<yoko;l++){
				if(table[k][l]=='#'){//¶ã”­Œ©
					if(k==tate-1||l==yoko-1||table[k][l+1]!='#'||table[k+1][l+1]!='#'||table[k+1][l+1]!='#'){
						impossible=true;
						goto END;
					}else{
						table[k][l]='/';
						table[k+1][l]='\\';
						table[k][l+1]='\\';
						table[k+1][l+1]='/';
					}
				}
			}
		}
		
		//cout << "line:" << line << endl;
		END:
		cout << "Case #" << i << ":"<<endl;
		if(impossible){
			cout << "Impossible" << endl;
		}else{
			for(int k=0;k<tate;k++){
				for(int l=0;l<yoko;l++){
					cout << table[k][l];
				}
				cout << endl;
			}
		}
	}
	return 0;
}