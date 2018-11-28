#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int N,i,o,NA,T,NB,a,trenA,trenB;
vector<string> bTA,bTB;
vector< vector<int> > TlA,TlB,TsA,TsB;
vector<bool> cubiertoA,cubiertoB;
char pos;
int hora;
string buffer;

int main(){
int h=0,m=1,min=0;
cin >> N;
for(i=0;i<N;i++){
	cin >> T;
	cin >> NA >> NB;

	getline(cin,buffer);
	bTA.resize(NA);
	bTB.resize(NB);
	for(o=0;o<NA;o++) getline(cin,bTA[o]);
	for(o=0;o<NB;o++) getline(cin,bTB[o]);

	sort(bTA.begin(),bTA.end());
	sort(bTB.begin(),bTB.end());

	TlB.resize(NA);
	TsA.resize(NA);
	for(o=0;o<NA;o++){
		TlB[o].resize(2);
		TsA[o].resize(2);

		TsA[o][h]=(bTA[o][0]-'0')*10+(bTA[o][1]-'0');
		TsA[o][m]=(bTA[o][3]-'0')*10+(bTA[o][4]-'0');


		TlB[o][h]=(bTA[o][6]-'0')*10+(bTA[o][7]-'0');
		TlB[o][m]=(bTA[o][9]-'0')*10+(bTA[o][10]-'0')+T;

		while(TlB[o][m] >= 60){ TlB[o][m]-=60; TlB[o][h]++; }
		

	}

	TlA.resize(NB);
	TsB.resize(NB);
	for(o=0;o<NB;o++){
		TlA[o].resize(2);
		TsB[o].resize(2);

		TsB[o][h]=(bTB[o][0]-'0')*10+(bTB[o][1]-'0');
		TsB[o][m]=(bTB[o][3]-'0')*10+(bTB[o][4]-'0');


		TlA[o][h]=(bTB[o][6]-'0')*10+(bTB[o][7]-'0');
		TlA[o][m]=(bTB[o][9]-'0')*10+(bTB[o][10]-'0')+T;

		while(TlA[o][m] >= 60){ TlA[o][m]-=60; TlA[o][h]++; }		
		
	}


//	for(o=0;o<NA;o++) printf("%i:%i %i:%i\n",TsA[o][h],TsA[o][m],TlB[o][h],TlB[o][m]);
	cubiertoA.resize(NA);
	for(o=0;o<NA;o++) cubiertoA[o]=0;
	cubiertoB.resize(NB);
	for(a=0;a<NB;a++) cubiertoB[a]=0;
	

	trenA=0; trenB=0;

	while(1){
		for(o=0;o<NA;o++) if(cubiertoA[o]==0) break;
		for(a=0;a<NB;a++) if(cubiertoB[a]==0) break;

		if(a==NB && o==NA) break;

		hora=0;
		min=0;

		if(NA==o){ pos='B'; trenB++; }
		else if(NB==a){ pos='A'; trenA++; }
		else if(TsA[o][h]>TsB[a][h] || (TsA[o][h]==TsB[a][h] && TsA[o][m]>TsB[a][m])){ pos='B'; trenB++; }
		else { pos='A';	trenA++; }

		while(1){
			if(pos=='A'){
				for(o=0;o<NA;o++) 
					if(cubiertoA[o]==0 && (TsA[o][h]>hora || (TsA[o][h]==hora && TsA[o][m]>=min))) break;
				if(o==NA) break;
				
				hora=TlB[o][h];
				min=TlB[o][m];
				cubiertoA[o]=1;
				pos='B';
//				printf("%i-%i,Sale de A, llega a las %i:%i\n",trenA,trenB,hora,min);
			}
			else {
				for(o=0;o<NB;o++) 
					if(cubiertoB[o]==0 && (TsB[o][h]>hora || (TsB[o][h]==hora && TsB[o][m]>=min))) break;
				if(o==NB) break;
				
				hora=TlA[o][h];
				min=TlA[o][m];
				cubiertoB[o]=1;
				pos='A';
//				printf("%i-%i,Sale de B, llega a las %i:%i\n",trenA,trenB,hora,min);				
			}
		}
	}

	cout << "Case #" << i+1 << ": " << trenA << " " << trenB << endl;

}

}
