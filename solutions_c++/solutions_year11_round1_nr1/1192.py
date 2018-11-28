#include <iostream>
#include <set>
#include <string>

using namespace std;

//‚OŠ„‚ðŒx‰ú

int main(){
	int i=0, n;
	cin >> n;
	while(++i<=n){
		int Pd, Pg;
		unsigned long long N;
		cin >> N >> Pd >> Pg;
		if(Pg==100&&Pd<100||Pg==0&&Pd>0)goto BROKEN;
		
		if(N>=100)goto POSSIBLE;
		for(int D=1;D<=N;D++){
		 if(D*Pd%100==0)
		 	goto POSSIBLE;
		}
		BROKEN:
		cout << "Case #" << i << ": " << "Broken" << endl;
		continue;
		POSSIBLE:
		cout << "Case #" << i << ": " << "Possible" << endl;
	}
	return 0;
}