#include <iostream>
using namespace std;

int main (int argc, char * const argv[]) {
	int t=0, T;
	scanf("%d",&T);
	while(t<T){
		t++;
		long long N;
		int Pd=0, Pg=0,res=0;
		scanf("%lld %d %d",&N, &Pd, &Pg);
		if(Pd>0) {
			for(int i=1;i<=N && i<=100;i++) {
				if(i * Pd % 100 == 0) {
					res=1;
					break;
				}
			}
		} else {
			res=1;
		}
		if(res==1){
			if(Pg==100 && Pd<100) res=0;
			if(Pg==0 && Pd>0) res=0;
		}

		cout << "Case #" << t << ": ";
		if(res==0)
			cout << "Broken" << endl;
		else
			cout << "Possible" << endl;
	}

	return 0;
}
