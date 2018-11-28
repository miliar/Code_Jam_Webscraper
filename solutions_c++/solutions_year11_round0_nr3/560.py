#include <fstream>
#include <iostream>

using namespace std;

/*ifstream fin("GCJ P C.in");
ofstream fout("GCJ P C.out");

#define cin fin
#define cout fout*/

int t;
int n;
int sum;
int mi;
int r;

void process(){
	cin >> n;
	sum=0;
	r=0;
	mi=1000000;
	int b;
	for(int i=0;i<n;i++){
		cin >> b;
		sum+=b;
		r^=b;
		if(b<mi)
			mi=b;
	}
	if(r)
		cout << "NO" << endl;
	else
		cout << sum-mi << endl;
}

int main(){
	cin >> t;
	for(int i=0;i<t;i++){
		cout << "Case #" << i+1 << ": ";
		process();
	}
	return 0;
}