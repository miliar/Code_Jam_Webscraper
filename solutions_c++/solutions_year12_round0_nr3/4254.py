//ASSIGNMENT 313
#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<set>
#include<map>
#include<algorithm>
#include<cstring>
#include<iomanip>
#include<cmath>
#include<queue>

using namespace std;
bool checkRecycled(string n1, string n2);
string toString(int n);
int main(){
	int n;
	cin >> n;
	int n1, n2;
	string s1, s2;

	for(int cs=0; cs<n; cs++){
		int numRec = 0;
		
		cin >> n1 >> n2;
		
		for(int i=n1; i<=(n2-1); i++){
			for(int j=i+1; j<=n2; j++){
				if(checkRecycled(toString(i), toString(j))){
					numRec++;
				}
			}
		}
		
		cout << "Case #" << cs+1 << ": " << numRec << endl;
	}

	return 0;
}

bool checkRecycled(string n1, string n2){
	if(n1.size()!= n2.size()){
		return false;
	}

	n2+= n2;
	return n2.find(n1)!=string::npos;
}

string toString(int n){
	char s[8];
	itoa(n, s, 10);
	return string(s);
}