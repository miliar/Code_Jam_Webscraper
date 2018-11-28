#include <stdio.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <math.h>
#include <map>
#define MaxLength INT_MAX
#define MaxNode 1000000
#define MN 105
using namespace std;

int M,T,D,N;
int mem[MN][MN];
long long wp[MN];
long long wp2[MN];
long long wpu[MN];
long long wpu2[MN];
double wpf[MN];
double owpf[MN];
double oowpf[MN];
long long owp[MN];
long long owpu[MN];
long long oowp[MN];
long long oowpu[MN];
long long gcd(long long a, long long b){
	if(b==0)
		return a;
	return gcd(b,a%b);
}
int main(){
	int i,j,k,len,t,n,m,maxv,v;
	double result;
	char ss[MN];
	long long temp;
	long long tempu,g;

	scanf("%d",&T);
	for(t=1; t<=T;t++){
		scanf("%d\n", &N);
		for(i=0; i<N;i++){
			gets(ss);
			oowp[i]=owp[i]=wp[i]=0;
			wpu[i]=0;
			for(j=0; j<N;j++)
				if(ss[j]=='.')
					mem[i][j]=-1;
				else if(ss[j]=='1'){
					mem[i][j]=1;
					wp[i]++;
					wpu[i]++;
				}else{
					mem[i][j]=0;
					wpu[i]++;
				}
				
			temp=gcd(wp[i],wpu[i]);
			wp[i]/=temp;
			wpu[i]/=temp;
			wpf[i]=wp[i]*1.0/wpu[i];
		}
		for(i=0; i<N;i++){
			owpu[i]=1;
			g=0;
			for(j=0; j<N;j++)
				if(mem[i][j]!=-1){
					tempu=0;
					temp=0;
					for(k=0; k<N;k++)
						if(mem[j][k]!=-1 && k!=i){
							tempu++;
							temp+=mem[j][k];
						}
					wpu2[j] = tempu;
					wp2[j] = temp;
					temp=gcd(wp2[j],wpu2[j]);
					wpu2[j]/=temp;
					wp2[j]/=temp;
					owpu[i]*=wpu2[j];
					
					g++;
				}
			for(j=0; j<N;j++)
				if(mem[i][j]!=-1)
					owp[i]+=wp2[j]*owpu[i]/wpu2[j];
			owpu[i]*=g;
			g=gcd(owp[i],owpu[i]);
			owp[i]/=g;
			owpu[i]/=g;

			owpf[i]=owp[i]*1.0/owpu[i];
		}
		for(i=0; i<N;i++){
			oowpu[i]=1;
			temp=0;
			oowpf[i]=0;
			for(j=0; j<N;j++)
				if(mem[i][j]!=-1){
					oowpf[i]+=owpf[j];
					temp++;
				}
			oowpf[i]/=temp;
		}
		printf("Case #%d:\n",t);
		for(i=0; i<N;i++){
			tempu = 4*wpu[i]*owpu[i]*oowpu[i];
			temp = wp[i] *owpu[i]*oowpu[i] + 2*wpu[i]*owp[i]*oowpu[i] + wpu[i]*owpu[i]*oowp[i];
			result = wpf[i]+2*owpf[i]+oowpf[i];
			result/=4;
			cout << result << endl;
		}
	}
	
	return 0;
}
