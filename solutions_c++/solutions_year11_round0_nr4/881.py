#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <fstream>
using namespace std;
/*
double nChoosep[1005][1005] = {0.0};
double invfcts[1005] = {1.0,1.0,0.5};
double prdrgs[1005] = {1.0,0.0,0.5,1.0/3.0};
double expc[1005] = {0.0,0.0,2.0};
*/

ifstream cin ("D-Large.in");
ofstream cout ("D-Large.out");
int main(){/*
	nChoosep[1][1] = 1;
	for(int j=1;j<1005;j++){
		nChoosep[j][0] = 1;
		nChoosep[j][1] = 1;
	}
	for(int i=2;i<1005;i++)
		for(int j=2;j<=i;j++)
			nChoosep[i][j] = nChoosep[i-1][j]+nChoosep[i-1][j-1];
	for(int i=3;i<1005;i++){
		prdrgs[i] = 1.0/i*(prdrgs[i-2] + double(i-1)*prdrgs[i-1]);		
	}
	for(int i=3;i<1005;i++)
		invfcts[i] = 1.0/(i)*invfcts[i-1];
	for(int i=3;i<1005;i++){
		double sum = 1.0;
		for(int j=1;j<=i;j++){
			sum+= invfcts[j]*prdrgs[i-j]*expc[i-j];
		}
		
		sum = sum/(1.0-prdrgs[i]);
		expc[i] = sum;
		//if(i<1000) cout << "E[" <<i << "] = " << expc[i] << endl;
	}*/
	int T;
	cin >> T;
	for (int i=0;i<T;i++){
		int N;
		cin >> N;		
		int z =0;
		for(int j=1;j<=N;j++){
			int x;
			cin >> x;
			if(x!=j) z++;			
		}
		cout <<"Case #" << i+1 <<": " << z << endl;
	}

	
	
	system("pause");
	return 0;
}