#include <iostream>
#include <fstream>

using namespace std;

/*ifstream fin("GCJ P D.in");
ofstream fout("GCJ P D.out");

#define cin fin
#define cout fout*/

int t;
int n;

void init(){
	cin >> n;
}

void process(){
	int ans=0;
	int b;
	for(int i=1;i<=n;i++){
		cin >> b;
		ans+=(b!=i);
	}
	cout << ans << ".000000" << endl;
}

int main(){
	cin >> t;
	for(int i=0;i<t;i++){
		cout << "Case #" << i+1 << ": ";
		init();
		process();
	}
	return 0;
}