#include"stdlib.h"
#include"stdio.h"
#include <string>
#include<cmath>
#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int WinMap[101][101]={0};
double WP[101]={0};
double OWP[101]={0};
double OOWP[101]={0};
double score[101]={0};
int main()
{
ifstream in;
ofstream out;
in.open("A-large.in");
out.open("OUTPUT.txt");

int T,N;
in>>T;
char c;

for(int Case=1;Case<=T;Case++){
	in>>N;
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			in>>c;
			if(c=='0')WinMap[i][j]=-1;
			else if(c=='1')WinMap[i][j]=1;
			else WinMap[i][j]=0;
		}
	}
	for( i=0;i<N;i++){
	double sum=0,win=0;
	for(int j=0;j<N;j++){
		if(WinMap[i][j]!=0)	sum++;
		if(WinMap[i][j]>0)win++;

	}
	if(sum>=0.5)WP[i]=win/sum;
	else WP[i]=0;
	}
	for( i=0;i<N;i++){
		OWP[i]=0;
		int n=0;
		for(int j=0;j<N;j++){
			if(WinMap[i][j]==0)continue;
			n++;
			double sum=0,win=0;

			for(int k=0;k<N;k++){
				if(k==i)continue;
				if(WinMap[j][k]!=0)sum++;
				if(WinMap[j][k]>0)win++;
				

			}
			if(sum>=0.5)OWP[i]+=win/sum;
		}
		if(n>0)OWP[i]/=double(n);

	}
	
	for( i=0;i<N;i++){
		OOWP[i]=0;
		int n=0;
		for(int j=0;j<N;j++){
			if(WinMap[i][j]==0)continue;
			OOWP[i]+=OWP[j];
			n++;

		}
		if(n>0)OOWP[i]/=double(n);
	}
	for( i=0;i<N;i++){
		score[i]=0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
	}

	out<<"Case #"<<Case<<":\n";
	for( i=0;i<N;i++){
		out<<fixed<<setprecision(12)<<score[i]<<endl;
	}
}



in.close();
out.clear();
out.close();
return 0;
}