#include <iostream>

using namespace std;

const int MaxN= 1000000 + 10;

int n;
int c, d;
int p[MaxN];

inline bool canGo(int k){
	int back= p[0] - k;
	for (int i=1 ; i<n ; i++){
		int des= back+d;
		if (des<p[i]){
			if (p[i]-des>k)
				back= p[i]-k;
			else
				back= des;
		}else{
			if (des-p[i]>k)
				return false;
			else
				back= des;
		}
	}
	return true;
}
/**************************************/
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		cin >> c >> d;
		d*= 2;
		n= 0;
		for (int i=0 ; i<c ; i++){
			int o, v;
			cin >> o >> v;
			o*= 2;
			while(v--)
				p[n++]= o;
		}
//		for (int i=0 ; i<n ; i++)
//			cout << i << " -> " << p[i] << endl;
		int f= 0, l= 1000000000;
		while(f<l){
			int m= (f+l)/2;
//			cout << f << ' ' << m << ' ' << l << endl;
			if (canGo(m))
				l= m;
			else
				f= m+1;
		}
		cout << "Case #" << t << ": ";
		if (f%2==0)
			cout << f/2 << ".0" << endl;
		else
			cout << f/2 << ".5" << endl;
	}
	return 0;
}