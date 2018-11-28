/*
 * RPI.cpp
 *
 *  Created on: May 22, 2011
 *      Author: batchunag
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <stdio.h>
#include <string.h>
#include <list>
#define FOR(i,a,b) for (int i=a; i<b; i++)
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define mp make_pair
#define pb push_back

using namespace std;
typedef vector<int> VI;
typedef pair <int,int> PII;

int main(){
	freopen("input.txt","r",stdin);
	freopen("answer.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=1; t<=T; t++){
		cout<<"Case #"<<t<<':'<<endl;
		int N;
		cin>>N;
		string S[N];
		for (int i=0; i<N; i++)
			cin>>S[i];
		double wp[N],owp[N],oowp[N];
		double w[N],l[N];
		for (int i=0; i<N; i++){
			w[i]=0,l[i]=0;
			for (int j=0; j<N; j++){
				if (S[i][j]=='1') w[i]++;
				else if (S[i][j]=='0') l[i]++;
			}
			if (w[i]+l[i]==0) wp[i]=0;
			else wp[i]=w[i]/(w[i]+l[i]);
		}
		for (int i=0; i<N; i++){
			double sum=0.0;
			double x=0.0;
			for (int j=0; j<N; j++){
				if (S[i][j]=='1') {
					if (w[j]+l[j]>1) sum+=(w[j])/(w[j]+l[j]-1);
					x++;
				}
				else if (S[i][j]=='0') {
					if (w[j]+l[j]>1) sum+=(w[j]-1)/(w[j]+l[j]-1);
					x++;
				}
			}
			//printf("%.7lf#%lf\n",sum,x);
			owp[i]=sum/x;
		}
		//cout<<endl;
		for (int i=0; i<N; i++){
			double sum=0.0;
			double x=0.0;
			for (int j=0; j<N; j++){
				if (S[i][j]!='.') {
					x=x+1;
					sum+=owp[j];
				}
			}
			//printf("%.7lf#%lf\n",sum,x);
			if (x>0 ) oowp[i]=sum/x;
			else oowp[i]=0;
		}
		//cout<<endl;
		for (int i=0; i<N; i++)
			printf("%.8lf\n",0.25*( wp[i]+oowp[i])+0.5*owp[i]);
			//printf("%.7lf %.7lf %.7lf\n",wp[i],owp[i],oowp[i]);
	}
	return 0;
}
