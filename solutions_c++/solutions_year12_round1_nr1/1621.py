#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;


int main ()
{
	ifstream cin;
	cin.open("A-small-attempt0.in");
	ofstream cout;
	cout.open("password_small.out");

	int T, A, B;
	double p[5];
	double choices[10][15];

	cin>>T;

	for (int t=1; t<=T; t++)
	{
		cin>>A>>B;

		for (int i=0; i<A; i++)
			cin>>p[i];

		if (A==3)
		{
			choices[0][0]=p[0]*p[1]*p[2];
			choices[0][1]=p[0]*p[1]*(1-p[2]);
			choices[0][2]=p[0]*(1-p[1])*p[2];	
			choices[0][3]=(1-p[0])*p[1]*p[2];
			choices[0][4]=p[0]*(1-p[1])*(1-p[2]);
			choices[0][5]=(1-p[0])*p[1]*(1-p[2]);
			choices[0][6]=(1-p[0])*(1-p[1])*p[2];
			choices[0][7]=(1-p[0])*(1-p[1])*(1-p[2]);

			choices[1][0] = 1 + B-A;
			for (int i=1; i<8; i++)
				choices[1][i]= 1 + B-A + B + 1;

			choices[2][0] = choices[2][1] = 1 + B-(A-1) + 1;
			for (int i=2; i<8; i++)
				choices[2][i] = 1 + B-(A-1) + 1 +B + 1;

			choices[3][0]=choices[3][1]=choices[3][2]=choices[3][4]= 2 + B-(A-2) + 1;
			choices[3][3]=choices[3][5]=choices[3][6]=choices[3][7]= 2 + B-(A-2) + 1 + B +1;

			for (int i=0; i<8; i++)
				choices[4][i] = 3 + B + 1;

			for (int i=0; i<8; i++)
				choices[5][i] = 1 + B +1 ;


			for (int i=1; i<6; i++)
			{
				double exp=0;
				for (int j=0; j<8; j++)
				{
					exp+= choices[0][j]*choices[i][j];
				}
				choices[i][8]=exp;
			}

			double min = 1000000000;
			for (int i=1; i<6;i++)
				if(choices[i][8]<min)
					min=choices[i][8];
			cout<<fixed<<setprecision(6);
			cout<<"Case #"<<t<<": "<<min<<endl;

		}

		if (A==2)
		{
			choices[0][0]=p[0]*p[1];
			choices[0][1]=p[0]*(1-p[1]);
			choices[0][2]=(1-p[0])*p[1];
			choices[0][3]=(1-p[0])*(1-p[1]);

			choices[1][0] = 1 + B-A;
			for (int i=1;i<4;i++)
				choices[1][i] = 1 + B-A +B +1;

			choices[2][0]=choices[2][1]=1 + B-(A-1) + 1;
			choices[2][2]=choices[2][3]=1 + B-(A-1) + 1 +B +1;

			for(int i=0;i<4;i++)
				choices[3][i]=2 + B + 1;

			for(int i=0; i<4;i++)
				choices[4][i] = 1 + B + 1;


			for (int i=1;i<5;i++)
			{
				double exp=0;
				for (int j=0; j<4; j++)
				{
					exp+=choices[0][j]*choices[i][j];
				}
				choices[i][4]=exp;
			}

			double min=1000000000;
			for(int i=1; i<5; i++)
				if(choices[i][4]<min)
					min=choices[i][4];
			cout<<fixed<<setprecision(6);
			cout<<"Case #"<<t<<": "<<min<<endl;
		}

		if (A==1)
		{
			choices[0][0]=p[0];
			choices[0][1]=(1-p[0]);

			choices[1][0]= B-A + 1;
			choices[1][1]= B-A +1 + B+1;

			choices[2][0]=choices[2][1]=1 + B + 1;

			choices[3][0]=choices[3][1]=1+ B + 1;

			for(int i=1;i<4;i++)
			{
				double exp=0;
				for (int j=0;j<2;j++)
				{
					exp+=choices[0][j]*choices[i][j];
				}
				choices[i][2]=exp;
			}

			double min=1000000000;
			for (int i=1; i<4; i++)
				if (choices[i][2]<min)
					min=choices[i][2];
			cout<<fixed<<setprecision(6);
			cout<<"Case #"<<t<<": "<<min<<endl;

		}


	}

	return 0;
}