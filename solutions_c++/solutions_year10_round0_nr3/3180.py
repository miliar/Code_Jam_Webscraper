#include <fstream>
#include <vector>
#include <iostream>
#include <cmath>
#include <queue>


using namespace std;
typedef vector<double> VD;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<vector<int> > MI;
typedef vector<vector<bool> > MB;

int main(){
	int k,r,n,t,cont,sum,res;
	cin >> t;
	for(int j=0;j<t;j++){
		cont=0;
		res=0;
		cin >> r;
		cin >> k;
		cin >> n;
		VI fila(n);
		for(int i=0;i<n;i++) cin >> fila[i];
		for(int i=0;i<r;i++){
			sum=0;
			for(int s=0;((sum+fila[cont])<=k)&&(s<n);s++){
					sum=sum+fila[cont];
					cont=(cont+1)%n;
				    
			}
			res=res+sum;
		}
		cout<< "Case #" << (j+1) << ": " << res << endl;
	}
		
}
		

	
	
