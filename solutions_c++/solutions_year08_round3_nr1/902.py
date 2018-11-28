// prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int g_num; 

int main(int argc, char* argv[])
{
	int nNumTestCase; // Number of TestCase; 
	int res; 
	

	FILE *fpDataIn;
	FILE *fpDataOut; 
	
	if( (fpDataIn = fopen( argv[1], "r" )) == NULL )
		exit( 1 );
	if( (fpDataOut = fopen( argv[2], "w" )) == NULL )
		exit( 1 );
	


	//fseek( fpDataIn, 0L, SEEK_SET );
	//fgets( buffer, 100, fpDataIn ); 
	//nNumTestCase = atoi(buffer); 
	fscanf(fpDataIn,"%d",&nNumTestCase);

	int pushnum; 
	

	for(int i=0;i<nNumTestCase;i++) {
		vector<int> array;
		int p,k,l; 
		int properkey; 




		fscanf(fpDataIn,"%d %d %d",&p,&k,&l);
		properkey = k; 
//		properkey =  l/k; 
//		if(properkey*k  != l)properkey++; 
		res =0; 

		for(int j=0;j<l;j++) {
			fscanf(fpDataIn,"%d",&pushnum);
			array.push_back(pushnum);
		}
		sort(array.begin(), array.end());
		if((p*k) < l )  {
			fprintf(fpDataOut,"Case #%d: impossible\n",i+1);
		} else {
			//	printf("%d",array[0]); 
			int mul=1; 
			for(int i2=l-1; i2 >= 0;) {
				printf("\nbegin\n"); 
				for(int i3=0; (i3<properkey ) && (i2 >= 0 );i3++) {
//					printf("%d ",array[i2]); 
					/*
					if(array[i2] <0  || array[i2]*mul > 1000000 ) {
						printf("\ncase = %d array = %d, mul = %d \n ",i+1,array[i2],mul); 
						i2 = -10; 
						break; 
					}*/
					res = res + (array[i2]*mul);
					i2--; 
				}
				printf("\r\n res = %d \r\n",res); 
				printf("\nend"); 
				mul++; 
			}
			if(i2 == -10) {
				fprintf(fpDataOut,"Case #%d: impossible\n",i+1);
			}else fprintf(fpDataOut,"Case #%d: %d\n",i+1,res);
		}
		// getch();
	}
	// getch();
	fclose( fpDataIn );
	fclose( fpDataOut );
	return 1; 
}

