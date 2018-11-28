#include<iostream>
using namespace std;
int main(){
	int t,num;
	cin>>t;
	for(int l=1;l<=t;l++){
		int ans=0;
		cin>>num;
		char robot[101];
		int dis[101];
		int stack=0;
		int tmp;
		for(int i=0;i<num;i++){
			cin>>robot[i];
			cin>>dis[i];
		}
		int poso=1,posb=1;
		int stacko=0,stackb=0,need;
		for(int i=0;i<num;i++){	
			//cout<<ans<<" ";
			if(robot[i]=='O'){
				//stackb+=abs(dis[i]-poso)+1;
				need=abs(dis[i]-poso)-stacko+1;
				stacko=0;
				if(need<=0)need=1;
				stackb+=need;

				ans+=need;
				poso=dis[i];
			}
			else if(robot[i]=='B'){
				//stacko+=abs(dis[i]-posb)+1;
				need=abs(dis[i]-posb)-stackb+1;
				stackb=0;
				if(need<=0)need=1;
				stacko+=need;

				ans+=need;
				posb=dis[i];
			}
		}
		cout<<"Case #"<<l<<": "<<ans<<endl;
	}		
	return 0;
}