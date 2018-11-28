#include<iostream>
#include<fstream>
#include<map>
#include<stdlib.h>

using namespace std;

map<char, char> charmap;

int main()
{
    char getch;
    //ifstream infile ("B-small-attempt0.in");
    ifstream infile ("B-large.in");
    //ifstream infile ("input.txt");
    ofstream outfile;
    outfile.open("output.txt");
    int numlines = 0;
    int index = 0;
    int rowindex = 0;
    int temp =0;
    int* scorearr; 
    int numDancers = 0;
    int numSup = 0;
    int lstScore = 0;
    int res = 0;

    if (infile.is_open())
    {
        while (!infile.eof())
        {
            //infile.get(getch);
            getch = infile.get();
            //if ()
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
                }
                else
                {
                    scorearr[(rowindex - 3)] = temp;
                    temp = 0;

                    for (int k = 0; k < numDancers; k++)
                    {
                        cout << scorearr[k] << " : " << lstScore << " : " << numSup << endl;
                        int temp1 = lstScore -1;
                        int temp2 = lstScore -2;
                        if (temp1 < 0)
                            temp1 = 0;
                        if (temp2 < 0)
                            temp2 = 0;
                        if (scorearr[k] >= (lstScore + 2* temp1))
                        {
                            res++;
                        }
                        else
                        {
                            if (numSup > 0)
                            {
                                if (scorearr[k] >= (lstScore + 2*temp2))
                                {
                                    res++;
                                    numSup--;
                                }
                            }                            
                        }
                    }

                    outfile << res <<"\n";

                }
                index++;

                if (index <= numlines)
                {
                    outfile << "Case #" << index << ": ";
                }

                rowindex =0;
                    temp =0;
                    scorearr = NULL; 
                    numDancers = 0;
                    numSup = 0;
                    lstScore = 0;
                    res = 0;

                continue;
            }
            if (getch == ' ')
            {
                if (rowindex == 0)
                {
                    if (index > 0)
                    {
                        numDancers = temp;
                        temp = 0;
                        scorearr = (int *) malloc (numDancers * sizeof(int));                        
                        
                    }
                    rowindex++;
                }
                else if (rowindex == 1)
                {
                    if (index > 0)
                    {
                        numSup = temp;
                        temp = 0;                        
                    }
                    rowindex++;
                }
                else if (rowindex == 2)
                {
                    if (index > 0)
                    {
                        lstScore = temp;
                        temp = 0;
                    }
                    rowindex++;
                }
                else if (rowindex > 2)
                {
                    if (index > 0)
                    {
                        scorearr[(rowindex - 3)] = temp;
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
