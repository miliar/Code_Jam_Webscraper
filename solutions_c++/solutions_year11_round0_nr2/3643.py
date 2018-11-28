#include <iostream>
#include <string>
using namespace std;
int test, qtcom, qtopp, qt;
string s, result;
bool exist[8];
struct obj
{
	char f, s, res;
};
obj com[36];
obj opp[28];

int number(char c)
{
	switch(c)
	{
		case 'Q':return 0;
		case 'W':return 1;
		case 'E':return 2;
		case 'R':return 3;
		case 'A':return 4;
		case 'S':return 5;
		case 'D':return 6;
		case 'F':return 7;
	}
	return 8;
}

void combine(char c2)
{
	//cout << "Combine: ";
	char c1=result[result.size()-1];
	for(int i=0; i<qtcom; i++)
		if((c1==com[i].f && c2==com[i].s) || (c1==com[i].s && c2==com[i].f))
		{
			result[result.size()-1]=com[i].res;
			//cout << "PODMIANA" << endl;
			return;
		}
	result+=c2;
	//cout << "DODANIE" << endl;
}

void update()
{
	for(int i=0; i<8; i++)
				exist[i]=false;
	//cout << "Update: ";
	for(unsigned int i=0; i<result.size(); i++)
		if(number(result[i])<8)
			exist[number(result[i])]=true;
	for(int i=0; i<qtopp; i++)
		if(exist[number(opp[i].f)] && exist[number(opp[i].s)])
		{
			//cout << "CZYSZCZENIE dla " << i << endl;
			result.clear();
			return;
		}
	//cout << endl;
}
 
int main()
{
	cin >> test;
	for(int t=0; t<test; t++)
	{
		cin >> qtcom;
		for(int i=0; i<qtcom; i++)	
		{
			cin >> s;
			com[i].f=s[0];
			com[i].s=s[1];
			com[i].res=s[2];
		}	
		cin >> qtopp;
		for(int i=0; i<qtopp; i++)	
		{
			cin >> s;
			opp[i].f=s[0];
			opp[i].s=s[1];
		}
		cin >> qt;
		cin >> s;
		result=s[0];
		exist[number(s[0])]=true;
		for(unsigned int i=1; i<s.size(); i++)
		{
			//cout << "DODAJEMY: " << s[i] << endl;
			combine(s[i]);
			update();
		}
		cout << "Case #" << t+1 << ": [";
		if(result.size()>0)cout << result[0];
		for(unsigned int i=1; i<result.size(); i++)
			cout << ", " << result[i];
		cout << "]" << endl;
		result.clear();
	}
	
	
	return 0;
}
