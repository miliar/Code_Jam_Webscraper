#include <iostream>
using namespace std;

typedef int num;
const int maxN = 32000, maxV = 100000000;
int m, tr[maxN], ch[maxN];

int minc(int v, int b){
	int r, rOr, rAnd, l0, l1, r0, r1;
	if(v >= (m+1)/2){
		if(tr[v] == b) return 0;
		else return maxV;
	}
	l0 = minc(2*v, 0);
	l1 = minc(2*v, 1);
	r0 = minc(2*v+1, 0);
	r1 = minc(2*v+1, 1);
	if(b == 0){
		rOr = l0 + r0;
		rAnd = min(l0, r0);
	}else{
		rOr = min(l1, r1);
		rAnd = l1 + r1;
	}
	if(tr[v] == 0){
		//Or
		r = rOr;
		if(ch[v] && r > 1 + rAnd) r = 1 + rAnd;
	}else{
		r = rAnd;
		if(ch[v] && r > 1 + rOr) r = 1 + rOr;
	}
	return r;
}

void doit(){
	int i, b, x;
	cin >> m >> b;
	for(i = 1; i <= (m-1)/2; i++)
		cin >> tr[i] >> ch[i];
	for(i = (m+1)/2; i <= m; i++)
		cin >> tr[i];
	x = minc(1, b);
	if(x >= maxV){
		cout << "IMPOSSIBLE";
		return;
	}
	cout << x;
	return;
}

int main(){
	int tst, tc;
	cin >> tst;
	for(tc = 1; tc <= tst; tc++){
		cout << "Case #" << tc << ": ";
		doit();
		cout << endl;
	}
	//system("pause");
	return 0;
}