#include <stdio.h>
#include <math.h>
#include <fstream>
#include <stdlib.h>
#include <ctype.h>
#include <conio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>


using namespace std;


void check(int,int,int);


int n = 0;
int N = 0;
int S = 0;
int p = 0;
int t = 0;
int s = 0;
int c = 0;


int main()
{
    string inp;
    int i;
    int j;
    ifstream input ("B-large.in.txt");
    ofstream output ("output.out");
    if(input.is_open())
    {
        getline(input,inp);
        n = atoi(inp.c_str());
        for(i = 1; i <= n; i++)
        {
            getline(input,inp);
            output << "Case #" << i << ": ";
            N = 0;
            S = 0;
            p = 0;
            t = 0;
            s = 0;
            c = 0;
            istringstream is(inp);
            is >> N >> S >> p;
            for(j = 0; j < N; j++)
            {
                is >> t;
                if(t > 1 && t>=(3*p-4) && t<(3*p-2))
                {
                    s += 1;
                }
                if(t>=(3*p-2))
                {
                    c += 1;
                }
            }
            int x = c;
            if ( s <= S)
            {
                x += s;
            }
            else
            {
                x += S;
            }
            output << x << "\n";
        }
    }
}
