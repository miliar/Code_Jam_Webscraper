#include<iostream>
#include<vector>
#include<stdio.h>
#include<string>
using namespace std;
int main(){
int tc,n;
char c;
cin>>tc;
for(int i = 0;i<tc;i++){
	cin>>n;
	vector<string> vs(n);
	for(int j = 0;j<n;j++){
		cin>>vs[j];}
	vector<double> wp(n),owp(n),oowp(n);
	vector<int> wing(n), totalg(n);
	for(int j = 0;j<n;j++){
		wing[j] = 0;
		totalg[j] = 0;
	}
	for(int j = 0;j<n;j++){
		for(int k=0;k<n;k++){
			if(vs[j][k] == '1') {
				totalg[j]++;
				wing[j]++;
				}
			else if(vs[j][k] == '0'){
				totalg[j]++;
				}
			}
		wp[j] = (wing[j]*1.0)/totalg[j];
		
		}
	for(int j = 0;j<n;j++){
		double sum = 0.0;
		for(int k = 0;k<n;k++){
			if(vs[j][k] == '0'){
				sum+=((wing[k]-1.0)/(totalg[k]-1.0));
				}
			else if(vs[j][k] == '1'){
				sum+=((wing[k])/(totalg[k]-1.0));
				}
			}
		owp[j] = sum/totalg[j];
		}
	for(int j = 0 ;j<n;j++){
		double sum2=0;
		for(int k = 0;k<n;k++){
			if(vs[j][k] != '.'){
				sum2+=(owp[k]);
				}
			}
		oowp[j] = sum2/totalg[j];
	}
	printf("Case #%d:\n", i+1);
	for(int j = 0;j<n;j++){
		printf("%.12lf\n",(0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j]));
		}
		}			
return 0;
}			
	
		
			
	
