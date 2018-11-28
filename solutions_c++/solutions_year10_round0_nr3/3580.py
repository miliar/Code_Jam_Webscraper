//============================================================================
// Name        : Theme.cpp
// Author      : Bernis
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#include <algorithm>
using namespace std;



int main() {
	FILE * fin, *fout;
	
	//long int max=100; //100000000
    //string fname = "C";
	//freopen((fname+".in").c_str(), "r", stdin);
	//freopen((fname+".out").c_str(), "w", stdout);
	
	fin = fopen("C.in", "r");
	fout = fopen("output.out", "w");
	
	long int T,R,K,N,g,v=0;
	long int total, somme, temp, gsom;
	
	queue <long int> qIntegers;
	queue <long int> save;
	
	fscanf(fin,"%d", &T);
	
	for (long int c = 1; c <= T; ++c) {
		fscanf(fin,"%d", &R);
		fscanf(fin,"%d", &K);
		fscanf(fin,"%d", &N);
		gsom =0;
		for(long int i=1; i<=N; i++){
			fscanf(fin,"%d", &g);
			gsom=gsom+g;
			qIntegers.push(g);		
		}
		
		printf("R=%d\n", R);
		printf("K=%d\n", K);
		printf("N=%d\n", N);
		printf("gsom=%d\n", gsom);
		total=0;
		
		for(long int j=1; j<=R; j++){
			somme=0;
			
			while(somme <= K){
				v=0;
				temp= qIntegers.front();
				somme= somme + temp;
				
				if((somme <= K) && (gsom > K)){	
					save.push(temp);
					if(qIntegers.size()) qIntegers.pop();
				}else if(somme > K){
					v=1;
					somme= somme - temp;
					while (!save.empty()){
					    qIntegers.push(save.front());
					    save.pop();
					 }
					break;			
				}else if(gsom <=K){
					v=1;
					total=R*gsom;
					somme=0;
					printf("pourtant je passe");
					break;
				}
				if (v==1)break;
			}
			printf("somme=%d\n", somme);
			total=total+somme;
			
		} 
		fprintf(fout,"Case #%d: %d\n", c, total);
		while (!qIntegers.empty())  qIntegers.pop();
		
	}
	return 0;
}
