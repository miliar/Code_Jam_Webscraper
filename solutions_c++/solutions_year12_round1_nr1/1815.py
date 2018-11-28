// =========================================================
//
//       Filename:  Password Problem.cpp
//
//    Description:
//
//        Version:  1.0
//        Created:  04/27/2012
//       Revision:  none
//       Compiler:  g++
//
//         Author:  Tao Lin, tlin005@gmail.com
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 04/27/2012
//
// =========================================================

#include <iostream>
#include <vector>
#include <string.h>
#include <math.h>

using namespace std;

#define MAXNUM 200


double solve(unsigned int A, unsigned int B, vector< double > p_list)
{
    if (A >= B)
        return 0;

    double result = 0;

    vector< double> sum_p;
    sum_p.push_back(1);
    for (unsigned int i = 0; i < p_list.size(); i++)
        sum_p.push_back(sum_p[i]*p_list[i]);

    double exp;
    // keep typing
    exp = sum_p[A]*(B-A+1) + (1-sum_p[A])*(B-A+1+B+1);
    result = exp;

    // give up
    exp = 1+B+1;
    if (exp < result)
        result = exp;

    // k backspace

    for (unsigned int i = 1; i <= A; i++)
    {
        double pp = 0;
        for (unsigned int j = A-i+1; j <= A; j++)
            pp += sum_p[j-1]*(1-p_list[j-1]);
        pp += sum_p[A];

        exp = pp*(i+B-A+i+1) + (1-pp)*(i+B-A+i+1+B+1);
        if (exp < result)
            result = exp;
    }

    return result;
}

int main()
{
    unsigned int case_no;
    unsigned int A, B;
    vector< double > p_list;

    double result;

    // load input
    cin >> case_no;

    for (unsigned int i = 0; i < case_no; i++)
    {
        cin >> A;
        cin >> B;
        //cout << A << " " << B << endl;

        p_list.clear();
        for (unsigned int j = 0; j < A; j++)
        {
            double p;
            cin >> p;
            //cout << p << endl;
            p_list.push_back(p);
        }
        // sove problem
        result = solve(A, B, p_list);
        cout << "Case #" << i+1 << ": ";
        cout << result << endl;
    }

    return 0;

}
