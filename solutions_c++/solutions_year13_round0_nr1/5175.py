// GoogleCodejam_2013_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "string"

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		
		char b[5][5];
		for (int j = 0; j < 4; j++)
		{
			cin>>b[j];
		}
		cout<<"Case #"<<i+1<<": "; 
		int find =false;
		for (int j = 0; j < 4 && !find; j++)
		{
			find = true;
			if(strcmp(b[j] , "OOOO" )==0)
				cout<<"O won";
			else if(strcmp(b[j] , "TOOO" )==0)
				cout<<"O won";
			else if(strcmp(b[j] , "OTOO" )==0)
				cout<<"O won";

			else if(strcmp(b[j] , "OOTO" )==0)
				cout<<"O won";
			else if(strcmp(b[j] , "OOOT" )==0)
				cout<<"O won";
			else if(strcmp(b[j] , "XXXX" )==0)
				cout<<"X won";
			else if(strcmp(b[j] , "TXXX" )==0)
				cout<<"X won";
			else if(strcmp(b[j] , "XTXX" )==0)
				cout<<"X won";
			else if(strcmp(b[j] , "XXTX" )==0)
				cout<<"X won";
			else if(strcmp(b[j] , "XXXT" )==0)
				cout<<"X won";


			else 
				find =false;
		}

		for (int j = 0; j < 4 &&!find; j++)
		{
			char temp[5];
			temp[0] = b[0][j];
			temp[1] = b[1][j];
			temp[2] = b[2][j];
			temp[3] = b[3][j];
			temp[4] = 0;

			find = true;
			if(strcmp(temp , "OOOO" )==0)
				cout<<"O won";
			else if(strcmp(temp , "TOOO" )==0)
				cout<<"O won";
			else if(strcmp(temp , "OTOO" )==0)
				cout<<"O won";

			else if(strcmp(temp , "OOTO" )==0)
				cout<<"O won";
			else if(strcmp(temp , "OOOT" )==0)
				cout<<"O won";
			else if(strcmp(temp , "XXXX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "TXXX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "XTXX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "XXTX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "XXXT" )==0)
				cout<<"X won";

			else 
				find =false;
		}

		if(!find)
		{
			char temp[5];
			temp[0] = b[0][0];
			temp[1] = b[1][1];
			temp[2] = b[2][2];
			temp[3] = b[3][3];
			temp[4] = 0;

			find = true;
			if(strcmp(temp , "OOOO" )==0)
				cout<<"O won";
			else if(strcmp(temp , "TOOO" )==0)
				cout<<"O won";
			else if(strcmp(temp , "OTOO" )==0)
				cout<<"O won";

			else if(strcmp(temp , "OOTO" )==0)
				cout<<"O won";
			else if(strcmp(temp , "OOOT" )==0)
				cout<<"O won";
			else if(strcmp(temp , "XXXX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "TXXX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "XTXX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "XXTX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "XXXT" )==0)
				cout<<"X won";

			else 
				find =false;
		}

		if(!find)
		{
			char temp[5];
			temp[0] = b[3][0];
			temp[1] = b[2][1];
			temp[2] = b[1][2];
			temp[3] = b[0][3];
			temp[4] = 0;

			find = true;
			if(strcmp(temp , "OOOO" )==0)
				cout<<"O won";
			else if(strcmp(temp , "TOOO" )==0)
				cout<<"O won";
			else if(strcmp(temp , "OTOO" )==0)
				cout<<"O won";

			else if(strcmp(temp , "OOTO" )==0)
				cout<<"O won";
			else if(strcmp(temp , "OOOT" )==0)
				cout<<"O won";
			else if(strcmp(temp , "XXXX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "TXXX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "XTXX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "XXTX" )==0)
				cout<<"X won";
			else if(strcmp(temp , "XXXT" )==0)
				cout<<"X won";

			else 
				find =false;
		}

		for (int j = 0; j < 4 && !find; j++)
		{
			for (int k = 0; k < 4 && !find; k++)
			{
				if(b[j][k] =='.')
				{
					find = true;
					cout<<"Game has not completed";
				}
			}
		}

		if(!find)
			cout<<"Draw";

		cout<<"\n";
	}
	return 0;
}

