#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <math.h>
#include <stdlib.h>
#include <tchar.h>
using namespace std;

#define MaxSpace		5000

unsigned int nTotalTestCase;
list<long long> availableFreq;
list<long long>::iterator availableFreqIndex;
list<long long>::iterator availableFreqIndextmp;

bool isHarmony(long long a, long long b);
long long atoll(const char *ca );

void main(void)
{
	ifstream inFile;
	ofstream outFile;
	char temp[MaxSpace];
	unsigned int spacePos;
	string tmp1, tmp2;

	unsigned int NPlayer;
	long long LHerts, HHerts;
	static long long playerHerts[1000];
	char *result;


	inFile.open("C-small-attempt0.in");
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
		NPlayer = (unsigned int)atoi(tmp1.c_str());

		spacePos = tmp2.find(' ');
		tmp1 = tmp2.substr(0, spacePos);
		tmp2 = tmp2.substr(spacePos+1, t.length() - 1);
		LHerts = atoll(tmp1.c_str());
		HHerts = atoll(tmp2.c_str());

		inFile.getline(temp, MaxSpace);
		t = temp;
		for (unsigned int k = 1;k < NPlayer; k++)
		{
			spacePos = t.find(' ');
			tmp1 = t.substr(0, spacePos);
			t = t.substr(spacePos+1, t.length() - 1);
			playerHerts[k-1] = atoll(tmp1.c_str());

		}
		playerHerts[NPlayer-1] =  atoll(t.c_str());
		/////////////////////////////calculate
		availableFreq.clear();
		for (long long k=LHerts; k<=HHerts;k++)
		{
			if ( isHarmony(k, playerHerts[0]))
			{
				availableFreq.push_back(k);
			}
		}

		for (unsigned int k=1;k<NPlayer;k++)
		{
			for (availableFreqIndex = availableFreq.begin();availableFreqIndex !=availableFreq.end();)
			{
				if ( !isHarmony(playerHerts[k], *availableFreqIndex))
				{
					availableFreqIndextmp = availableFreqIndex;
					availableFreqIndex++;
					availableFreq.erase(availableFreqIndextmp);
				}
				else
				{
					availableFreqIndex++;
				}
			}
			if (availableFreq.size() == 0)
			{
				result = "NO";
				break;
			}
		}
		
		if (availableFreq.size()>0)
		{
			_itoa_s(i+1, temp, 10);
		}

		/////////////////////////
		//Display
		tmp1 ="Case #";
		_itoa_s(i+1, temp, 10);
		tmp1 += temp;
		tmp1 += ": ";

		if (availableFreq.size()>0)
		{
	//		long long lltmp = availableFreq.front();
	//		_i64tot(lltmp,temp, 0);
	//		string lltmp(availableFreq.pop_front());
			sprintf(temp, "%lld", (long long)availableFreq.front());
			tmp1+=temp;
		}
		else
		{
			tmp1+="NO";
		}

		tmp1+= "\n";
		outFile.write(tmp1.c_str(), tmp1.length());

	}
	inFile.close();
	outFile.close();
}


bool isHarmony(long long a, long long b)
{
	if ((a%b ==0 )||(b%a ==0))
	{
		return true;
	}
	else 
		return false;
}

long long atoll(const char *ca )
{
	long long ig=0;
	int       sign=1;
	/* test for prefixing white space */
	while (*ca == ' ' || *ca == '\t' ) 
		ca++;
	/* Check sign entered or no */
	if ( *ca == '-' )       
		sign = -1;
	/* convert string to int */
	while (*ca != '\0')
		if (*ca >= '0' && *ca <= '9')
			ig = ig * 10LL + *ca++ - '0';
		else
			ca++;
	return (ig*(long long)sign);
}