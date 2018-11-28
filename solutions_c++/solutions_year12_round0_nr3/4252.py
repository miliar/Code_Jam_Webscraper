#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>

using namespace std;

bool is_recycled(int a, int b){
	stringstream u,v;
	u << a;
	v << b;
	string x = u.str();
	string y = v.str();
	if (x.length() != y.length())
		return false;
	int n = x.length();
	for(int i=1;i<n;i++){
		if(y.substr(i,n-i)+y.substr(0,i) == x)
			return true;
	}
	return false;
}

int main(){
	int T;
	cin >> T;
	cin.ignore();
	for(int i=1;i<=T;i++){
		stringstream ss;
		string s; int count=0;
		int a,b;
		cin >> skipws >> a >> b;
		for(int n=a;n<b;n++)
			for(int m=n+1;m<=b;m++)
				if(is_recycled(n,m))
					count++;
		ss << "Case #" << i << ": " << count;
		s=ss.str();
		cout << s << endl;
	}
	return 0;
}
