#include<iostream>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int test=1; test<=T; test++){
		string org;
		int k; cin>>k;
		cin>>org;
		int t[5]={0,1,2,3,4};
		string sec;
		sec.resize(org.size());
		int res=1000000;
		do{
			for(int block=0; block<org.size(); block+=k)
				for(int i=0; i<k; i++)
					sec[block+i]=org[block+t[i]];
			int cnt=0;
			for(int i=0, masker='~'; i<sec.size(); i++)
				if(sec[i]!=masker){
					masker=sec[i];
					cnt++;
				}
			res=min(res,cnt);
		}while(next_permutation(t,t+k));
		printf("Case #%d: %d\n", test, res);
	}
	return 0;
}
