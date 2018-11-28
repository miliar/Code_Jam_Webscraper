/*
Author: Cheng Li
Language: C++
IDE: Visual Studio C++ 2008
* 
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

const int HEIGHT=100;
const int WIDTH=100;

struct node
{
	int altitudes;
	//int group;
	bool sink;
	char basin;

public:
	node(): basin('!'){};
};


node M[HEIGHT][WIDTH];

void resetM( int H, int W)
{
for(int i=0; i< H; ++i)
	{
		for(int j=0; j< W; ++j)
		{
			M[i][j].sink = false;
			M[i][j].basin ='!';
		}
	}
}

bool isAllSet( int H, int W)
{

	for(int i=0; i< H; ++i)
	{
		for(int j=0; j< W; ++j)
		{
			if(M[i][j].basin == '!')
				return false;
		}
	}
	return true;
}

void reOrder( int H, int W)
{
	map<char, char> map_char;
	char c='a';
	for(int i=0; i< H; ++i)
	{
		for(int j=0; j< W; ++j)
		{
			char temp = M[i][j].basin;
			if(map_char.count(temp)==0)
			{
				map_char[temp] = c;
				++c;
			}
		}
	}

	for(int i=0; i< H; ++i)
	{
		for(int j=0; j< W; ++j)
		{
			char old = M[i][j].basin;
			char newChar= map_char[old];
			M[i][j].basin = newChar;
		}
	}

}

int main(void)
{
	string InFileName="B-large.in";
	string OutFileName="B-large.out";

	ifstream fin;
	ofstream fout;

	//open input file
	fin.open(InFileName.c_str(), ios::in);
	if(fin.fail())
	{
		std::cerr<<"Input file open error!";
	}

	//create output file
	fout.open(OutFileName.c_str(), ios::out);	
	if(fout.fail())
	{
		std::cerr<<"Output file open error!";
	}

	int caseNum=0;
	int caseCount=1;
	fin>>caseNum;

	while(caseCount<=caseNum)//for case loop
	{
		if(caseCount==2)
			int debug= caseCount;
		//int switchCount=0;

		/*	vector<string> engine_vec;
		vector<string> keys_vec;*/
		vector<pair<int, int>> vec_sink;

		string strTemp;
		fin.ignore(1,'\n');

		int H=0;
		int W=0;

		fin>>H>>W;

		resetM(H, W);

		for(int i=0; i< H; ++i)
		{
			fin.ignore(1,'\n');
			for(int j=0; j< W; ++j)
				fin>>M[i][j].altitudes;
		}

		//Step1: Find sinks
		for(int i=0; i< H; ++i)
		{
			for(int j=0; j< W; ++j)
			{
				int x,y;
				bool flagN=true;
				bool flagW=true;
				bool flagE=true;
				bool flagS=true;

				//north
				x=i-1, y=j;

				if(x>=0)
				{
					flagN = M[i][j].altitudes <= M[x][y].altitudes; 				
				}

				//west
				x=i, y=j-1;
				if(y>=0)
				{
					flagW = M[i][j].altitudes <= M[x][y].altitudes; 				
				}			

				//east
				x=i, y=j+1;
				if(y<W)
				{
					flagE = M[i][j].altitudes <= M[x][y].altitudes; 				
				}	
				//south
				x=i+1, y=j;
				if(x<H)
				{
					flagS = M[i][j].altitudes <= M[x][y].altitudes; 				
				}

				//is sink
				if(flagN && flagW && flagE && flagS)
				{
					M[i][j].sink =true;
					vec_sink.push_back(make_pair(i, j));	
				}
				else// not sink
				{
					M[i][j].sink =false;
				}
			}
		}

		//Step 2: Assign character for sinks
		//map<pair<int, int>, char> map_Letter;
		char c='a';
		vector<pair<int, int>>::iterator iter= vec_sink.begin();
		for(; iter!=vec_sink.end();++iter)
		{
			int i= iter->first;
			int j= iter->second;

			if(c=='n')
				char a=c;

			M[i][j].basin = c;
			//map_Letter[make_pair(i, j)]= c;

			++c;
		}


		//Step 4: Scan until all set
		while(!isAllSet(H, W))
		{
			for(int i=0; i< H; ++i)
			{
				for(int j=0; j< W; ++j)
				{
					if(M[i][j].basin != '!')
						continue;
					else
					{
						if(i==1 && 2==8)
							int debug=i;

						int self= M[i][j].altitudes;
						//find the smallest number
						int smallest =self;
						int x,y;
						if(i-1>=0)
						{
							int n= M[i-1][j].altitudes;
							if(n<smallest)
							{
								smallest = n;
								x=i-1;
								y=j;
							}
						}
						if(j-1>=0)
						{
							int w= M[i][j-1].altitudes;
							if(w<smallest)
							{
								smallest = w;
								x=i;
								y=j-1;
							}
						}
						if(j+1<W)
						{
							int e= M[i][j+1].altitudes;						
							if(e<smallest)
							{
								smallest = e;
								x=i;
								y=j+1;
							}
						}
						if(i+1<H)
						{
							int s= M[i+1][j].altitudes;
							if(s<smallest)
							{
								smallest = s;
								x=i+1;
								y=j;
							}
						}
						
						if(M[x][y].basin!='!')
							M[i][j].basin= M[x][y].basin;
					}
				}
			}
		}

		//Step 5: reOrder all the characters following lexicographically 
		reOrder( H, W);

		//for test
		cout<<"Case #"<<caseCount<<": "<<endl;
		for(int i=0; i< H; ++i)
		{

			for(int j=0; j< W; ++j)
			{
				cout<<M[i][j].basin<<" ";
			}
			cout<<endl;
		}

		fout<<"Case #"<<caseCount++<<": "<<'\n';		
		for(int i=0; i< H; ++i)
		{

			for(int j=0; j< W; ++j)
			{
				fout<<M[i][j].basin<<" ";
			}
			fout<<'\n';
		}
	}


	//close input file& output file
	fin.close();
	fout.close();

	return 1;
}