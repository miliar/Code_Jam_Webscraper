#include <vector>
#include <string>
//#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <ctime>

using namespace std;

//ifstream cin("A-small-attempt0.in");
//ofstream cout("Asmall0.out");

ifstream cin("A-Large.in");
ofstream cout("A-Large.out");

int main(){
	int T;
	cin >> T;
	int N;
	for(int i=0;i<T;i++){
		cin >> N;
		vector <string>  grid;
		string s;
		for(int j=0;j<N;j++){
			cin >> s;
			grid.push_back(s);
		}
		
		vector <double > wp;
		wp.assign(N,0);
		
		for(int j=0;j<N;j++){
			double s1 = 0, s2 = 0;
			for(int k = 0;k<N;k++){
				if(grid[j][k] == '1') s1++;
				if(grid[j][k] == '0') s2++;
			}
			wp[j] = s1/(s1+s2);
		}
		vector <double> owp;
		owp.assign(N,0);
		for(int j=0;j<N;j++){
			double z = 0;
			double s1 = 0;
			for(int k=0;k<N;k++){
				if(grid[j][k]!='.'){
					z++;
					int t1 = count(grid[k].begin(),grid[k].end(),'.');
					double wz = (wp[k]*(N-t1) + (grid[j][k]-'0')-1)/(N-t1-1);
					s1+=wz;
					
				}
			}
			owp[j] = s1/z;
		}
		vector <double> oowp;
		oowp.assign(N,0);
		for(int j=0;j<N;j++){
			double z = 0;
			double s1 = 0;
			for(int k=0;k<N;k++){
				if(grid[j][k]!='.'){
					z++;					
					s1+=owp[k];					
				}
			}
			oowp[j] = s1/z;
		}
		vector <double> RPI;
		for(int j=0;j<N;j++){
			RPI.push_back(wp[j]*0.25 + owp[j]*0.5 + oowp[j]*0.25);
		}
		cout << "Case #" << i+1 << ":" << endl;
		for(int j=0;j<N;j++)
			cout <<fixed << setprecision(9) << RPI[j] << endl;
	
	}
	system("pause");
	return 0;

}