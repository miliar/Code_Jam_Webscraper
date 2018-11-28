// 2012-round1A-A.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <ctime>

//#define LARGE_PROBLEM
//#define SHOW_TIME
//#define MYDEBUG

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned char uchar;

using namespace std;

long double p[100000];
//double pcorrct[100000];
// double pwrong [100000];

// a is the number of inputed char
// b is the number of total char
double Solve(int a, int b)
{
    int factor = 1000000;
    double best = factor*(b + 2 ); 

    double error = 1e-6;
    double pcorrect = factor * p[0];
    double score = pcorrect*(a-1+b) + (factor-pcorrect) * (a-1+b+b+1);
    best = min(score, best);
    for (int i=1; i<a; i++) {
        pcorrect *= p[i];
        double score = pcorrect*( a-i-1 + b-i) + (factor-pcorrect) * ( a-i-1 + b-i+b+1);
        best = min(score, best);
    }

 #ifdef MYDEBUG
#endif
   return best/factor;
}


int main(int argc, char * argv[])
{
#ifdef LARGE_PROBLEM
    ifstream fin("A-large.in");
    ofstream fout("A-large.out2");
#else
    ifstream fin("A-small-attempt1.in");
    ofstream fout("A-small-attempt1.out");
#endif

    fout.precision(10);
    fout.setf(ios::fixed,ios::floatfield);

    if(!fin.is_open()) {
        cout << "Can't open input file." << endl;
        return -1;
    }

    if(!fout.is_open()) {
        cout << "Can't open output file." << endl;
        return -1;
    }

    clock_t start_clock = clock();

    int T;
    fin >> T;

    int case_no = 0;
    for (int i=0; i<T; i++) {
        int A, B;
        fin >> A >> B;
        for (int j=0; j<A; j++) {
               fin >> p[j];
        }

        double ans = Solve(A, B);
        fout << "Case #" << ++case_no << ": " << ans  << endl;

#ifdef MYDEBUG
      cout << "Case #" << i+1 << ": " << A << ' '<< B << endl;
      cout << "Case #" << i+1 << ": " << ans  << endl;

      //if (i==21)
      //    return -1;
#endif

    }

    clock_t end_clock = clock();

#ifdef SHOW_TIME
    cout << (end_clock - start_clock) / double(CLOCKS_PER_SEC) << endl;
#endif

	return 0;
}
