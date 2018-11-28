//============================================================================
// Name        : SavingTheUniverse.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

class startTable
{
public:
	int start;
	int arrive;
	bool departure; // true for A, false for B

	startTable(char* sTime, char* dTime, bool de, int turn)
	{
		start = atoi(sTime)*60+ atoi(sTime+3);		
		arrive = atoi(dTime)*60 + atoi(dTime+3);
		departure = de;
		setTurnAround(turn);
	}
	bool operator <(const startTable &T) const 
	{
		return (start<T.start);
	}
	startTable(const startTable &T)
	{
			start= T.start;
			arrive = T.arrive;
			departure = T.departure;
	}
	
	void operator =(const startTable &T)
	{
		start= T.start;
		arrive = T.arrive;
		departure = T.departure;
	}

	void setTurnAround(int t)
	{
		arrive+=t;
	}
	void print() const
	{
		cout<<start/60<<":"<<start%60<<" "<<arrive/60<<":"<<arrive%60<<" "<<departure<<endl;
	}
};

class arriveTable
{
public:
	int start;
	int arrive;

	arriveTable(int s, int a)
	{
		start = s;		
		arrive = a;
	}
	
	bool operator <(const arriveTable &T) const 
	{
		return (arrive<T.arrive);
	}
	void print() const
	{
		cout<<start/60<<":"<<start%60<<" "<<arrive/60<<":"<<arrive%60<<endl;
	}
};



int main() {
	ifstream fin;
	ofstream fout;
	fout.open("output.txt");
	fin.open("sample3.txt");
	int n;
	fin>>n;
	
	for(int i=0;i<n;i++)
	{
		int turnAround, timeA, timeB;
		int startA =0, startB=0;

		fin>>turnAround>>timeA>>timeB;
		multiset<startTable> table;
		
		char temp1[10], temp2[10];
		for(int j =0 ; j<(timeA+timeB);j++)
		{
			fin>>temp1>>temp2;
			temp1[2]='\0';
			temp2[2]='\0';
			if(j<timeA)
				table.insert(startTable(temp1,temp2,true, turnAround));
			else
				table.insert(startTable(temp1,temp2,false, turnAround));
		}
		
//debug
		for(set<startTable>::iterator it = table.begin() ; it != table.end(); it++)
			it->print();

		multiset<arriveTable> queA, queB;
		for(multiset<startTable>::iterator it = table.begin() ; it != table.end(); it++)
		{
			if(it->departure==true)
			{
				if(queA.empty())
				{	//depart new train
					startA++;
					queB.insert(arriveTable(it->start, it->arrive));
				}
				else
				{	
					multiset<arriveTable>::iterator ait = queA.begin();
					if(ait->arrive<=it->start)
					{//depart previously arrived train
						queB.insert(arriveTable(it->start,it->arrive));
						queA.erase(ait);
					}
					else
					{//no train is arrived yet
						startA++;
						queB.insert(arriveTable(it->start, it->arrive));
					}
				}
			}
			else
			{
				if(queB.empty())
				{	//depart new train
					startB++;
					queA.insert(arriveTable(it->start, it->arrive));
				}
				else
				{	
					multiset<arriveTable>::iterator ait = queB.begin();
					if(ait->arrive<=it->start)
					{//depart previously arrived train
						queA.insert(arriveTable(it->start,it->arrive));
						queB.erase(ait);
					}
					else
					{//no train is arrived yet
						startB++;
						queA.insert(arriveTable(it->start, it->arrive));
					}
				}
			}
		}
		
		cout<<"Case #"<<i+1<<": "<<startA<<" "<<startB<<endl;
		fout<<"Case #"<<i+1<<": "<<startA<<" "<<startB<<endl;
		table.clear();
	}	
	
	fout.close();
	fin.close();
	return 0;
}
