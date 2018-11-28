#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

unsigned int gcd(unsigned int a, unsigned int b){
	if(a == 0){
		return b;
	} else if(b == 0){
		return a;
	}

	if(a>=b){
		return gcd(b, a%b);
	} else{
		return gcd(a, b%a);
	}
}

static void doWork(ifstream &in, ofstream &out, int caseNo){
	unsigned long long n;
	unsigned int pd, pg;
	in >> n >> pd >> pg;
	if((pg == 100 && pd != 100) ||
	   (pg == 0 && pd != 0)){
		out << "Case #" << caseNo << ": Broken" << endl;
	} else{
		unsigned int theGcd = gcd(100, pd);
		unsigned int den = 100/theGcd;
		if(n>=den){
			out << "Case #" << caseNo << ": Possible" << endl;
		} else{
			out << "Case #" << caseNo << ": Broken" << endl;
		}
	}
}



int main(){
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int tc;
	in >> tc;
	for(int i=1; i<=tc; i++){
		doWork(in, out, i);
	}
	in.close();
	out.close();
	return 0;
}
