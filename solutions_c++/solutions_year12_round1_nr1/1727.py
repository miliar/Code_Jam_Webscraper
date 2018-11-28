#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;
ifstream fin("zad1.in");
ofstream fout("zad1.out");

double cpi(double *X, int A)
{
    double sum=1;
    for (int j=0; j<A; j++)
    {
        sum *= X[j];
    }
    return sum;
}
double zad1(int A, int B, double *X)
{
    double min = B+2;
    double P=cpi(X,A);
    double cur;
    for (int i=0; i<A; i++)
    {
        cur=(B-A+2*i+1)*P+(2*B-A+2*i+2)*(1-P);
        if (cur<min) min = cur;
        P/=X[A-i-1];
    }
    return min;
}

int main()
{
    int T;
    int A,B;
    double* X;
    fin>>T;
    for (int i=1; i<=T; i++)
    {
        fin>>A>>B;
        X = new double[A];
        for (int k=0; k<A; k++)
        {
            fin>>X[k];
        }
        fout<<"Case #"<<i<<": ";
        fout<<setprecision (6)<< fixed << zad1(A,B,X) <<endl;
        delete[] X;
    }
    fin.close();
    return 0;
}
