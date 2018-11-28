#include<iostream>
#include<vector>
using namespace std;

double dp[1002];
double perm[1002][1002];
int N,coun,crnt,T;
int ar[1002];
bool bol[1002];
vector<int> loops;
double ans;

double f(int X) {
	if(X<=1) return 0.00;
	//if(X==2) return 2.00;
	if(dp[X]>-1) return dp[X];
	dp[X]=1.00;
	double temp=1.00;
	for(int i=1;i<X;i++) {
		dp[X]+=(f(i)/temp);
		temp+=1.00;
	}
	temp=1.00-(1.00/temp);
	dp[X]=dp[X]/temp;
	return dp[X];
}

int main() {
	cin>>T;
		//cout<<"perm: "<<endl;
		//for(int i=1;i<=4;i++) {
		//	for(int j=1;j<i;j++) {
		//		cout<<"("<<i<<","<<j<<"): "<<perm[i][j]<<endl;
		//	}
		//}
	for(int tc=1;tc<=T;tc++) {
		cin>>N;
		for(int i=1;i<=N;i++) {
			cin>>ar[i];
			bol[i]=false;
			dp[i]=-2.00;
		}
		loops.clear();
		for(int i=1;i<=N;i++) {
			if(bol[i]) continue;
			coun=0;
			crnt=i;
			do {
				bol[crnt]=true;
				crnt=ar[crnt];
				coun++;
			} while(!bol[crnt]);
			loops.push_back(coun);
		}
		//cout<<"loops: "<<endl;
		//for(int i=0;i<loops.size();i++) cout<<loops[i]<<" ";
		//cout<<endl;
		ans=0.00;
		for(int i=0;i<loops.size();i++) ans+=f(loops[i]);
		cout<<"Case #"<<tc<<": ";
		printf("%.10lf\n",ans);
	}
}
