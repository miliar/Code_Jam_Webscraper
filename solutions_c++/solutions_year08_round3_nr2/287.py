// coded by Martin Tillmann for the Google Code Jam 08 contest.

#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>
using namespace std;


void check(string ss,int pos);

int total=0;

int main()
{
string s;
getline(cin ,s);
int cases;
stringstream(s) >> cases;
for(int casecounter=0;casecounter<cases;casecounter++)
	{
	getline(cin,s);
	total=0;
	check(s,0);
	cout << "Case #" << casecounter+1 << ": " << total << "\n";
	}
return 0;
}

void check(string ss,int pos)
{
if(pos>=ss.length()-1) 
	{
	long long int erg=0;
	long long int number=0;
	bool done=false;
	bool plus=true;
	for(int i=0;i<ss.length();i++)
		{
		if(done==false) 
			{
			number=(long long int)atoll(&ss.c_str()[i]);
			done=true;
			}
		else 
			{
			if(ss.c_str()[i]=='+')
				{
				if(plus) erg+=number;
				else erg-=number;
				plus=true;
				done=false;
				}
			else if(ss.c_str()[i]=='-')
				{
				if(plus) erg+=number;
				else erg-=number;
				plus=false;
				done=false;
				}
			}
		}	
	if(plus) erg+=number;
	else erg-=number;
	if((erg%2)==0 || (erg%3)==0 || (erg%5)==0 || (erg%7)==0) {total++; return;}
	else {return;}
	}
else
	{
	check(ss.substr(0,pos+1)+"+"+ss.substr(pos+1,ss.length()),pos+2);
	check(ss.substr(0,pos+1)+"-"+ss.substr(pos+1,ss.length()),pos+2);
	check(ss,pos+1);
	}
}
