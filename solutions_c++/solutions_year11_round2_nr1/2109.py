#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
#include<string>
#include<cstdio>
using namespace std;

char s[105][105];

double wp[105];
double owp[105];
double oowp[105];
double sum1[105];
double sum0[105];
double sump[105];

int main() 
{
	int cas,t,i,j,n,m;
	freopen("A-largein.txt","r",stdin);	freopen("out.txt","w",stdout);
	cin>>t;
	for(cas=1;cas<=t;cas++){
		cin>>n;
		for(i=0;i<n;i++){
			sum1[i]=sum0[i]=sump[i]=0.0;
			getchar();
			for(j=0;j<n;j++){
				cin>>s[i][j];
				if(s[i][j]=='1'){
					sum1[i]=sum1[i]+1.0;
				}else if(s[i][j]=='0'){
					sum0[i]=sum0[i]+1.0;
				}else if(s[i][j]=='.'){
					sump[i]=sump[i]+1.0;
				}
			}
		}
		///////////wp////////////
		for(i=0;i<n;i++){
			wp[i]=sum1[i]/(sum1[i]+sum0[i]);
		}
		///////////owp///////////
		for(i=0;i<n;i++){
			double sum=0.0;
			int ktemp=0;
			for(j=0;j<n;j++){
				if(j!=i){
					if(s[j][i]!='.'){
						ktemp++;
						if(s[j][i]=='1'){
							sum += (sum1[j]-1.0)/(sum1[j]-1.0+sum0[j]);
						}else if(s[j][i]=='0'){
							sum += sum1[j]/(sum1[j]-1.0+sum0[j]);
						}
					}
				}
			}
			owp[i] = (1.0/(ktemp))*sum;
		}
		///////////oowp//////////
		for(i=0;i<n;i++){
			double sum=0.0;
			int ktemp=0;
			for(j=0;j<n;j++){
				if(j!=i){
					if(s[j][i]!='.'){
						ktemp++;
						sum += owp[j];
					}
				}
			}
			oowp[i] = (1.0/(ktemp))*sum;
		}		
		////////////////////////
		cout<<"Case #"<<cas<<":"<<endl;
		//
		for(i=0;i<n;i++){
			cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
		}
	}
	return 0;
} 



