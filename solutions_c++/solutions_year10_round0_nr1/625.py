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
	ifstream entrada("A-small.in");
    ofstream salida("A-small.out");
	int t;
	int n;
	int k;
	entrada >> t;
	for(int i=1;i<=t;++i){
		entrada >> n >> k;
		int aux = 1;
		for(int j=1;j<=n;++j){
			aux *= 2;
		}
		if(((k+1)%aux)==0){
			salida << "Case #" << i << ": " << "ON" << endl;
		} else{
			salida << "Case #" << i << ": " << "OFF" << endl;
		}
	}
}
