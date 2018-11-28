#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int T;
    int N, S, p;
    int count;
    int t[100];

    ifstream in("B-large.in");
    ofstream out("B-large.out");

    in >> T;
    for(int j=1; j<=T; j++)
    {
        in >> N >> S >> p;
        count = 0;

        for(int i=0; i<N; i++)
        {
            in >> t[i];
            int not_suprised_max = (t[i]+2)/3;
            int suprised_max = (t[i]+4)/3;
            if(not_suprised_max>=p && not_suprised_max >=1)
                count++;
            else if(S >0 && suprised_max>=p && suprised_max>=2)
            {
                count++;
                S--;
            }
            else if(not_suprised_max == 0 && p == 0)
                count++;
        }
        out << "Case #" << j << ": " << count << endl;
    }

    in.close();
    out.close();
    return 0;
}
