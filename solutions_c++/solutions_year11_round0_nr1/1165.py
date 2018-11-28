#include <iostream>
#include <fstream>
using namespace std;
int main(){
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	int Pi[109];
	char Ci[109];
	int cases,k;
	int lastO,lastB,current;
	int currentO,currentB;
	int i,j;
	cin >> cases;
	for(i=1;i<=cases;i++){
		cin >> k;
		lastO=1;
		lastB=1;
		current=0;
		currentO=0;
		currentB=0;
		for(j=0;j<k;j++){
			cin >> Ci[j] >> Pi[j];
		}
		for(j=0;j<k;j++){
			if(Ci[j]=='O'){
				if(j>0 && Ci[j-1]!='O'){
					currentO=((abs(Pi[j]-lastO)+1)>(currentB-currentO))?(currentO+(abs(Pi[j]-lastO)+1)):(currentB+1);
				}else{
					currentO+=(abs(Pi[j]-lastO)+1);
				}
				lastO=Pi[j];
			}else{
				if(j>0 && Ci[j-1]!='B'){
					currentB=((abs(Pi[j]-lastB)+1)>(currentO-currentB))?(currentB+(abs(Pi[j]-lastB)+1)):(currentO+1);
				}else{
					currentB+=(abs(Pi[j]-lastB)+1);
				}
				lastB=Pi[j];
			}
		}
		cout << "Case #" << i << ": " << (currentO>currentB?currentO:currentB) << endl;
	}
	return 0;
}