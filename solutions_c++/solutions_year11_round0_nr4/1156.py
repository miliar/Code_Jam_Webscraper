#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;
int main(){
	ifstream cin("D-large.in");
	ofstream cout("D-large.out");
	int t;
	int i,j;
	int n;
	double count;
	int Array[1008];
	cin >> t;
	
	for(i=1;i<=t;i++){
		count=0;
		cin >> n;
		for(j=1;j<=n;j++){
			cin >> Array[j];
			if(Array[j]!=j){
				count++;
			}
		}
		cout << "Case #"<< i << ": "<<  setprecision(6) << fixed << count << endl;
	}
	return 0;
}