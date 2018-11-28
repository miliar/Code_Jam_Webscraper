#include<iostream>
#include<algorithm>
#include<utility>
#include<vector>
#include<map>
#include<cstdio>
#include<cstring>

using namespace std;

int gcd(int a, int b){
       if (b==0) return a;
       else return gcd(b, (a%b));
}

int main(){
	int test, pd, pg;
	long long n;
	
	cin >> test;
	for(int t=1;t<=test;t++){
		cin >> n >> pd >> pg;
		/*
		cout << gcd(pd, 100) << " ";
		cout << 100/gcd(pd, 100) << endl;*/
		
		if(((100/gcd(pd, 100)) > n) ||
			(pg == 100 && pd != 100) ||
			(pg == 0 && pd != 0)) cout << "Case #" << t << ": Broken\n";
		else cout << "Case #" << t << ": Possible\n";
		
	}
	
	return 0;
}
