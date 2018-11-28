#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    unsigned int T;
    cin >> T;
    for (unsigned int test_case = 1; test_case <= T; test_case++)
    {
        int N, S, p;
        cin >> N >> S >> p;
        int already = 0;
        int potential = 0;
        int t_i, remainder, third;
        for (int i=0; i<N; i++)
        {
            cin >> t_i;
            if (t_i == 0)
            {
                if (p==0)
                    already++;
            }
            else
            {
                remainder = t_i % 3;
                third = t_i / 3;
                switch(remainder)
                {
                case 0:
                    if (third >= p)
                        already++;
                    else if ((third + 1) == p)
                        potential++;
                    break;
                case 1:
                    if (third+1 >= p)
                        already++;
                    break;
                case 2:
                    if (third+1 >= p)
                        already++;
                    else if (third+2 == p)
                        potential++;
                    break;
                }
            }
        }
        
        // cout << already << " " << potential << " " << S << endl;
        
        int answer = already + min(potential, S);
        
        cout << "Case #" << test_case << ": " << answer << endl;
    }
    return 0;
}
