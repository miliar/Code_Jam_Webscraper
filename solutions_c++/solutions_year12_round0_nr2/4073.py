#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;



int main ()
{
    int no_of_tests, n, surprise_counter, compare, number, mod, average_score, counter;
    cin >> no_of_tests;

    for (int i = 0; i < no_of_tests; ++i)
    {
        counter = 0;
        cin >> n >> surprise_counter >> compare;
        for (int j = 0; j < n; ++j)
        {
            cin >> number;
            average_score = number/3;
            mod = number%3;

            if (average_score >= compare)
            {
                ++counter;
            }

            else if ((mod > 0) && ((average_score+1)>=compare))
            {
                ++counter;
            }
            else if ((average_score>=1) && ((average_score+1)>=compare) && (surprise_counter > 0))
            {

                    ++counter;
                    --surprise_counter;


            }
            else if ((mod == 2) && ((average_score+2)>=compare) && (surprise_counter > 0))
            {

                    ++counter;
                    --surprise_counter;

            }



        }
        cout << "Case #" << i+1 << ": " << counter << endl;
    }
    return 0;

}
