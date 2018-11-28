#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <sstream>
#include <map>

using namespace std;


int main(){
	FILE *f;
	int ncase;
	f = fopen("case.txt", "r");
	
	fscanf(f, "%d", &ncase);
	
	for(int i=0;i<ncase;i++){
		int n, k;
		fscanf(f, "%d %d", &n, &k);
		vector <int> vec;
		
		cout << "Case #" << i+1 << ": ";
		if((k+1)%(int)pow((double)2,(double)n)==0){
			cout << "ON";
		}else{
			cout << "OFF";
		}
		cout << endl;
	}
	
	fclose(f);
	return 0;
}

