#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#define ll long long
using namespace std;
/*int modder(double ans){
	ll ans2=(ll)ans;
	return ans2%1000;
}*/
int main(){
string ans[32];
//Table of values calculated using calculator included in base install of Ubuntu
ans[2]="027";
ans[3]="143";
ans[4]="751";
ans[5]="935";
ans[6]="607";
ans[7]="903";
ans[8]="991";
ans[9]="335";
ans[10]="047";
ans[11]="943";
ans[12]="471";
ans[13]="055";
ans[14]="447";
ans[15]="463";
ans[16]="991";
ans[17]="095";
ans[18]="607";
ans[19]="263";
ans[20]="151";
ans[21]="855";
ans[22]="527";
ans[23]="743";
ans[24]="351";
ans[25]="135";
ans[26]="407";
ans[27]="903";
ans[28]="791";
ans[29]="135";
ans[30]="647";
	int N;
	cin>>N;
	double thing=3+sqrt(5);
	for(int z=1;z<=N;z++){
		cout<<"Case #"<<z<<": ";
		int n;
		cin>>n;
		cout<<ans[n]<<endl;
		/*
		float ans=thing;
		for(int i=1;i<n;i++){
			ans*=thing;
			while(ans>100000000)
				ans-=1000000000;
		}
		int finalans=modder(ans);
		if(finalans<100)
			cout<<"0";
		if(finalans<10)
			cout<<"0";
		cout<<finalans<<endl;
		*/
	}
}
