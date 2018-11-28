# include <iostream>
# include <fstream>
using namespace std;

void sort (int *a, int n)
   {int pass, j, tmp;
    bool xchange = true;
    for (pass = 1; pass < n && xchange == true; pass++)
    { xchange = false;
      for (j=0; j < n - pass; j++)
      { if (a[j] > a[j+1])
        { tmp = a[j]; a[j] = a[j+1]; a[j+1] = tmp;
          xchange = true;
        } /* end of if */
      } /* end of inner for loop */
    } /* end of outer for loop */
   } /* end of bubble sort */


int main()
{int NoOfTestCases;
ifstream fin("test.input", ios::in);
fin >> NoOfTestCases;
for (int i=1; i<=NoOfTestCases; i++)
	{int TurnTime;
	fin >> TurnTime;
	int NA, NB;
	fin >> NA >> NB;
	int DepartFromA[NA];
	int ArriveAtA[NB];
	int DepartFromB[NB];
	int ArriveAtB[NA];
	for (int j=0; j<NA; j++)
		{int dummyhr, dummymin;
		char dummychar;
		fin >> dummyhr >> dummychar >> dummymin;
		DepartFromA[j]=(dummyhr*60 + dummymin);
		fin >> dummyhr >> dummychar >> dummymin;
		ArriveAtB[j]=(dummyhr*60 + dummymin);}
	for (int j=0; j<NB; j++)
		{int dummyhr, dummymin;
		char dummychar;
		fin >> dummyhr >> dummychar >> dummymin;
		DepartFromB[j]=(dummyhr*60 + dummymin);
		fin >> dummyhr >> dummychar >> dummymin;
		ArriveAtA[j]=(dummyhr*60 + dummymin);}
	sort (DepartFromA, NA);
	sort (ArriveAtA, NB);
	sort (DepartFromB, NB);
	sort (ArriveAtB, NA);
	
	int ReqdFromA=0, ReqdFromB=0;
	int k=0;
	for (int j=0; j<NA; j++)
		{if ( (k<NB) && ( (DepartFromA[j]-ArriveAtA[k]) >= TurnTime) )
			k++;
		else
			ReqdFromA++;
		}
	k=0;
	for (int j=0; j<NB; j++)
		{//cerr << ArriveAtB[k] << endl;
		if ( (k<NA) && ( (DepartFromB[j]-ArriveAtB[k]) >= TurnTime) )
			k++;
		else
			ReqdFromB++;
		}
//	cerr<<TurnTime << " " <<NA<<" " << NB<<endl;
	cout << "Case #" << i << ": " << ReqdFromA << " " << ReqdFromB << endl;
	}
}