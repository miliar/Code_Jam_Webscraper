#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

ifstream in("a.in");
ofstream out("a.out");

void sol(int testCase){
	int n;
	in >> n;
	int a[n], b[n], st[n];
	for(int i = 0; i < n; i++){
		in >> a[i];
		b[i] = a[i];
	}
	sort(b, b + n);
	out << "Case #" << testCase << ": ";
	int m = n;
	for(int i = 0; i < n; i++) if(a[i] == b[i]) m--;
	
	out << m << ".000000" << endl;
}

int main(){
	int n;
	in >> n;
	for(int i = 0; i < n; i++) sol(i + 1);
}
