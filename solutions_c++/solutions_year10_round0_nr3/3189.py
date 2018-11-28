#include <iostream>
#include <fstream>
#include <string.h>

#define INPUT "C-small-attempt0.in"
#define OUTPUT "C-small-attempt0.out"

using namespace std;

int main (void) {
    ifstream input;
    ofstream output;

    input.open (INPUT);
    output.open (OUTPUT);

    if (input.is_open ()) {
        int data;
        input >> data;
        for (int d=0; d<data; d++) {
            int rounds, max, groups;
            input >> rounds;
            input >> max;
            input >> groups;

            cout << "values:" << rounds << " " << max << " " << groups << endl;

            int grpArr [groups];

            for (int gr=0; gr < groups; gr++) {
                input >> grpArr [gr];
                cout << grpArr [gr] << " ";
            }
            cout << endl;

            int earnings = 0;
            for (int r=0; r < rounds; r++) {
                int ppl = 0, gr;
                for (gr=0; gr < groups; gr++) {
                    if ((ppl + grpArr [gr]) <= max )
                        ppl += grpArr [gr];
                    else
                        break;
                }
                earnings += ppl;
                
                int temparr [groups], idx, mv;
                for (idx=0, mv=gr; mv < groups; mv++, idx++) {
                    temparr [idx] = grpArr [mv];
                }

                for (mv=0;mv < gr; idx++, mv++) {
                    temparr [idx] = grpArr [mv];
                }
                
                memcpy (grpArr, temparr, sizeof (grpArr));

                for (idx=0; idx < groups; idx++)
                    cout << grpArr[idx] << " ";
                cout << endl;
            }   
            
            cout << "earnings:" << earnings << endl;
            output << "Case #" << d + 1 << ":" << " " << earnings << endl;
       }
    }    

    return 0;
}

