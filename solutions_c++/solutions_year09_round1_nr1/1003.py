#include <fstream>
#include <iostream>
#include <vector>
#include <set>
using namespace std;

ifstream IN("A-small-attempt1.in");
ofstream OUT("A-small-attempt1.out");


void print( vector<int> bases ){
	for (int i = 0; i < bases.size(); i++) cout << bases[i] << " ";
	cout << endl;
}


int producto( vector<int> v ){
	int p = 0;
	for (int i = 0; i < v.size(); i++) p += v[i]*v[i];
	return p;
}

vector<int> convert( int n, int b ){
	vector<int> num;
	while (n >= b){
		num.insert(num.begin(), n % b);
		n /= b;
	}
	num.insert(num.begin(), n);
	return num;
}

bool happy( int n, int b ){
	set<int> passed;
	vector<int> v = convert(n, b);
	int p;
	while ((p = producto(v)) && passed.find(p) == passed.end()){
		passed.insert(p);
		v = convert(p, b);
	}
	return p == 1;
}

bool allhappy( int n, vector<int> b ){
	for (int i = 0; i < b.size(); i++){
		if (!happy(n, b[i])) return false;
	}
	return true;
}

int main(){
	/*cout << producto(convert(91, 10)) << endl;
	system("pause");
	return 0;*/
	int T;
	IN >> T;
	IN.get();
	for (int t = 1; t <= T; t++){
		vector<int> bases;
		int b;
		do {
			IN >> b;
			bases.push_back(b);
		} while (!IN.eof() && IN.peek() != '\n');
		int n = 2;
		while (!allhappy(n++, bases)) cout << endl;
		cout << endl << endl;
		OUT << "Case #" << t << ": " << n-1 << endl;
	}
}
