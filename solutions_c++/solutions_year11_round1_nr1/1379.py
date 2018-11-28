#include <iostream>

using namespace std;

int main (int argc, char const *argv[])
{
	int T;
	int n, pd, pg;
	cin>>T;
	bool flag;
	for(int i=0; i<T; i++){
		cin>>n>>pd>>pg;
		flag = false;
		if(pg ==0 && pd!=0){
			cout<<"Case #"<<i+1<<": Broken"<<endl;
			continue;
		}else if(pg == 100 && pd != 100){
			cout<<"Case #"<<i+1<<": Broken"<<endl;
			continue;
		}
		for(int j=1; j<=n; j++){
			if((j*pd)%100 == 0){
				cout<<"Case #"<<i+1<<": Possible"<<endl;
				flag = true;
				break;
			}	
		}
		if(flag == false){
			cout<<"Case #"<<i+1<<": Broken"<<endl;
		}
	}
	return 0;
}