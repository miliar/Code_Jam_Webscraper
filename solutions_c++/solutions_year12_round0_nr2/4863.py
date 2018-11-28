
#include <fstream>
#include <iostream>
using namespace std;

int result(int p, int surprise, int *sums, int num);

int main()
{
    int buff=1, testCases, numGooglers, sTriplets, pMax;
    int sums[100]={0};
    ifstream myInput("B-large.in.txt");
    ofstream myOutput("output_large_google.txt");

    myInput>>testCases;
    while(myInput.good() && buff<=testCases)
    {
        myInput>>numGooglers;
        myInput>>sTriplets;
        myInput>>pMax;

        for(int i=0; i<numGooglers; i++)
        {
            myInput>>sums[i];
        }

        myOutput<<"Case #"<<buff<<": "<<result(pMax, sTriplets, sums, numGooglers)<<endl;
        buff++;
    }
}

int result(int p, int surprise, int sums[], int numG )
{
    int individual, temp, remainder, counter=0;

    for(int a=0; a<numG; a++)
    {
        temp=sums[a];
        remainder=temp%3;
        individual=temp/3;

        switch(remainder)
        {
            case 0:
                if(surprise>0 &&individual>0)
                {
                    if(individual==(p-1))
                    {
                        individual=individual+1;
                        surprise--;
                    }
                }
                if(individual>=p)
                    counter++;
                break;
            case 1:
                individual++;
                if(individual>=p)
                    counter++;
                break;
            case 2:
                if(surprise>0)
                {
                    if(individual==(p-2))
                    {
                        individual=individual+2;
                        surprise--;
                    }
                    else individual++;
                }
                else individual++;

                if(individual>=p)
                    counter++;
                break;
        }
    }
    return counter;
}
