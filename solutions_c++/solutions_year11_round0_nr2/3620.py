// Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

char Combination(vector<string> combinations, string str)
{
	char found=0;
	string rev="";
	rev+=str.at(1);
	rev+=str.at(0);
	for(int i=0;(i<combinations.size())&&(found==0);i++)
	{
		if(combinations.at(i).substr(0,2).compare(str)==0) found=combinations.at(i).at(2);
		else if(combinations.at(i).substr(0,2).compare(rev)==0) found=combinations.at(i).at(2);

	}
	return found;
}

char Combination(vector<string> combinations, char c1, char c2)
{
	char found=0;
	string rev="", str="";
	str+=c1;
	str+=c2;
	rev+=str.at(1);
	rev+=str.at(0);
	for(int i=0;(i<combinations.size())&&(found==0);i++)
	{
		if(combinations.at(i).substr(0,2).compare(str)==0) found=combinations.at(i).at(2);
		else if(combinations.at(i).substr(0,2).compare(rev)==0) found=combinations.at(i).at(2);

	}
	return found;
}


bool Opposite(vector<string> oposites, string str)
{
	bool found=false;
	string rev="";
	rev+=str.at(1);
	rev+=str.at(0);


	for(int i=0;(i<oposites.size())&&(found==false);i++)
	{
		if(oposites.at(i).substr(0,2).compare(str)==0) found=true;
		else if(oposites.at(i).substr(0,2).compare(rev)==0) found=true;
	}


	return found;
}

bool Opposite(vector<string> oposites, char c1, char c2)
{
	bool found=false;
	string rev="", str="";
	str+=c1;
	str+=c2;
	rev+=str.at(1);
	rev+=str.at(0);


	for(int i=0;(i<oposites.size())&&(found==false);i++)
	{
		if(oposites.at(i).substr(0,2).compare(str)==0) found=true;
		else if(oposites.at(i).substr(0,2).compare(rev)==0) found=true;
	}


	return found;
}


int _tmain(int argc, _TCHAR* argv[])
{
	
	ifstream mag_in;
    mag_in.open("B-large.in");

	ofstream mag_out;
    mag_out.open("mag.rez");
	

	int N, Ni, C, D;
	string magic, temp;
	char comb;
	

	

	mag_in >> N;
	for(int i=0;i<N;i++)
	{

		
		
		mag_in >> C;
		vector<string> combines;
		for(int j=0;j<C;j++)
		{
			mag_in >> temp;
			//cout<<temp<<endl;
			combines.push_back(temp);
		}
		//cout<<"C"<<C<<endl;

		mag_in >> D;
		vector<string> opposites;
		for(int j=0;j<D;j++)
		{	
			mag_in >> temp;
			//cout<<temp<<endl;
			opposites.push_back(temp);
		}


		//cout<<"D"<<D<<endl;

		mag_in >> Ni >>magic;

		vector<char> output;
		
		output.push_back(magic.at(0));
		for(int j=1;j<Ni;j++)
		{
			/*
			//check oposites
			if(Opposite(opposites, magic.substr(j,2)))
			{
				if(j<Ni-2)//check to not go out of bound
				{
					comb=Combination(combines, magic.substr(j+1,2));
					if(comb==0) {output.clear(); j++;} 
					else
					{
						output.push_back(magic.at(j));
						output.push_back(comb);
						j+=2;
					}
				}
			}
			//check combinations
			else
			{
				comb=Combination(combines, magic.substr(j,2));
				if(comb==0) output.push_back(magic.at(j));
				else
				{
					output.push_back(comb);
					j++;
				}
			}

			if(j==Ni-2) output.push_back(magic.at(j+1));
			*/

			
			output.push_back(magic.at(j));
			if(output.size()>1)
			{
				comb=Combination(combines, output.at(output.size()-1), output.at(output.size()-2));
				if(comb!=0)
				{
				
				
					output.at(output.size()-2)=comb;
					output.pop_back();
				
				}
				else
				{
					for(int k=0;k<output.size();k++)
					{
						if(Opposite(opposites, output.at(k), output.at(output.size()-1)))
						{
							output.clear();
							break;
						}
					}
				}
			}
		}
		
		mag_out << "Case #"<<i+1<<": [";

		if(output.size()>=1)
		{
			for(int k=0;k<output.size();k++) 
			{
				
				mag_out<<output.at(k);
				if(k!=output.size()-1) mag_out<<", ";

			
			}

			//if(output.size()>1) mag_out<<output.at(output.size()-1);
		}
		mag_out<<"]"<<endl;

	}





	

	
	
	
	mag_in.close();
	mag_out.close();
	return 0;
}

