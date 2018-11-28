// CropTriangle.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include <iostream> 
#include <fstream> 
#include <vector> 
#include <list> 
#include <algorithm> 
#include <string> 
#include <iostream>
#include <sstream>
using namespace std; 







__int64 N_center_of_triangle(vector<__int64> Fx, vector<__int64> Fy)
{
	  int szLoop = Fx.size(); 
	  __int64 x0, y0,x1,y1,x2,y2,ret; 
	  ret =0;
	
	  for(int i =0 ; i < szLoop ; i++)
	  {
			x0 = Fx[i];
			y0 = Fy[i];
			for(int j = i+1 ; j <  szLoop; j++)
			{
				x1 = Fx[j];
				y1 = Fy[j];
				for(int k = j +1 ; k < szLoop; k++)
				{
					x2 = Fx[k];
					y2 = Fy[k];

					__int64 sumX = x0 + x1 + x2;
					__int64 sumY= y0 + y1 + y2;

					

					if ( sumX % 3 == 0 && sumY % 3 == 0 )
					  ret++; 

				}
			}
			
	  }

	 
	 
     return ret; 
}


int _tmain(int argc, _TCHAR* argv[])
{
	fstream file_op("arqIn.txt",ios::in);
	fstream file_Out("arqOut.txt",ios::out); 
	int Ncases; 
	vector<string> vcStr;  
	char ch[255]; 

	file_op >> Ncases; 
	
	

	stringstream ss;
	string str; 

	int nTrees = 0;
	__int64 A,B,C,D,x0,y0,M;
	
	
    

	for(int k =0 ; k < Ncases; k++)
	{
		
        file_op >> nTrees;
		file_op >> A;
		file_op >> B;
		file_op >> C; 
		file_op >> D;
		file_op >> x0;
		file_op >> y0;
		file_op >> M; 

		vector<__int64> X,Y;
		X.resize(nTrees);
		Y.resize(nTrees); 

		X[0] = x0, Y[0] = y0; 
		
		for(int  i = 1; i < X.size(); i++)
		{

			X[i] = (A * X[i-1] + B) % M;
            Y[i] = (C * Y[i-1] + D) % M;
			
		}
  	
		__int64 ret = N_center_of_triangle(X,Y);


		cout << "Case #" << k+1 << " " << ret << endl; 
		file_Out << "Case #" << k+1 << " " << ret << endl; 


	}



	return 0;
}
