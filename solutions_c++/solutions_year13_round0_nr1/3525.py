

#include<iostream>
#include <string>
#include <bitset>
#include <limits>
#include<math.h>
#include<cmath>
#include<fstream>
#include<bitset>
#include<vector>
#include <sstream>
#include<algorithm>
#include<time.h>
#include<set>
#include<map>
#include <numeric>
//#include "Source.cpp"
using namespace std;


string check(vector<string> cases)
{
	bool row[4]={false};
	bool col[4]={false};
	string Result;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			//check col;
			if(!col[i])
			{int Xcount=0;
					int Ocount=0;
						int c=i;
					int d=0;
						bool T=false;
				for (int k = 0; k < 4; k++)
				{
					if(cases[c][d]=='X')
						Xcount++;
					if(cases[c][d]=='O')
						Ocount++;
					if(cases[c][d]=='T')
						T=true;
					d++;
						if((Xcount==3&&T==true)||Xcount>3)
					return "X won";
			
				if((Ocount==3&&T==true)||Ocount>3)
					return "O won";
				}
				col[i]=true;
			}

			//check row
			if(!row[j])
			{
				int c=0;
					int d=j;
					int Xcount=0;
					int Ocount=0;
					bool T=false;
				for (int i = 0; i < 4; i++)
				{
					
				if(cases[c][d]=='X')
						Xcount++;
					if(cases[c][d]=='O')
						Ocount++;
					if(cases[c][d]=='T')
						T=true;
					c++;
						if((Xcount==3&&T==true)||Xcount>3)
					return "X won";
			
				if((Ocount==3&&T==true)||Ocount>3)
					return "O won";
				}
				row[j]=true;
			}


			//check diagonal 1 
			if(i==0&&j==0)
			{
				int Xcount=0;
				int Ocount=0;
				bool T=false;
				int c=0;
				for (int k = 0; k < 4; k++)
				{
					if(cases[c][c]=='X')
						Xcount++;
					if(cases[c][c]=='O')
						Ocount++;
					if(cases[c][c]=='T')
						T=true;
					c++;
				}
				if((Xcount==3&&T==true)||Xcount>3)
					return "X won";
			
				if((Ocount==3&&T==true)||Ocount>3)
					return "O won";
			}
			//check diagonal 2 
				if(i==3&&j==0)
			{
				int Xcount=0;
				int Ocount=0;
				bool T=false;
				int c=3;
				int d=0;
				for (int k = 0; k < 4; k++)
				{
					if(cases[c][d]=='X')
						Xcount++;
					if(cases[c][d]=='O')
						Ocount++;
					if(cases[c][d]=='T')
						T=true;
					c--;
					d++;

				}
				if(Xcount==3&&T==true)
					return "X won";
				if((Xcount==3&&T==true)||Xcount>3)
					return "X won";
			
				if((Ocount==3&&T==true)||Ocount>3)
					return "O won";
			}
				//check diagonal 3
				if(i==0&&j==3)
			{
				int Xcount=0;
				int Ocount=0;
				bool T=false;
				int c=0;
				int d=3;
				for (int k = 0; k < 4; k++)
				{
					if(cases[c][d]=='X')
						Xcount++;
					if(cases[c][d]=='O')
						Ocount++;
					if(cases[c][d]=='T')
						T=true;
					c++;
					d--;
				}
				if((Xcount==3&&T==true)||Xcount>3)
					return "X won";
			
				if((Ocount==3&&T==true)||Ocount>3)
					return "O won";
			}
			//check diagonal 4 
			if(i==3&&j==0)
			{
				int Xcount=0;
				int Ocount=0;
				bool T=false;
				int c=3;
				int d=0;
				for (int k = 0; k < 4; k++)
				{
					if(cases[c][d]=='X')
						Xcount++;
					if(cases[c][d]=='O')
						Ocount++;
					if(cases[c][d]=='T')
						T=true;
					c--;
					d++;
				}
				if((Xcount==3&&T==true)||Xcount>3)
					return "X won";
			
				if((Ocount==3&&T==true)||Ocount>3)
					return "O won";
			}

		}
	}

	
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if(cases[i][j]=='.')
			{
				return  "Game has not completed";
			}
		}

	}
	
		return "Draw";
	
}

int main()
{





	int Testcase;
	
	 string STRING;
	ifstream infile;
	infile.open ("A-large.in");
	ofstream Result;
Result.open("Result.txt");
string Test;

getline(infile,Test);
stringstream t(Test);
t>>Testcase;

cout<<"Test cases "<<Testcase<<endl;
string Case;
vector<string>sample;


for (int i = 0; i < Testcase; i++)
{
	int x=i;
	for (int j = 0; j < 4; j++)
	{
		 getline(infile,STRING);
		if(STRING!="")
		{
			sample.push_back(STRING);
			Case+=STRING;
		}
		
	
	}
	 getline(infile,STRING);
	// cout<<"Case #"<<++x<<":"<<check(sample)<<endl;
	 Result<<"Case #"<<++x<<": "<<check(sample)<<endl;
	sample.clear();
	//	cout<<Case;
	Case="";
	
	
}

	  infile.close();
	  Result.close();
	return 0;

}