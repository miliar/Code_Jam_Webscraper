#include <iomanip>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>

using namespace std;

int main()
{
    //char filename[50] = "B-small-attempt5.in.txt";
	char filename[50] = "B-large.in.txt";
	char outputFilename[50] = "B-big.out.txt";

	//24*60 = 1440
	int da[1500], aa[1500], db[1500], ab[1500];
	int count, tr, ta, tb;
	int i, j, k, m;
	char a[10];
	int h, s;
	int ava, aResult=0, bResult=0;

	ofstream ostrm;
	ostrm.open(outputFilename);

	ifstream istrm(filename);	
	istrm >> count;

	for (i=1; i<=count; i++)
	{
		aResult = 0;
		bResult = 0;

		for (j=0; j<1500; j++)
		{
			da[j] = aa[j] = db[j] = ab[j] = 0;
		}

		istrm >> tr >> ta >> tb; 
		if (ta == 0)
		{
            cout << "Case #" << i << ": 0 "  << tb << endl;
			ostrm << "Case #" << i << ": 0"  << tb << endl;
		    continue;
		}

		if (tb == 0)
		{
            cout << "Case #" << i << ": " << ta << " 0" << endl;
			ostrm << "Case #" << i << ": " << ta << " 0" << endl;
		    continue;
		}

		for (j=0; j<ta; j++)
		{
		    istrm >> a; 
			sscanf(a, "%d:%d", &h, &s);
			da[h*60+s] ++;

		    istrm >> a; 
			sscanf(a, "%d:%d", &h, &s);
			ab[h*60+s+tr] ++;
        }

		for (j=0; j<tb; j++)
		{
		    istrm >> a; 
			sscanf(a, "%d:%d", &h, &s);
			db[h*60+s] ++;

		    istrm >> a; 
			sscanf(a, "%d:%d", &h, &s);
			aa[h*60+s+tr] ++;
        }
		
		// check A
        ava = 0;
		while (aa[ava] == 0 && ava<1480)
			ava ++;
		for (j=0; j<1500; j++)
		{
			if (da[j] >0)
			{
				m = da[j];
				for(k=1; k<=m; k++)
				{
					if(j >= ava)
					{
						da[j] --;
						aa[ava] --;
						if (aa[ava] == 0)
						{
						    while (aa[ava] == 0 && ava<1480)
							    ava ++;
						}
					}
				}
			}
		}

		// check B
		ava = 0;
		while (ab[ava] == 0 && ava<1480)
			ava ++;
		for (j=0; j<1500; j++)
		{
			if (db[j] >0)
			{
				m = db[j];
				for(k=1; k<=m; k++)
				{
					if(j >= ava)
					{
						db[j] --;
						ab[ava] --;
						if (ab[ava] == 0)
						{
						    while (ab[ava] == 0 && ava<1480)
							    ava ++;
						}
					}
				}
			}
		}

		// Summary
		for (j=0; j<1500; j++)
		{
			if (da[j] > 0)
				aResult += da[j];
			if (db[j] > 0)
				bResult += db[j];
		}
		cout << "Case #" << i << ": " << aResult << " " << bResult << endl; 
		ostrm << "Case #" << i << ": " << aResult << " " << bResult << endl;
	} 
	return 0;
}