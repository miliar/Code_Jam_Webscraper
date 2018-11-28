#include <iostream>
#include <string>
#include <fstream>
using namespace std;

const int MSN = 102;
const int MQN = 1002;

const int MCN = 101;



int main()
{
	
	ifstream inf("A-large.in");
	ofstream outf("A-large.txt");

	int i = 0, j = 0, k = 0;
	int testNumber = 0;
	inf>>testNumber;
	
	
	int sn = 0, qn = 0;
	
	string ss[MSN];
	string qs[MQN];
	int hit[MSN] = {0};
	int hitCount = 0;
	int switchN = 0;
	for( k = 0; k < testNumber; k++)
	{
		inf>>sn;
		inf.get();
		for ( i = 0; i < sn; i++ )
		{
			getline(inf,ss[i]);
		}
		inf>>qn;
		inf.get();
		for ( j = 0; j < qn; j++ )
		{
			getline(inf,qs[j]);
		}
		
		for ( j = 0; j < qn; j++ )
		{
			for ( i = 0; i < sn; i++ )
			{
				if (qs[j] == ss[i])
				{
					if (hit[i] == 0)
					{
						hit[i] = 1;
						hitCount++;
						if (hitCount == sn)
						{
							switchN++;
							j--;
							memset(hit, 0, MSN*sizeof(int));
							hitCount = 0;
						}//if
						break;
					}//if
				}//if
			}//for
		}//for
		outf<<"Case #"<<k+1<<": "<<switchN<<"\n";
		memset(hit, 0, MSN*sizeof(int));
		switchN = 0;
		hitCount = 0;
	}
	return 0;
}
