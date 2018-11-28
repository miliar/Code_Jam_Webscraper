#include<iostream>
#include<fstream>
#define MAX 40
#define MIN(a,b) ((a)<(b)?(a):(b))
using namespace std;
typedef long long LL;
double ch[MAX+1][MAX+1];
double dp[MAX+1][MAX+1];
bool computed[MAX+1][MAX+1];
void pre(){
	ch[0][0]=1;
	for(int n=1; n<=MAX; ++n){
		for(int k=0; k<=n; ++k){
			if(!k) ch[n][k]=1;
			else ch[n][k]=ch[n-1][k-1]+ch[n-1][k];
		}
	}
}
int c,n;

double compute(int picked, int remain){
	if(remain==0)
		return 0;
	if(computed[picked][remain])
		return dp[picked][remain];
	double rtn=0;
	double getout;
	double tot;
	if(picked>=n){
		double prob=1-ch[picked][n]/ch[c][n];
		tot=prob;
		getout=1/prob;
	}else{
		getout=1;
		tot=1;
	}
	//cout<<picked<<" "<<remain<<" "<<getout<<endl;
	for(int i=1; i<=MIN(remain, n); ++i){
		
		if(remain<i || picked<n-i) continue;
		double way=ch[remain][i]*ch[picked][n-i];
		double prob=way/ch[c][n];
		//cout<<picked<<" "<<remain<<" "<<i<<" "<<prob<<endl;
		rtn+=prob/tot*(getout+compute(picked+i, remain-i));
	}

	//cout<<picked<<" "<<remain<<" "<<rtn<<endl;
	dp[picked][remain]=rtn;
	computed[picked][remain]=true;
	return rtn;
}

int main(){
	pre();
	ifstream fin("C-large.in");
	freopen("C.out","w",stdout);
	
	int ca;
	fin>>ca;
	for(int cas=1; cas<=ca; ++cas){
		fin>>c>>n;
		memset(computed, 0, sizeof(computed));
		double rtn;
		if(c<=n)
			rtn=1;
		else
			rtn=compute(0,c);
		printf("Case #%d: %.7f\n", cas, rtn);
	}
}

