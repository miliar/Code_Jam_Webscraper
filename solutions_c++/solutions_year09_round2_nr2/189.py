#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

const int inf = 0x3f3f3f3f;

#define Eo(x) {cerr << #x <<  " " << x << endl;}
string getnext(string q){
	string q1 = q;
	if (std::next_permutation(q1.begin(), q1.end()))
		return q1;
	else{
		q1 = "0" + q;
		std::next_permutation(q1.begin(), q1.end());
		return q1;
	}
}
int main(){
//	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ferlon;
	string n;
	scanf("%d",&ferlon);
	for ( int _ = 0; _ < ferlon; _++){
		cin >> n;
		cout << "Case #" << _ + 1 << ": " << getnext(n) << endl;
	}
	return 0;
}
