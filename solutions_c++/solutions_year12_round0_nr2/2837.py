#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <stack>
#include <vector>
using namespace std;


int main()
{
    ifstream inputFile;
    ofstream outputFile;

    inputFile.open("B-large.in");
    outputFile.open("B-large.out");

    int T;
    int i,j;
    int N;
    int S;
    int p;
    int t;
    int lower;
    int lowerS;
    int normal;
    int normalWithS;
    while(inputFile>>T)
    {
        for (i=0;i<T;i++)
        {
            inputFile>>N;
            inputFile>>S;
            inputFile>>p;
            normal=0;
            normalWithS=0;


            if(p==0)
            {
                lower = 0;
                lowerS = 0;
            }
            else if(p==1)
            {
                lower = 1;
                lowerS = 1;
            }
            else
            {
                lower = 3*(p-1)+1;
                lowerS = 3*(p-2)+2;
            }

            if(lower<0)
            {
                lower=0;
            }

            if(lowerS<0)
            {
                lowerS=0;
            }

            for(j=0;j<N;j++)
            {
                inputFile>>t;

                if(t>=lower)
                {
                    normal++;
                }
                if(t>=lowerS)
                {
                    normalWithS++;
                }
            }

            if(normalWithS-normal>=S)
            {
                normal+=S;
            }
            else
            {
                normal=normalWithS;
            }
            outputFile<<"Case #"<<i+1<<": ";
            outputFile<<normal<<endl;
        }

    }

    system("pause");
    return 0;
}