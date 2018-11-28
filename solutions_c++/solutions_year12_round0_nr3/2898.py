#include<iostream>
#include<string>
#include<fstream>
#include<set>
#include<utility>
#include<cmath>

using namespace std;

bool answer(int a, int b){
	int digit = (int)log10(a);
	int temp = a;
	for(int i = 0; i < digit; i++){
		int r = temp%10;
		int q = temp/10;
		temp = r*pow(10.0,digit)+q;
		if(temp == b){
			//cout << "yes" << a << " " << b << endl;
			return true;
		}
	}
	//cout << "no " << a << " " << b << endl;
	return false;	
}

int main(){

	ifstream in_str("input.txt");
	ofstream out_str("output.txt");
	
	int numOfCases = 0;
	in_str >> numOfCases;
	for(int i = 0; i < numOfCases; i++){
		int a,b;
		set<pair<int,int> > result;
		in_str >> a >> b;
		for(int j = a; j <= b-1; j++){
			for(int k = j+1; k <= b; k++){
				if(answer(j,k))
					result.insert(make_pair(j,k));
			}
		}
		out_str << "Case #" << i+1 << ": " << result.size() << endl;
		
	}
	return 0;
}