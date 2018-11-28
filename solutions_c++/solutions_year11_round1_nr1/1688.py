#include<iostream>
#include<map>
#include<vector>
#include<sstream>
#include<fstream>
#define fori(a,b,c) for(int a=b; a<c; a++)
using namespace std;

typedef map<int, vector<string> > dict;

int gcd(int a, int b){
	if(b==0) return a;
	return gcd(b, a%b);
}

int lcm(int a, int b){
	return (a*b)/gcd(a, b);
}

bool solve(int a, int b, int c){
	if(c==100) return b==100;
	if(c==0) return b==0;
	if(b==0) return true;
	return (100/gcd(100,b))<=a;
}

int main(int argc, char *argv[]){
//	cout.setf(ios::fixed,ios::floatfield);
//	cout.precision(6);
	int t;
//	istream& in = cin;ostream&out=cout;
	fstream fin(argv[1]);istream& in=fin;fstream fout("a.out");ostream&out = fout;
//	istringstream in("3 1 100 50 10 10 100 9 80 56");ostream&out=cout;
	in>>t;
	fori(i,0,t){
		int a,b,c;
		in>>a>>b>>c;
			
		out<<"Case #"<<(i+1)<<": ";
		out<<(solve(a,b,c)?"Possible":"Broken");
		
		out<<endl;
	}
	system("PAUSE >void.out");
	return 0;
}
