#include<iostream>
using namespace std;

int judge(int x, int b) {
	int tmp =x;
	int num = 1;
	int cnt =0;
	int sum = 0;
	bool flag[2000009] ={0};
	while(tmp) {
		num *=10;
		tmp/=10;
		cnt++;
	}

	for(int i=1; i<cnt; ++i) {
		tmp = x;
		int ttm = i;
		int tnum =1;
		int tt = 0;
		while(ttm) {
			tt = tt+(tmp%10)*tnum;
			tmp /= 10;
			tnum *=10;
			--ttm;
		}
		tt = tt*(num/tnum)+tmp;
		if(tt > x && tt <= b && !flag[tt]){
			flag[tt] = 1;
			sum++;
		}
	}
	return sum;
}

int main()
{
	int t;
	cin >> t;
	for(int cas =1; cas <=t; ++cas) {
		int a,b;
		cin >> a >> b;
		int cont = 0;
		for(int i=a; i<=b; ++i) {
			cont += judge(i,b);
		}
		cout << "Case #" << cas << ": ";
		cout << cont << endl;
	}
	return 0;
}
