#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
using namespace std;

int main()
{
    ifstream in ("B-small-attempt4.in");
    ofstream out("B-small-attempt4.out");

    int N,T,NA,NB;

    in >> N;

    for(int n = 0; n < N; n++)
    {
        in >> T >> NA >> NB;

        vector<int> trains_in_A;
        vector<int> trains_out_A;

        vector<int> trains_in_B;
        vector<int> trains_out_B;

        for(int na = 0; na < NA; na++)
        {
            int hd,md,ha,ma;
            char tmp;

            in >> hd >> tmp >> md >> ha >> tmp >> ma;

            trains_out_A.push_back(hd*60 + md);
            trains_in_B.push_back(ha*60 + ma);
        }

        for(int nb = 0; nb < NB; nb++)
        {
            int hd,md,ha,ma;
            char tmp;

            in >> hd >> tmp >> md >> ha >> tmp >> ma;

            trains_out_B.push_back(hd*60 + md);
            trains_in_A.push_back(ha*60 + ma);
        }

        out << "Case #" << n + 1 << ": ";

        // sort
        sort(trains_in_A.begin(),trains_in_A.end());
        sort(trains_in_B.begin(),trains_in_B.end());

        sort(trains_out_A.begin(),trains_out_A.end());
        sort(trains_out_B.begin(),trains_out_B.end());

        int A = 0, B = 0;

        vector<int>::iterator itrI;
        vector<int>::iterator itrO;

        itrI = trains_in_A.begin();
        itrO = trains_out_A.begin();
        while(itrO != trains_out_A.end())
        {
            if(itrI == trains_in_A.end())
                A++;
            else if(*itrO < *itrI + T)
                A++;
            else
                itrI++;

            itrO++;
        }

        itrI = trains_in_B.begin();
        itrO = trains_out_B.begin();
        while(itrI != trains_in_B.end() && itrO != trains_out_B.end())
        {
            if(itrI == trains_in_B.end())
                B++;
            else if(*itrO < *itrI + T)
                B++;
            else
                itrI++;

            itrO++;
        }

        out << A << " " << B << endl;



    }

    return 0;
}
