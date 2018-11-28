#include <iostream>
#include <math.h>
#include <string>
using namespace std;


#include<fstream>
ifstream fin("C-small-attempt0.in");
ofstream fout("output.txt");

int main()
{

	int n;
    int arr[1000];
    int numR;
	int numK;
    int numN;
    int i, j, k;
    int totalIncome = 0;
    int count = 0 ;
    int index = 0;
    int numGroup = 0;

    if(NULL == fin)
    {
      cout<<"NO INPUT FILE"<<endl;
      return 0;
    }

    fin >> n;


	for(i = 0; i < n; i++)
	{
       fin >> numR;
       fin >> numK;
       fin >> numN;

        for(j = 0; j < numN; j++)
        {
              fin >> arr[j];
             // cout << " Input "<< j <<" :: " << arr[j]<<endl;
        }

        index = 0;
        totalIncome = 0;
        for(k = 0; k < numR; k++)
        {
           numGroup = 0;

               for(count = 0; ((count + arr[index]) <= numK) && (numGroup < numN);
                        numGroup++)
               {
                 count = count + arr[index];

                 if(index == (numN-1))
                   index = 0;
                 else
                   index++;
               }


               totalIncome +=  count;
           }


		fout << "Case #" << i + 1 << ": "  << totalIncome << endl;
	}



	return 0;
}







