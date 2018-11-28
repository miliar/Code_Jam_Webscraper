#include<iostream>
using namespace std;

int T,R,C;
long long int D;
char c;
long long int ar[600][600];

long long int absol(long long int X) {
	if(X<0.00) return -X;
	return X;
}

bool possible(int X) {
	//cout<<"testing: "<<X<<endl;
	if(X>min(R,C)) return false;
	for(int i=0;i+X<=R;i++) {
		for(int j=0;j+X<=C;j++) {
			long long int totalW=0LL;
			long long int sigmaX=0LL;
			long long int sigmaY=0LL;
			for(int k=0;k<X;k++) {
				for(int l=0;l<X;l++) {
					if(k==0&&l==0) continue;
					if(k==0&&l+1==X) continue;
					if(k+1==X&&l==0) continue;
					if(k+1==X&&l+1==X) continue;
					totalW+=ar[i+k][j+l];
					sigmaX+=(ar[i+k][j+l]*(2*l+1));
					sigmaY+=(ar[i+k][j+l]*(2*k+1));
				}
			}
			//cout<<"mulai dari "<<i<<","<<j<<endl;
			//cout<<"titik pusat: "<<(sigmaX/totalW)<<" , "<<(sigmaY/totalW)<<endl;
			//cout<<"sigmaX, sigmaY, totalW: "<<sigmaX<<" "<<sigmaY<<" "<<totalW<<endl;
			if((sigmaX==totalW*X)&&(sigmaY==totalW*X)) return true;
		}
	}
	return false;
}

int main() {
	cin>>T;
	for(int tc=1;tc<=T;tc++) {
		cin>>R>>C>>D;
		for(int i=0;i<R;i++) {
			for(int j=0;j<C;j++) {
				cin>>c;
				ar[i][j]=(int)c-(int)'0';
				ar[i][j]+=D;
			}
		}
		//test for 3x3
		if(possible(3)) {
			//int l=3,r=1+min(R,C);
			//while(l+1<r) {
			//	int mid=(l+r)/2;
				//cout<<"mid: "<<mid<<endl;
			//	if(possible(mid)) l=mid;
			//	else r=mid;
			//}
			int i;
			for(i=min(R,C);i>=3;i--) {
				if(possible(i)) break;
			}
			cout<<"Case #"<<tc<<": "<<i<<endl;			
		}
		else {
			cout<<"Case #"<<tc<<": IMPOSSIBLE"<<endl;
		}
	}
}
