// A.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <map>
#include <math.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

long double avar(int* mas, int n){
	int sum = 0;
	long double count = 0;
	for(int i=0; i<n; i++)
		if(mas[i]>=0){
			sum+=mas[i];
			count++;
		}
	return sum/count;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* in = freopen("input.txt", "r", stdin);
	FILE* out = freopen("output.txt", "w", stdout);

	int T;
	cin>>T;
	for(int t=0; t<T; t++){
		int n;
		cin>>n;

		char* str = new char[n+2];
		
		int** mas = new int*[n];
		for(int i=0; i<n; i++)
			mas[i] = new int[n];

		for(int i=0; i<n; i++){
			cin>>str;
			for(int j=0; j<n; j++)
				if(str[j]=='1') mas[i][j] = 1;
				else {
					if(str[j] == '0') mas[i][j] = 0;
					else mas[i][j] = -1;
				}
		}

		long double * WP = new long double[n];

		for(int i=0; i<n; i++){			
			WP[i] = avar(mas[i], n);			
		}

		int* pg = new int[n];
		
		for(int i=0; i<n; i++){
			pg[i]=0;
			for(int j=0; j<n; j++)
				if(mas[i][j]>=0) pg[i]++;
		}

		long double * OWP = new long double[n];
		for(int i=0; i<n; i++){
			int count = 0;
			OWP[i] = 0;
			for(int j=0; j<n; j++)
				if(mas[i][j]>=0){
					count++;
					OWP[i]+=(WP[j]*pg[j]-mas[j][i])/(pg[j]-1);
				};
			OWP[i]/=count;
		}

		long double * OOWP = new long double[n];
		for(int i=0; i<n; i++){
			OOWP[i] = 0;
			for(int j=0; j<n; j++)
				if(mas[i][j]>=0)
					OOWP[i]+=OWP[j];
			OOWP[i]/=pg[i];
		}

		cout<<"Case #"<<t+1<<":\n";
		for(int i=0; i<n; i++){
			//cout<<WP[i]<<endl<<OWP[i]<<endl<<OOWP[i]<<endl;
			printf("%0.8lf\n", (25.0*WP[i]+50.0*OWP[i]+25.0*OOWP[i])/(long double)100);
		}
		
		for(int i=0; i<n; i++)
			delete[] mas[i];
		delete[] mas;
		delete[] str;
		delete[] pg;
		delete[] WP;
		delete[] OWP;
		delete[] OOWP;
	}

	fclose(in);
	fclose(out);
	return 0;
}

