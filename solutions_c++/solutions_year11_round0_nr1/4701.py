//#include <iostream>
#include <fstream>

std::ifstream cin("A-large.in");
std::ofstream cout("A-large.out");

#define abs(a) ((a) < 0) ? -(a) : (a)
#define max(a, b) (a < b) ? (b) : (a)

int main ()
{
    char roby;
     int buty, i, j, k,
         testcount,
         casecount,
         testcase = 1;

      int time, timefor_O, timefor_B;

        cin >> testcount;

            while (testcount--)
            {
                cin >> casecount;

                time = timefor_O = timefor_B =  0;
                i = j = 1;

                    while (casecount--)
                    {
                        cin >> roby >> buty;

                        if(roby == 'O')
                        {
                            k = abs(buty - i);
                            k -= (k > timefor_O) ? timefor_O : k;

                                time += k + 1;
                                timefor_O = 0;
                                timefor_B += k + 1;

                            i = buty;
                        }
                        else
                        {
                            k = abs(buty - j);
                            k -= (k > timefor_B) ? timefor_B : k;

                                time += k + 1;
                                timefor_O += k + 1;
                                timefor_B = 0;

                            j = buty;
                        }
                    }

                cout << "Case #" << testcase++ << ": " << time << std::endl;
            }

     return 0;
}
