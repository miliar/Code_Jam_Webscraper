#include <iostream>
#include <cmath>
using namespace std;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T,N;
	cin>>T;

	for(int t = 0; t < T; ++ t)
	{
		int res = 0;
		int binall[1000];
		memset(binall,0,1000*sizeof(int));
		int mini = 1000000 + 1;
		cin>>N;
		for(int n = 0;n < N; ++ n){
			int tempi;
			cin>>tempi;
			if (tempi < mini) mini = tempi;
			res += tempi;
			int p = 0;
			while (tempi > 0){				
				binall[p] += tempi%2;
				tempi = tempi/2;
				++ p;
			}
		}
		bool nocry = true;
		for(int i = 0; i < 30; ++ i){
			if (binall[i] % 2 != 0){
				nocry = false; break;
			}
		}
		if (nocry){
			cout<<"Case #"<<t+1<<": "<<res - mini<<endl;
		}else{
			cout<<"Case #"<<t+1<<": NO"<<endl;
		}
	}
	return 0;
}