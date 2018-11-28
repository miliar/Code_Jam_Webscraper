
//#define BEFORE_SUBMIT

#ifdef BEFORE_SUBMIT
#include <conio.h>
#endif /* BEFORE_SUBMIT */

#include <iostream>
#include <queue>

/*

R times
k people
and N groups

Small dataset

1 ? R ? 1000.
1 ? k ? 100.
1 ? N ? 10.
1 ? gi ? 10.
Large dataset

1 ? R ? 108.
1 ? k ? 109.
1 ? N ? 1000.
1 ? gi ? 107.

*/



using namespace std;

int main()
{
    int no_of_test_cases;
    cin>>no_of_test_cases;
    int temp1 = no_of_test_cases;
    while(temp1--)
    {
        long long int R, k, N, money = 0, total_log=0;
        cin>>R>> k>> N;
        queue <long long int> groups;
        for (long long int i=0; i<N; i++)
        {
            long long int g;
            cin>>g;
            total_log = total_log+g;
            groups.push(g);
        }
        int temp_R = R;
        while (temp_R--)
        {
            long long int curr_t = 0, g_in=0;
            while ((curr_t+groups.front()<=k)&&(g_in<N))
            {
                curr_t = curr_t + groups.front();
                groups.push(groups.front());
                groups.pop();
                g_in++;
            }
            money = money+curr_t;
            curr_t = 0;
        }
        cout<<"Case #"<<no_of_test_cases-temp1<<": "<<money<<"\n";
    }
#ifdef BEFORE_SUBMIT
    getch();
#endif /* BEFORE_SUBMIT */
    return 0;
}
