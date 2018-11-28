#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<set>
#include<map>
#include<cstring>
#include<cmath>
using namespace std;
double pw2(double dd){
	return dd*dd;
}
int main(){
	int n;
	cin >> n;
	for(int i=0 ; i<n ; i++){
		int num;
		cin >> num;
		double pos[3],vel[3];
		for(int k=0 ; k<3 ; k++){
			pos[k]=0.0; vel[k]=0.0;
		}
		for(int j=0 ; j<num ; j++){
			for(int k=0 ; k<3 ; k++){
				int temp; cin >> temp;
				pos[k]+=temp;
			}
			for(int k=0 ; k<3 ; k++){
				int temp; cin >> temp;
				vel[k]+=temp;
			}
		}
		for(int k=0 ; k<3 ; k++){
			pos[k]/=num;
		}
		for(int k=0 ; k<3 ; k++){
			vel[k]/=num;
		}
		double mint=0,mind=0;
		mint=pos[0]*vel[0] + pos[1]*vel[1] + pos[2]*vel[2];
		double hoge= (vel[0]*vel[0]+vel[1]*vel[1]+vel[2]*vel[2]);
		if(hoge>1e-8) {
			mint/=hoge;
			mint=-mint;
			if(mint<0.0){
				mint=0.0;
				mind=sqrt(pos[0]*pos[0]+pos[1]*pos[1]+pos[2]*pos[2]);
			}else {
				mind=sqrt(pw2(pos[0]+vel[0]*mint)+pw2(pos[1]+vel[1]*mint)
					+pw2(pos[2]+vel[2]*mint));
			}
		}else{
			mint=0.0;
			mind=sqrt(pos[0]*pos[0]+pos[1]*pos[1]+pos[2]*pos[2]);
		}

		printf("Case #%d: %.8f %.8f\n",i+1,mind,mint);
	}
	return 0;
}