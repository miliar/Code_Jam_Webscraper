#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <map>

using namespace std;

int main()
{

    ifstream is;
    ofstream rs;
    FILE *pfile = NULL;
    is.open("./A-small-attempt.in");
    pfile = fopen("./res.out", "w");
    //rs.open("./res.out");
    int num_of_test;
    is >>  num_of_test;
    for(int i=0; i<num_of_test; i++)
    {
        int A,B;
        is >> A;
        is >> B;
        vector <double> p(A,0);
        for(int i=0;i<A;i++)
        {
            is >> p[i];
        }
        //
        double min_L;

        //keep typing
        double P=1;
        double L;
        for(int i=0;i<A;i++) P=P*p[i];
        int right_l=(B-A+1);
        int wrong_l=right_l+(B+1);
        min_L=P*right_l+wrong_l*(1-P);
        // i backspaces
        for(int i=1;i<A;i++)
        {
            P=1;
            for(int j=0;j<=i;j++)
            {
                P=P*p[j];
            }
            right_l=(B-A+1)+2*i;
            wrong_l=right_l+(B+1);
            L=P*right_l+wrong_l*(1-P);
            if(L<min_L) min_L=L;
        }
        //enter
        L=B+2;
        if(L<min_L) min_L=L;
        fprintf(pfile,"Case #%d: %.6f\n",i+1,min_L);
        //rs << "Case #" << i+1 << ": " <<  min_L << endl;
    }
    return 0;
}


