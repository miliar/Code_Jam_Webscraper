#include<iostream>
#include<fstream>
#include<map>
#include<stdlib.h>
#include<math.h>
#include<set>

using namespace std;

unsigned long long func(unsigned long long a, unsigned long long b)
{
   unsigned long long i;
   unsigned long long ret = 0;
   set<unsigned long long> myset;

   for (i = a ; i <= b; i ++)
   {
        int length = 0;
        unsigned long long temp = i;
        unsigned long long temp1;

        myset.clear();

        while (temp > 0)
        {
            temp = temp /10;
            length++;
        }

        temp = i;
        int iter = length;
        while (iter > 1)
        {
            int res = temp % 10;
            temp1 = temp/10 + res * (unsigned long long) pow(10, (length-1));

            if ((temp1 <=b) && (temp1 > i) && (myset.count(temp1) == 0))
            {
                myset.insert(temp1);
        //        cout << i << " : " << temp1 << endl;
                ret++;
            }
            
            temp = temp1;
            iter--;
        }
   }
   return ret;
}

int main()
{
    char getch;
    //ifstream infile ("C-small-attempt0.in");
    ifstream infile ("C-large.in");
    //ifstream infile ("input.txt");
    ofstream outfile;
    outfile.open("output.txt");
    int numlines = 0;
    int index = 0;
    int rowindex = 0;
    unsigned long long temp =0;
    unsigned long long numN = 0;
    unsigned long long numM = 0;
    unsigned long long res = 0;

    if (infile.is_open())
    {
        while (!infile.eof())
        {
            //infile.get(getch);
            getch = infile.get();
            if (getch >= '0' && getch <= '9')
            {
                temp = temp * 10 + getch - '0';
                continue;
            }
            if (getch == '\n' )
            {
                if (index == 0)
                {
                     numlines = temp; 
                     temp = 0;
                }
                else
                {
                    numM = temp;
                    temp = 0;
                    
                    cout << numN << " : " << numM << endl;
                    cout << "begin: \n";
                    res = func(numN, numM);
                    outfile << res <<"\n";

                }
                index++;

                if (index <= numlines)
                {
                    outfile << "Case #" << index << ": ";
                }

                rowindex =0;
                continue;
            }
            if (getch == ' ')
            {
                if (rowindex == 0)
                {
                    if (index > 0)
                    {
                        numN = temp;
                        temp = 0;
                    }
                    rowindex++;
                }
                else if (rowindex == 1)
                {
                    if (index > 0)
                    {
                        numM = temp;
                        temp = 0;                        
                    }
                    rowindex++;
                }
                continue;
            }
        }

    }
    else
    {
        cout << "unable to open file\n";
    }

    return 0;
}
