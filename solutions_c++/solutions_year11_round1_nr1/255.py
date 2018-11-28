#include <iostream>

using namespace std;

int main(){


	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	cin>>T;
	for(int i = 0; i < T; ++ i){
		long long N,PD,PG;
		cin>>N>>PD>>PG;
		bool f = false;
		if (PD == 0) f = true;
		else
		for(int j = 1; j <= N; ++ j){
			if (j * PD % 100 == 0)  {f = true;break;}
			
		}
		if (f){
//			cout<<PD<<"	"<<PG<<endl;
			if (PD < 100 && PG == 100) 
				f = false;
			if (PD > 0 && PG == 0)
				f = false;
		
		}

		if (f){
			cout<<"Case #"<<i + 1<<": Possible"<<endl;
		}else{
			cout<<"Case #"<<i + 1<<": Broken"<<endl;
		}
	
	}


	return 0;
}