#include <iostream>
using namespace std;
int N, K, power, turned, z;
unsigned long long tab[35];
void pre(){
	tab[1] = 1;
	for(int i=2; i<=31; i++)
		tab[i] = (long long)2*tab[i-1]+1;
}
void check(){
	if(K-tab[N]==0||((K-tab[N])%(tab[N]+1)==0))
		cout << "Case #" << z <<": ON" << endl;
	else
		cout << "Case #" << z <<": OFF" << endl;
}
int main(){
	int Z=1;
	cin >> Z;
	pre();
	for(z=1; z<=Z; z++){
		cin >> N >> K;
		check();
	}
	return 0;
}


