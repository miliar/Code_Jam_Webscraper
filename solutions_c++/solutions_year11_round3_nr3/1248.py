#include <iostream>
#include <fstream>
#include <iomanip>// fixed << setprecision(#);
#include <vector>
#include <string>

using namespace std;

int main()
{
    ifstream input ("input3.txt");
    ofstream output ("output3.txt");

    int cases;
    input >> cases;

    for(int a = 0; a < cases; a ++)
    {
        int N, L, H;
        input >> N >> L >> H;
        vector<int> people;
        int tmp;
        for(int b = 0;b < N; b++)
        {
            input >>tmp;
            people.push_back(tmp);

        }

        bool possible = false;
        int freq;
        if(L !=1)
        {
            for(int b = L; b <=H; b++)
            {
                bool multiple = true;
                for(int c = 0; c < people.size(); c++)
                {
                    double quotient;
                    if(people[c] < b)
                    {
                        quotient = double(b)/double(people[c]);
                        if(quotient != double(int(quotient)))
                        {
                            multiple = false;
                            break;
                        }
                    }
                    else if(people[c] > b)
                    {
                        quotient = double(people[c]/double(b));
                        if(quotient != double(int(quotient)))
                        {
                            multiple = false;
                            break;
                        }
                    }
                }
                if(multiple == true)
                {
                    possible = true;
                    freq = b;
                    break;
                }
            }
        }
        else
        {
            possible = true;
            freq = 1;
        }
        if(possible)
        {
            output << "Case #" << a+1 << ": " << freq <<endl;
        }
        else
        {
            output << "Case #" << a+1 << ": NO" <<endl;
        }


    }

    return 0;
}
