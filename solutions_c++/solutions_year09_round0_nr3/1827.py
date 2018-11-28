#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
#include<sstream>

using namespace std;

vector <int> v[11];

int main(){
	int n,soma=0, caso=1;
	string linha;
	stringstream ss;
	ss.clear();
	getline(cin,linha);
	ss.str(linha);
	ss>>n;
	ss.clear();
	for(int i=0; i<n; i++){
		soma=0;
		for(int j=0; j<11; j++) v[j].clear();
		getline(cin,linha);	
		for(int j=0; j<linha.length(); j++){
			if(linha[j]=='w') v[0].push_back(j);
			else if(linha[j]=='e') v[1].push_back(j);
			else if(linha[j]=='l') v[2].push_back(j);
			else if(linha[j]=='c') v[3].push_back(j);
			else if(linha[j]=='o') v[4].push_back(j);
			else if(linha[j]=='m') v[5].push_back(j);
			else if(linha[j]=='t') v[6].push_back(j);
			else if(linha[j]=='d') v[7].push_back(j);
			else if(linha[j]=='j') v[8].push_back(j);
			else if(linha[j]=='a') v[9].push_back(j);
			else if(linha[j]==' ') v[10].push_back(j);

		}
		/*for(int j=0; j<11; j++){
			for(int k=0; k<v[j].size(); k++) cout<<v[j][k]<<" ";
			cout<<endl;	
		}*/

		for(int w=0; w<v[0].size(); w++)
		for(int e=0; e<v[1].size(); e++)
		if(v[1][e]>v[0][w]) for(int l=0; l<v[2].size(); l++)// w -> e
		if(v[2][l]>v[1][e]) for(int c=0; c<v[3].size(); c++)// e -> l
		if(v[3][c]>v[2][l]) for(int o=0; o<v[4].size(); o++)// l -> c
		if(v[4][o]>v[3][c]) for(int m=0; m<v[5].size(); m++)// c -> o
		if(v[5][m]>v[4][o]) for(int ee=e+1; ee<v[1].size(); ee++)// o -> m
		if(v[1][ee]>v[5][m]) for(int esp=0; esp<v[10].size(); esp++)// m -> e
		if(v[10][esp]>v[1][ee]) for(int t=0; t<v[6].size(); t++)// e -> ' '
		if(v[6][t]>v[10][esp]) for(int oo=o+1; oo<v[4].size(); oo++)// ' ' -> t
		if(v[4][oo]>v[6][t]) for(int esp2=esp+1; esp2<v[10].size(); esp2++) // t -> o
		if(v[10][esp2]>v[4][oo]) for(int cc=c+1; cc<v[3].size(); cc++) // o -> ' '
		if(v[3][cc]>v[10][esp2]) for(int ooo=oo+1; ooo<v[4].size(); ooo++) // ' ' -> c
		if(v[4][ooo]>v[3][cc]) for(int d=0; d<v[7].size(); d++) // c -> o
		if(v[7][d]>v[4][ooo]) for(int eee=ee+1; eee<v[1].size(); eee++) // o -> d
		if(v[1][eee]>v[7][d]) for(int esp3=esp2+1; esp3<v[10].size(); esp3++) //d - > e
		if(v[10][esp3]>v[1][eee]) for(int j=0; j<v[8].size(); j++) // e -> ' '
		if(v[8][j]>v[10][esp3]) for(int a=0; a<v[9].size(); a++) // ' ' -> j
		if(v[9][a]>v[8][j]) for(int mm=m+1; mm<v[5].size(); mm++) // j - > a
		if(v[5][mm]>v[9][a]) soma++; // a - > m
		soma=soma%10000;					
		if(soma<10) cout<<"Case #"<<caso<<": 000"<<soma<<endl;
		else if(soma<100) cout<<"Case #"<<caso<<": 00"<<soma<<endl;
		else if(soma<1000) cout<<"Case #"<<caso<<": 0"<<soma<<endl;
		else cout<<"Case #"<<caso<<": "<<soma<<endl;
		caso++;
		
	}
}
