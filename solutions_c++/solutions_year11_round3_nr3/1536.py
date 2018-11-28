#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long INT64;
#define MAX (1E16)


INT64 d(INT64 a, INT64 b) {
	INT64 aux;
	while (a % b != 0) {
		if (a < b) {aux=a;a=b;b=aux;}
		else {aux=a;a=b;b=aux%b;}
	}
	return b;
}

INT64 m(INT64 a, INT64 b, INT64 max) {
	INT64 div=d(a,b);
	INT64 q1 = a/div;
	INT64 q2 = b/div;
	if (max/div + 1 < q1*q2) return -1;
	else {
		if (q1*q2*div > max) return -1;
		else return q1*q2*div;
	}
}


INT64 getResult(INT64 min, INT64 max, vector<INT64> f) {
	unsigned int n = f.size();
	vector<INT64> div, mul;
	div.resize(n);mul.resize(n);
	mul[0] = f[0]; if (mul[0]>max) mul[0]=-1;
	for (unsigned int i=1;i<n;++i) {
		if (mul[i-1] != -1) {mul[i] = m(mul[i-1],f[i],max); if (mul[i] > max) mul[i]=-1;}
		else mul[i] = -1;
	}
	div[n-1] = f[n-1]; if (div[n-1] < min) div[n-1] = -1;
	for (int i=n-2;i>=0;--i) {
		if (div[i+1] != -1) {div[i] = d(div[i+1],f[i]); if (div[i]<min) div[i] = -1;}
		else div[i] = -1;
	}
	INT64 bestD = -1,bestM = -1;
	if (div[0] != -1) {bestD = div[0];}
	else {
		for (unsigned int i=0;i<n-1;++i) {
			if (mul[i] == -1 || mul[i] > max) break;
			if (div[i+1] != -1 && div[i+1] % mul[i] == 0) {bestM = mul[i];bestD=div[i+1];break;}
		}
		if ((bestD == -1) && (mul[n-1] != -1)) {bestM = mul[n-1];}
	}
	//cerr << "bestM="<<bestM <<" bestD="<<bestD<<endl;
	if (bestD != -1 || bestM != -1) {
		for (INT64 i=min;i<=max;++i) {
			if (bestM == -1) {
				if (bestD % i == 0) return i;
			} else {
				if (bestD == -1) {
					if (i % bestM == 0) return i;
				} else {
					if (bestD % i == 0 && i % bestM == 0) return i;
				}
			}
		}
	}
	
	return -1;
}

int main(/*int argc, char** argv*/) {
    unsigned int T = 0;

    cin >> T;
    for (unsigned int t = 0; t < T; ++t) {
        unsigned int n;
		INT64 min, max ;
        vector<INT64> f;

		cin >> n;
		cin >> min;
		cin >> max;
        f.resize(n);
        for (unsigned int i = 0; i < n; ++i) cin >> f[i];
		sort(f.begin(),f.end());
		INT64 result = getResult(min,max,f);
		//INT64 bres = -1;
		//for (INT64 j=min;j<=max;++j) {
		//	bool good = true;
		//	for (int i=0;i<n;++i) if (f[i] % j != 0 && j % f[i] != 0) {good=false;break;}
		//	if (good) {bres = j; break;}
		//}
		//if (bres != result) cerr << "ERROR case#" << t+1 << " real=" <<bres <<" false=" << result << endl;
		if (result == -1) cout << "Case #" << (t + 1) << ": " << "NO" << endl;
		else cout << "Case #" << (t + 1) << ": " << result << endl;
    }
    return 0;
}
