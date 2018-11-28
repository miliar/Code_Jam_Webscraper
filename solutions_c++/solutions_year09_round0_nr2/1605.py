#include <iostream>
#include <string>
#include <fstream>
using namespace std;

char nextBasin;

char follow(int** map,int H, int W,int i, int j,char** mapOut);

int main(){
	nextBasin='a';
	fstream inputf,outputf;	
	string inputFile;
	cin >> inputFile;
	inputf.open(inputFile.c_str(),fstream::in);
	if (!inputf){
		cout<<"No file!";
		return -1;
	}
	outputf.open("output.out",fstream::out);
	int N;
	inputf >> N;
	for (int cntN=0;cntN<N;cntN++){
		nextBasin='a';
		int H,W;
		inputf>>H>>W;
		int **map = new int*[H];
		for (int i = 0; i < H; i++)
			map[i] = new int[W];
		char **mapOut = new char*[H];
		for (int i = 0; i < H; i++)
			mapOut[i] = new char[W];
		for (int i=0;i<H;i++)
			for (int j=0;j<W;j++)
				mapOut[i][j]='!';
		for (int i=0;i<H;i++)
			for (int j=0;j<W;j++)
				inputf>>map[i][j];
		for (int i=0;i<H;i++)
			for (int j=0;j<W;j++){
				if (mapOut[i][j]=='!'){
					follow(map,H,W,i,j,mapOut);
				}
			}
		
		outputf<<"Case #"<<cntN+1<<":"<<endl;
		for (int i=0;i<H;i++){
			for (int j=0;j<W;j++){
				outputf<<mapOut[i][j];
				if (j<W-1)
					outputf<<" ";
				else
					outputf<<endl;
			}
		}
		for (int i = 0; i < H; i++){
			delete mapOut[i];
			delete map[i];
		}
		
	}
	inputf.close();
	outputf.close();
	return 0;
}
	
char follow(int** map,int H, int W,int i, int j,char** mapOut){
	if (mapOut[i][j]!='!')
		return mapOut[i][j];

	int nb[4]={15000,15000,15000,15000};
	if (i>0)   nb[0]=map[i-1][j];
	if (j<W-1) nb[2]=map[i][j+1];
	if (i<H-1) nb[3]=map[i+1][j];
	if (j>0)   nb[1]=map[i][j-1];
	int min=15000;
	int minI=5;
	for (int k=0;k<4;k++)
		if (nb[k]<min){
			min=nb[k];
			minI=k;
		}
	if (map[i][j]<=min){
		char temp=nextBasin;
		mapOut[i][j]=nextBasin;
		nextBasin++;
		return temp;
	}
	else{
		if (minI==0)
			mapOut[i][j]=follow(map,H,W,i-1,j,mapOut);
		if (minI==2)
			mapOut[i][j]=follow(map,H,W,i,j+1,mapOut);
		if (minI==3)
			mapOut[i][j]=follow(map,H,W,i+1,j,mapOut);
		if (minI==1)
			mapOut[i][j]=follow(map,H,W,i,j-1,mapOut);
		return mapOut[i][j];
	}
		
}
