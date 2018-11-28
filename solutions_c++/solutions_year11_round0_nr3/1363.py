#include <fstream>
#include <cmath>

using namespace std;

ifstream in("in");
ofstream out("out");

void sol(int testCase){
	int n;
	in >> n;
	
	int a[n], x = 0, s = 0, m = 1000000000;
	for(int i = 0; i < n; i++){
		in >> a[i];
		x ^= a[i];
		s += a[i];
		m = min(m, a[i]);
	}
	out << "Case #" << testCase << ": ";
	if(x) out << "NO";
	else out << s - m;
}

int main(){
	int n;
	in >> n;
	for(int i = 0; i < n; i++) sol(i + 1), out << endl;
}
