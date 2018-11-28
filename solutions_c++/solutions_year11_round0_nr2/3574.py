#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <math.h>
using namespace std;

#define MaxSpace		5000

unsigned int nTotalTestCase;

typedef struct Comb
{
	char S1; //source 1
	char S2;
	char D;		//destination
}Comb;
unsigned int CombNum;
Comb CombArray[40];

typedef struct Oppo
{
	char o;
	char p;
}Oppo;
unsigned int OppoNum;
Oppo OppoArray[30];

unsigned int TargetStringLen;
string TargetString;
char ResString[105];

char element[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

list<char> resList;

string Calculate();
bool isElement(char C);
void CheckComp();
void CheckOppo();


int main(void)
{
	ifstream inFile;
	ofstream outFile;
	char temp[MaxSpace];
	unsigned int spacePos;
	string tmp1, tmp2;

	inFile.open("B-large.in");
	outFile.open("B-large.out");

	inFile.getline(temp, MaxSpace);
	nTotalTestCase = atoi(temp);

	for (unsigned int i = 0;i < nTotalTestCase; i++)
	{
		inFile.getline(temp, MaxSpace);
		string t(temp);

		spacePos = t.find(' ');
		tmp1 = t.substr(0, spacePos);
		tmp2 = t.substr(spacePos+1, t.length() - 1);
		CombNum = atoi(tmp1.c_str());
		for (unsigned int k=0;k<CombNum;k++)
		{
			spacePos = tmp2.find(' ');
			tmp1 = tmp2.substr(0, spacePos);
			tmp2 = tmp2.substr(spacePos+1, tmp2.length() - 1);

			CombArray[k].S1 = tmp1[0];
			CombArray[k].S2 = tmp1[1];
			CombArray[k].D = tmp1[2];
		}
		spacePos = tmp2.find(' ');
		tmp1 = tmp2.substr(0, spacePos);
		tmp2 = tmp2.substr(spacePos+1, tmp2.length() - 1);
		OppoNum = atoi(tmp1.c_str());
		for (unsigned int k=0;k<OppoNum;k++)
		{
			spacePos = tmp2.find(' ');
			tmp1 = tmp2.substr(0, spacePos);
			tmp2 = tmp2.substr(spacePos+1, tmp2.length() - 1);

			OppoArray[k].o = tmp1[0];
			OppoArray[k].p = tmp1[1];
		}
		spacePos = tmp2.find(' ');
		tmp1 = tmp2.substr(0, spacePos);
		tmp2 = tmp2.substr(spacePos+1, tmp2.length() - 1);
		
		TargetStringLen = atoi(tmp1.c_str());
		TargetString = tmp2;
//////////////////////////////////////////////////////////////////////////
		//Display
		tmp1 ="Case #";
		itoa(i+1, temp, 10);
		tmp1 += temp;
		tmp1 += ": ";
		tmp1 += Calculate();
		tmp1+= "\n";
		outFile.write(tmp1.c_str(), tmp1.length());

	}


	inFile.close();
	outFile.close();
	return 1;
}

string Calculate()
{
	string result;
//	char *tmp = TargetString.c_str();
	char temp[2];
	temp[1]=0;
	unsigned int i;

	for (i=0;i<TargetString.size();i++)
	{
		resList.push_back(TargetString.c_str()[i]);
		if (resList.size()>1)
		{
			CheckComp();
			CheckOppo();
		}

	}

	result = "[";
	while (resList.size()>0)
	{
		temp[0] = resList.front();
		resList.pop_front();
		result+=temp;
		result+=", ";
	}
	if (result.length()>1)
	{
		result = result.substr(0,result.length()-2);
	}
	
		result+="]";


	return result;
}

void CheckComp()
{
	char L1,L2, LL1, LL2;
	list<char>::iterator it;
	for (unsigned int i=0;i<CombNum;i++)
	{
		if (resList.size()>1)
		{
			it = resList.end();
			it--;
			LL1 = *it;
			it--;
			LL2 = *it;

			if (((LL1 == CombArray[i].S1) && (LL2 == CombArray[i].S2))
				|| ( (LL1 == CombArray[i].S2)  && (LL2 == CombArray[i].S1)))
			{
				resList.pop_back();
				resList.pop_back();
				resList.push_back(CombArray[i].D);
			}
		}
		
	}
}
void CheckOppo()
{
	 int pos1, pos2;
	list<char>::iterator it;
	string tmp;
	char temp[2];
	temp[1]=0;
	

	while (resList.size()>0)
	{
		temp[0] = resList.front();
		resList.pop_front();
		tmp+=temp;
	}

	for (unsigned int i=0;i<OppoNum;i++)
	{
		pos1 = tmp.find(OppoArray[i].o);
		pos2 = tmp.find(OppoArray[i].p);
		if (pos1>=0 && pos2 >=0)
		{

			// maybe there are multiple options.

// 			if (pos1 >pos2)
// 			{
// 				pos2 = tmp.find_last_of(OppoArray[i].p);
// 				tmp = tmp.substr(0,pos2)+tmp.substr(pos1+1, tmp.length()-1);
// 			}
// 			else
// 			{
// 				pos1 = tmp.find_last_of(OppoArray[i].o);
// 				tmp = tmp.substr(0,pos1)+tmp.substr(pos2+1, tmp.length()-1);
// 			}
			tmp ="";
		}
	}
	for (unsigned int i=0;i<tmp.length();i++)
	{
		resList.push_back(tmp.c_str()[i]);
	}

}

bool isElement(char C)
{
	for (unsigned int i=0;i<8;i++)
	{
		if (C == element[i])
		{
			return true;
		}
	}
	return false;
}