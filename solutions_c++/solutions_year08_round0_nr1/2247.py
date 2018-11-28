#include <fstream>
#include <iostream>
#include <string>
using namespace std; 

void main(void)
{
	bool engineflag[100];
	int engineflagNum = 0;
	int switchNum = 0;

//	char str[100];
	int N = 0;
	int S = 2;
	int Q = 0;
	int i = 0;
	int j = 0;
	int l = 0;
	int m = 0;
	string enginestr[100];
	string queriestr;
	char tmp[100];

	ifstream myinf("c:\\A-large.in");
	ofstream myouf("c:\\A-large.txt");

	myinf >> N;
	for (i=0; i<N; i++)
	{
		myinf >> S;
		myinf.getline(tmp, sizeof(tmp));
		for (j=0; j<S; j++)
		{
			myinf.getline(tmp, sizeof(tmp));
			enginestr[j] = tmp;
			engineflag[j] = false;
		}
		myinf >> Q;
		myinf.getline(tmp, sizeof(tmp));
		for (l=0; l<Q; l++)
		{
			myinf.getline(tmp, sizeof(tmp));
			queriestr = tmp;
			m = 0;
			for (j=0; j<S; j++)
			{
				if ((enginestr[j] == queriestr) && (engineflag[j] == false))
				{
					engineflag[j] = true;
					engineflagNum++;
					m = j;
					break;
				}
			}
			if (engineflagNum == S)
			{
				switchNum++;
				for (j=0; j<S; j++)
				{
					engineflag[j] = false;
				}
				engineflag[m] = true;
				engineflagNum = 1;
			}
		}
		
		myouf << "Case #" << i+1 << ": " << switchNum << endl;
		switchNum = 0;
		engineflagNum = 0;
	}
}