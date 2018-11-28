#include <iostream>
#include <math.h>
#include <string>

using namespace std;


#include<fstream>
ifstream fin("B-small-attempt3.in");
ofstream fout("output.txt");

int main()
{

    int n;
    int arrA[1000];
    int arrB[1000];

    int numT;
	int numN;

    int i, j, k;
    int count;

    int newNumA = 0;
    int newNumB = 0;


    if(NULL == fin)
    {
      cout<<"NO INPUT FILE"<<endl;
      return 0;
    }

    fin >> numT;


	for(i = 0; i < numT; i++)
	{
       fin >> numN;
       count = 0;


       fin >> arrA[0];
       fin >> arrB[0];



        for(j = 1; j < numN; j++)
        {
             fin >> newNumA;
             fin >> newNumB;

                int q=0;

                while((arrA[q] <= newNumA) && (q < j))
                {
                    q++;
                }

                if(q == j)
                {
                   arrA[j] = newNumA;
                   arrB[j] = newNumB;
                 }
                else
                {
                  for(int r = j-1; r >= q ; r-- )
                  {
                    arrA[r+1] = arrA[r];
                    arrB[r+1] = arrB[r];
                  }

                  arrA[q] = newNumA;
                  arrB[q] = newNumB;
                }

          }



          for(j = 0; j < numN; j++)
          {
                for(k = j; k < numN; k++)
                 {
                   if(arrB[j] > arrB[k])
                     count++;
                 }

           }




		fout << "Case #" << i + 1 << ": "  << count << endl;
	}


   return 0;
}







