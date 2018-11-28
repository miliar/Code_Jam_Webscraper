#include <iostream>

using namespace std;



int main()
{
    int T;
    cin >> T;

    int socre[50];

    for (int testcase=1; testcase<=T; ++testcase) {

        int N, S, p;
        cin >> N >> S >> p;

        int total = 0;
        int tmp;
        for (int i=0; i<N; i++)
        {
            cin >> tmp;
            if(tmp<2)
            {
                if(tmp>=p)
                    total++;
                continue;
            }

            if (tmp+2>= p*3)
                total++;
            else if (S>0 && tmp+4>=p*3)
            {
                S--;
                total++;
            }
        }

        cout << "Case #" << testcase << ": " << total << endl;
    }
    return 0;
}
