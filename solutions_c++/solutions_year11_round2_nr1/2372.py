#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>

using namespace std;
int Wlen(char *in,int N){
int total=0;
for(int i=0;i<N;i++) if(in[i]=='1' || in[i]=='0') total++;
return (total);
}
float WP(char *in,int N,int mis){
	int ones=0,total=0;
	if(in[mis]=='.') return 0;
	for(int i=0;i<N;i++)if(i!=mis){if(in[i]=='1') ones++; if(in[i]=='1' || in[i]=='0') total++;}
	return ((float)ones/total);
}

int main(){
ifstream input;
ofstream output;
input.open("d:/input.in");
output.open("d:/output.in");
int T;
input>>T;
for(int i=1;i<=T;i++){
	output<<"Case #"<<i<<": \n";
	cout<<"Case #"<<i<<": \n";
	int N;
	char tms[100][100];
	input>>N;
	for(int j=0;j<N;j++) input>>tms[j];
	for(int j=0;j<N;j++) {
		float nOWP=0,nWP=0,nOOWP=0;
		nWP=WP(tms[j],N,-1);
		for(int j2=0;j2<N;j2++) if(j2!=j){
			if(tms[j][j2]!='.'){


			nOWP+=WP(tms[j2],N,j);
			float temp=0;
			for(int j3=0;j3<N;j3++) if(j3!=j2){
				temp+=WP(tms[j3],N,j2);
			}
			temp=((float)temp/Wlen(tms[j2],N));
			nOOWP+=temp;
		
		
			}
		}
		nOOWP=((float)nOOWP/Wlen(tms[j],N));
		nOWP=((float)nOWP/Wlen(tms[j],N));
		//printf("WP : %f\n OWP : %f\n OOWP : %f\n",nWP,nOWP,nOOWP);
		output<<((float)(0.25 * nWP + 0.50 * nOWP + 0.25 * nOOWP))<<endl;
	}
	
}
system("pause");
return 0;
}