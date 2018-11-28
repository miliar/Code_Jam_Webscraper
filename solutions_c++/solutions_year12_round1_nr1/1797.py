

#include <fstream>
#include <iostream>

#include <vector>
#include <map>

#include <cstdio>
#include <cmath>

using namespace std;

static double solve( ifstream &infile )
{
    int typed = 0;
    infile >> typed;

    int length = 0;
    infile >> length;

    std::vector<double> p(typed);
    std::vector<double> ip(typed);
    std::vector<double> letterWrong(typed);

    //printf("\n\tt: %d, l: %d", typed, length);

    int allCorrectInt = 1;
    double allCorrect = 1.0;

    for( int i=0; i<typed; ++i )
    {
        infile >> p[i];
        ip[i] = 1.0 - p[i];

        //printf(" %f", p[i]);
        allCorrectInt *= (int)floor(p[i]);
        allCorrect *= p[i];
    }
    //printf(" (ac: %d, %f)\n", allCorrectInt, allCorrect);

    if( allCorrectInt == 1 )
    {
        return length-typed+1;
    }

    int hitEnter = length + 2;

    double allWrong = 1.0 - allCorrect;

    //printf(" calcing (%f)\n", allWrong);

    double keepTyping = allCorrect*(length-typed+1)+allWrong*(length-typed+hitEnter);

    //printf("\tkt: %f\n", keepTyping );
    double best = (keepTyping < hitEnter) ? keepTyping : hitEnter; 
    int allBackspace = (typed+length+1);

    if( allBackspace < best )
    {
        best = allBackspace;
    }

    int rightbase = (length-typed)+1;
    int wrongbase = (length-typed)+hitEnter;

    for( int bs=1; bs<typed; ++bs )
    {
        int right = rightbase + bs*2;
        int wrong = wrongbase + bs*2;
        double rightprob = 1.0;
        double wrongprob = 1.0;

        //printf("\tbs: %d\n", bs);
        int j=0;
        for( j=0; j<typed-bs; ++j )
        {
            rightprob *= p[j];
            //printf("\t%d: rp: %f\n", j, rightprob);
        }
        wrongprob -= rightprob;

        double ev = rightprob*right + wrongprob*wrong;
        //printf("\tr: %f * %d + w: %f * %d = %f\n", rightprob, right, wrongprob, wrong, ev);

        if( ev >= best )
        {
            continue;
        }

        best = ev;
    }

    return best;
}

int main( int argc, char **argv )
{
    if( argc < 2 )
    {
        ////printf("!!! NO INPUT FILE !!!\n");
        return -1;
    }

    std::ifstream infile(argv[1]);

    int cases = 0;

    infile >> cases;

    for(int caseNum=0; caseNum<cases; ++caseNum)
    {
        cout << "Case #" << caseNum+1 << ": ";

        double answer = solve( infile );

        printf("%.6f\n", answer);
    }

    return 0;
}

