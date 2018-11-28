#include <iostream.h>
#include <fstream.h>
#include <list.h>


int main(void)
{
	int iCases;
	int iCaseCounter;
	int answer;
	unsigned long points[100000][2];
	unsigned long A,B,C,D,x0,y0,M;
	unsigned long n;
	__int64 X,Y;
	unsigned long i;
	unsigned long x1,x2,x3,y1,y2,y3;
	unsigned long i1,i2,i3;
	unsigned long sumx,sumy;

	ifstream inFile;
	
	
	//inFile.open("A-test.in");
	inFile.open("A-small-attempt2.in");
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> iCases;
	for (iCaseCounter=1;iCaseCounter<iCases+1;iCaseCounter++)
	{
		answer = 0;
		
		inFile >> n;
		inFile >> A;
		inFile >> B;
		inFile >> C;
		inFile >> D;
		inFile >> x0;
		inFile >> y0;
		inFile >> M;
		
		X = x0;
		Y = y0;
		for ( i=0;i<n;i++ )
		{
			//cout << "X: " << X << ", Y: " << Y << endl;
			points[i][0] = X;
			points[i][1] = Y;
			X = ( A*X+B ) % M;
			Y = ( C*Y+D ) % M;
		}
		
		for ( i1=0;i1<n-2;i1++ )
		{
			for (i2=i1+1;i2<n-1;i2++)
			{
				for (i3=i2+1;i3<n;i3++)
				{
					x1 = points[i1][0];
					x2 = points[i2][0];
					x3 = points[i3][0];
					y1 = points[i1][1];
					y2 = points[i2][1];
					y3 = points[i3][1];
					sumx = x1+x2+x3;
					sumy = y1+y2+y3;
					if ( (sumx%3 == 0) && (sumy%3 == 0) )
					{
						/*
						cout << "x1: " << x1 << ";";
						cout << "x2: " << x2 << ";";
						cout << "x3: " << x3 << ";";
						cout << "y1: " << y1 << ";";
						cout << "y2: " << y2 << ";";
						cout << "y3: " << y3 << ";";
						cout << "centerx: " << sumx/3 << ";";
						cout << "centery: " << sumy/3 << endl;
						*/
						answer++;
						
					}
				}
			}			
		}
		
		cout << "Case #" << iCaseCounter << ": " << answer << endl;
	}
	
	

	
	inFile.close();
	return 0;
}