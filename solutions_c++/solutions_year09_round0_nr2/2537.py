

// GoogleTest2.cpp : Defines the entry point for the console application.

//



#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <set>
#include <map>

using namespace std;

class Token

{

private:

	friend std::ostream& operator<<(std::ostream&,Token const&);

	friend std::istream& operator>>(std::istream&,Token&);

public:

	std::string     value;

};

std::istream& operator>>(std::istream& str,Token& data)

{

	// Check to make sure the stream is OK.

	if (!str)

	{   return str;

	}



	char    x;

	// Drop leading space

	do

	{

		x = str.get();

	}

	while(str && isspace(x) && (x != '\n'));



	// If the stream is done. exit now.

	if (!str)

	{

		return str;

	}



	// We have skipped all white space up to the

	// start of the first token. We can now modify data.

	data.value  ="";



	// If the token is a '\n' We are finished.

	if (x == '\n')

	{   data.value  = "\n";

	return str;

	}



	// Otherwise read the next token in.

	str.unget();

	str >> data.value;



	return str;

}

std::ostream& operator<<(std::ostream& str,Token const& data)

{

	return str << data.value;

}

struct position

{

	int rowlocation;
	int collocation;
	position():rowlocation(-10),collocation(-10){}

};



struct directionCal

{

	int Value;

	position pos;

};

position CalculateMinPosition(vector<directionCal> Direction)

{

	position posVal;

	int minimum;

	if(Direction.size())

	{

		minimum = Direction[0].Value;

		posVal = Direction[0].pos;

	}

	for(int i=0; i<Direction.size(); ++i)

	{

		if(minimum > Direction[i].Value)

		{

			minimum = Direction[i].Value ;

			posVal = Direction[i].pos;

		}

	}

	return posVal;



}

void FindLink(vector<vector<int>> Val,int Val1,position pos,int m,int n,position& posout)

{

	//	int NorthVal,WestVal,EastVal,SouthVal;

	vector<directionCal> Direction;

	if(pos.rowlocation-1 >= 0 )

	{

		directionCal temp;

		temp.Value = Val[pos.rowlocation -1][pos.collocation];

		temp.pos.rowlocation = pos.rowlocation -1;

		temp.pos.collocation = pos.collocation;

		Direction.push_back(temp);

	}

	if(pos.collocation-1 >= 0)

	{

		directionCal temp;

		temp.Value = Val[pos.rowlocation][pos.collocation-1];

		temp.pos.rowlocation = pos.rowlocation ;

		temp.pos.collocation = pos.collocation-1;

		Direction.push_back(temp);

	}

	if(pos.collocation+1 <n)

	{

		directionCal temp;

		temp.Value = Val[pos.rowlocation][pos.collocation+1];

		temp.pos.rowlocation = pos.rowlocation ;

		temp.pos.collocation = pos.collocation+1;

		Direction.push_back(temp);

	}

	if(pos.rowlocation+1 <m)

	{

		directionCal temp;

		temp.Value = Val[pos.rowlocation+1][pos.collocation];

		temp.pos.rowlocation = pos.rowlocation +1;

		temp.pos.collocation = pos.collocation;

		Direction.push_back(temp);

	}

	posout = CalculateMinPosition(Direction);

	if(posout.rowlocation != -10 && posout.collocation != -10)

	{

		if(Val1 <= Val[posout.rowlocation][posout.collocation])

		{

			posout.rowlocation = -10;

			posout.collocation = -10;

		}

	}



}

void FindLinkedVector(set<int>& positionVal,vector<directionCal> ValData,position pos,int m)
{
	positionVal.insert(pos.rowlocation*m + pos.collocation);
	if(ValData[pos.rowlocation*m + pos.collocation].pos.rowlocation != -10 && ValData[pos.rowlocation*m + pos.collocation].pos.collocation != -10)
	{
		position pos1;
		pos1.rowlocation = ValData[pos.rowlocation*m + pos.collocation].pos.rowlocation;
		pos1.collocation = ValData[pos.rowlocation*m + pos.collocation].pos.collocation;
		FindLinkedVector(positionVal,ValData,pos1,m);
	}
}
void CompareTwoVectors(vector<position>& pos1,vector<position>& pos2)
{
	bool bflag = false;
	for(int i=0; i<pos1.size(); ++i)
	{
		for(int j=0; j<pos2.size(); ++j)
		{
			bool bflaginsert = true;
			if(pos1[i].rowlocation == pos2[j].rowlocation && pos1[i].collocation == pos2[j].collocation)
			{
				bflaginsert = false;
				bflag = true;
			}
			if(bflag == true && bflaginsert)
			{
				pos1.push_back(pos2[j]);
			}
		}
	}
}
int _tmain(int argc, _TCHAR* argv[])

{
	ifstream f("C:\\indrajitdata.txt");
	ofstream fout("C:\\Output.txt");
	Token x;

	vector<vector<int>> arr;
	f>>x;
	if(x.value == "\n")
	{
		f>>x;
	}
	int nCase = atoi(x.value.c_str());
	for(int pcase=0; pcase<nCase; ++pcase)
	{
		int m = 0;
		int n = 0;

		//cin>>m>>n;
		f>>x;
		if(x.value == "\n")
		{
			f>>x;
		}
		m = atoi(x.value.c_str());
		//IntToString(m,x.value);
		f>>x;
		if(x.value == "\n")
		{
			f>>x;
		}
		n = atoi(x.value.c_str());
		//IntToString(n,x.value);

		arr.resize(m);

		for(int i=0; i<m; ++i)

			arr[i].resize(n);

		for(int i=0; i<m; ++i)

		{

			for(int j=0; j<n; ++j)

			{
				f>>x;
				if(x.value == "\n")
				{
					f>>x;
				}
				arr[i][j] = atoi(x.value.c_str());
				//IntToString(arr[i][j],x.value);
				//cin>>arr[i][j];

			}

		}

		vector<directionCal> ValData;

		ValData.resize(m*n);

		for(int i=0; i<m; ++i)

		{

			for(int j=0; j<n; ++j)

			{

				position p;

				p.rowlocation = i;

				p.collocation = j;

				ValData[i*n+j].Value = arr[i][j];

				FindLink(arr,arr[i][j],p,m,n,ValData[i*n+j].pos);

			}

		}

		vector<char> outputChar;

		outputChar.resize(m*n);
		vector<set<int>> OutputPosition;
		for(int i=0 ;i<m; ++i)
		{
			for(int j=0 ;j<n; ++j)
			{
				set<int> positionvector;
				position pos;
				pos.rowlocation = i;
				pos.collocation = j;
				FindLinkedVector(positionvector,ValData,pos,n);
				OutputPosition.push_back(positionvector);
			}
		}
		bool bflag = false;

		for(int i=0; i<OutputPosition.size(); ++i)
		{
			if(bflag)
			{
				i =0;
			}
			bflag = false;
			for(int j=0; j<OutputPosition.size(); ++j)
			{
				if(!bflag)
				{

					if(i != j)
					{
						for(set<int>::iterator it = OutputPosition[j].begin(); it != OutputPosition[j].end(); ++it)
						{
							set<int>::iterator it2 = OutputPosition[i].find(*it);
							if(it2 != OutputPosition[i].end())
							{
								bflag = true;
							}
						}
					}
					if(bflag)
					{
						for(set<int>::iterator it = OutputPosition[j].begin(); it != OutputPosition[j].end(); ++it)
						{
							OutputPosition[i].insert(*it);
						}
						OutputPosition.erase(OutputPosition.begin() + j);
					}
				}
				//CompareTwoVectors(OutputPosition[i],OutputPosition[j]);
			}
		}
		map<int,set<int>> mapVal;
		for(int i=0; i<OutputPosition.size(); ++i)
		{
			mapVal.insert(pair<int,set<int>>(*OutputPosition[i].begin(),OutputPosition[i]));
		}
		char chdata = 'a';
		outputChar.resize(m*n);
		int indx1 = 0;
		for(map<int,set<int>>::iterator it = mapVal.begin(); it != mapVal.end(); ++it)
		{
			for(set<int>::iterator it2 = it->second.begin(); it2 != it->second.end(); ++it2)
				outputChar[*it2] = chdata + indx1;
			indx1++;
		}
		fout<<"Case #"<<pcase+1<<":"<<"\n";
			for(int i=0; i<m; ++i)
			{
				for(int j=0; j<n; ++j)
				{
					fout<<outputChar[i*n+j]<<" ";
				}
				fout<<"\n";
			}
	}
	f.close();
	fout.close();
	return 0;

}
