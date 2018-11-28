#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int compute_minute(string& hhmm);
void run(int* pData, int* arv, int left,int right);
void QuickSort(int* dp, int* arv, int Count);


int main()
{
	// read file
	ifstream infile("B-large.in");
	ofstream outfile("B-large.out");

	int N;
	int turntime;  // turnaround time
	int NA, NB;
	
	infile >> N;   // case number

	int tbentry;   // total number of table entry
	
	int *dpA, *arvA, *dpB, *arvB, *flagA, *flagB;
	int numA, numB;  // the number of A and B
	int pntA, pntB;  // index
	string hhmm;
	int i,j,k;

	for(i = 0; i < N; i++)
	{		
		pntA = 0;
		pntB = 0;
		numA = 0;
		numB = 0;
		// every case
		infile >> turntime;
		infile >> NA >> NB;
		tbentry = NA + NB;
		
		// assign memory
		dpA = new int[NA];
		arvA = new int[NA];
		dpB = new int[NB];
		arvB = new int[NB];
		flagA = new int[NA];
		flagB = new int[NB];

		// read information from input file
		for (j = 0; j < NA; j++)
		{
			infile >> hhmm;
			dpA[j] = compute_minute(hhmm);
			infile >> hhmm;
			arvA[j] = compute_minute(hhmm);
			
			flagA[j] = 0;
		}
		for (j = 0; j < NB; j++)
		{
			infile >> hhmm;
			dpB[j] = compute_minute(hhmm);
			infile >> hhmm;
			arvB[j] = compute_minute(hhmm);

			flagB[j] = 0;
		}

		// sort the table by the departure time
		QuickSort(dpA, arvA, NA);
		QuickSort(dpB, arvB, NB);

		// the main procedure
		while (pntA < NA && pntB < NB)
		{
			if (dpA[pntA] < dpB[pntB])  // train in station A first
			{
				for (k = 0; k < pntB; k++)
				{
					if (flagB[k]!=1 && arvB[k] + turntime <= dpA[pntA])
					{
						// flagA[pntA] = flagB[k]; // the number of trains will not increase
						flagB[k] = 1;   // we can't use it again
						break;
					}
				}
				
				if (k == pntB)
				{
					numA++;
					// flagA[pntA] = numA;
				}

				pntA++;
			}
			else   // dpA[pntA] > dpB[pntB]
			{
				// current station is B
				for (k = 0; k < pntA; k++)
				{
					if (flagA[k]!=1 && arvA[k] + turntime <= dpB[pntB])
					{
						// flagB[pntB] = flagA[k]; // the number of trains will not increase
						flagA[k] = 1;
						break;
					}
				}
				
				if (k == pntA)
				{
					numB++;
					// flagB[pntB] = (-numB);
				}
				pntB++;
			}
		}

		while(pntA == NA && pntB < NB)
		{
			// current station is B
			for (k = 0; k < pntA; k++)
			{
				if (flagA[k]!=1 && arvA[k] + turntime <= dpB[pntB])
				{
					// flagB[pntB] = flagA[k]; // the number of trains will not increase
					flagA[k] = 1;
					break;
				}
			}
			
			if (k == pntA)
			{
				numB++;
				//flagB[pntB] = (-numB);
			}
			pntB++;
		}

		while(pntB == NB && pntA < NA)
		{
			// current station is A
			for (k = 0; k < pntB; k++)
			{
				if (flagB[k]!=1 && arvB[k] + turntime <= dpA[pntA])
				{
					// flagA[pntA] = flagB[k]; // the number of trains will not increase
					flagB[k] = 1;
					break;
				}
			}
			
			if (k == pntB)
			{
				numA++;
				//flagA[pntA] = numA;
			}

			pntA++;
		}

		outfile << "Case #" << i+1 << ": " << numA << " " << numB << endl;

		// free memeory
		delete []dpA;
		delete []dpB;
		delete []arvA;
		delete []arvB;
		delete []flagA;
		delete []flagB;
	}
	
	infile.close();
	outfile.close();
	return 0;
}


// change the time style to minutes instead of HH:MM
int compute_minute(string& hhmm)
{
	return (atoi(hhmm.substr(0,2).c_str()))*60 + atoi(hhmm.substr(3,2).c_str());
}


void run(int* pData, int* arv, int left,int right)
{
    int i,j;
    int middle,iTemp;
    i = left;
    j = right;
    middle = pData[(left+right)/2]; 
    do{
        while((pData[i]<middle) && (i<right))// scan from left to right
            i++;           
        while((pData[j]>middle) && (j>left))// scan from right to left
            j--;
        if(i<=j) // find a value
        {
            // change
            iTemp = pData[i];
            pData[i] = pData[j];
            pData[j] = iTemp;

			iTemp = arv[i];
			arv[i] = arv[j];
			arv[j] = iTemp;

            i++;
            j--;
        }
    }while(i<=j); //cross

    if(left<j)
        run(pData, arv, left,j);

    if(right>i)
        run(pData,arv, i,right);
}

void QuickSort(int* dp, int* arv, int Count)
{
    run(dp, arv, 0, Count-1);
}