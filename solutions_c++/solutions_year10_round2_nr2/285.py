#include<algorithm>
#include<cmath>
#include<iomanip>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(){
	ifstream entrada("B-large.in");
    ofstream salida("B-large.out");
    int c;
    entrada >> c;
    int res;
    int n;
    int k;
    int b;
    int t;
    bool posible;
    for(int i=1;i<=c;++i){
		res = 0;
		posible = false;
		entrada >> n >> k >> b >> t;
		int pos[n];
		int vel[n];
		for(int j=0;j<n;++j){
			entrada >> pos[j];
		}
		for(int j=0;j<n;++j){
			entrada >> vel[j];
		}
		bool llega[n];
		for(int j=0;j<n;++j){
			double aux = (double) (b-pos[j]);
			aux = aux/(double)vel[j];
			if(aux <= (double) t){
				llega[j] = true;
			} else{
				llega[j] = false;
			}
		}
	
		vector<int> llegan;
		for(int j=n-1;j>=0;--j){
			if(llega[j]){
				llegan.push_back(j);
			}
		}
		
		if(llegan.size() >= k){
			posible = true;
		}
		if(posible){
			for(int j=0;j<k;++j){
				res += (n-1-j)-llegan[j];
			}
		}
	
	
		if(posible){
			salida << "Case #" << i << ": " << res << endl;
		} else{
			salida << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
	}
}
