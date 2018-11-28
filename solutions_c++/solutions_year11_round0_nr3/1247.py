#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{

	int T, N, u, v, ur, ut;
	int M, Ms;
	int nc, Tv;
	int C[10000];
	int n[30];
	int marc[10000];
	
	
	nc=1;
	cin>>T;
	while(T--){

		cin>>N;
		ut=Tv=0;
		for(int i=0;i<N;i++){
			cin>>C[i];
			Tv^=C[i];
			ut+=C[i];
			marc[i]=0;
		}
		
		
		if(Tv!=0){
			printf("Case #%d: NO\n",nc);
		}else{
			sort(C,C+N);
			printf("Case #%d: %d\n",nc,ut-C[0]);
		}
		nc++;
	}
	return 0;
}
