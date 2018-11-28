#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<vector>


using namespace std;


void main()
{
	freopen("input.txt","r",stdin);
	freopen("Output.txt","w",stdout);


	int T;
	scanf("%d",&T);
	for(int tT=0;tT<T;tT++){
		int n;
		char N[200][200];
		double W[150];
		int WT[150];
		double OWP[150];
		double OOWP[150];

		cin>>n;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				cin>>N[i][j];
			}
		}

		for(int i=0;i<n;i++){
			W[i]=0;
			WT[i]=0;
			for(int j=0;j<n;j++){
				if(N[i][j]=='1')(W[i]++,WT[i]++);
				else if(N[i][j]=='0')WT[i]++;				
			}
			W[i]/=WT[i];
		}

		for(int i=0;i<n;i++){
			OWP[i]=0;
			int Too=0;
			for(int j=0;j<n;j++){
				if(j!=i){
					if(N[j][i]=='1'){
						OWP[i]+=(W[j]*WT[j]-1)/(WT[j]-1);
						Too++;
					}
					else if(N[j][i]=='0'){
						OWP[i]+=(W[j]*WT[j])/(WT[j]-1);
						Too++;
					}
				}
			}
			OWP[i]/=Too;
		}

		for(int i=0;i<n;i++){
			OOWP[i]=0;
			int Too=0;
			for(int j=0;j<n;j++){
				if(j!=i && N[i][j]!='.')(OOWP[i]+=OWP[j],Too++);
			}
			OOWP[i]/=Too;
		}

		printf("Case #%d:\n",tT+1);
		for(int i=0;i<n;i++){
			double RPI = 0.25 * W[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			printf("%.10f\n",RPI);
		}
		
	}
}

