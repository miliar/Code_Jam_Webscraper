#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cstdlib>
#include<cstring>
#include<set>
#include<map>

using namespace std;

int in(){int a; scanf("%d",&a); return a;}

int main(){
	int t = in();
	int n;
	int c;
	for(int i=1;i<=t;++i){
		n = in();
		int a=0,mi=1001001001;
		long long su=0;
		for(int j=0;j<n;++j){
			c = in();
			a ^= c;
			mi = min(mi,c);
			su += c;
		}
		if(a) 
			cout << "Case #" << i << ": NO" << endl;
		else
			cout << "Case #" << i << ": " << su-mi << endl;
	}
	return 0;
}
