#include <iostream>
using namespace std;


const int MAX_N=50+10;
char table[MAX_N][MAX_N];
int n,m;


int main(){
	int tests;
	cin >> tests;
	for (int test=0;test<tests;test++){
		cin >> n >> m;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				cin >> table[i][j];
		bool imp=0;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++){
				if (table[i][j]=='#'){
					if (i==n-1 || j==m-1 || table[i][j+1]!='#' || table[i+1][j]!='#' || table[i+1][j+1]!='#'){
						imp=1; goto fix;
					}else {
						table[i][j]='/'; table[i][j+1]='\\';
						table[i+1][j]='\\'; table[i+1][j+1]='/';
					}

				}
				
			}
	fix:
		cout << "Case #" << test+1 << ":\n";
		if (imp)
			cout << "Impossible" << endl;
		else {
			for (int i=0;i<n;i++){
				for (int j=0;j<m;j++)
					cout << table[i][j];
				cout << endl;
			}
		}
		
	}


	return 0;
}