
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define FROM_0_TO(i,n) FOR(i,0,n) 

#define PRINT

#define TASKNUM "A"
#define DATASET "large"

ifstream fsIn(TASKNUM "-" DATASET ".in.txt");
ofstream fsOut(TASKNUM "-" DATASET ".out.txt");

class TTestCase
{
private:
    vector<double> Result;
    int N;
    vector<vector<char> > Data;
/*    struct S
    {
        int All;
        int Won;
        int Loose;
    };*/

    struct S
    {
        double Val;
        int All;
    };
    //vector<S> Stat;
    vector<S> WP;
    //vector<vector<double> > WP_without;
    vector<S> OWP;
    vector<S> OOWP;

    void Load();
    void Run();
    void Print();
public:
    TTestCase();
    ~TTestCase();
};


TTestCase::TTestCase()
    : Result(0)
{
	Load();

    Run();
}

void TTestCase::Load()
{
    cin >> N;
    Data.resize(N);
    FOR(i,0,N)
    {
        Data[i].resize(N);
        FOR(j,0,N)
            cin >> Data[i][j];
    }
}

void TTestCase::Run()
{
    WP.resize(N);
    OWP.resize(N);
    OOWP.resize(N);
    //fill(WP.begin(), WP.end(), 0);
    //fill(OWP.begin(), OWP.end(), 0);
    //fill(OOWP.begin(), OOWP.end(), 0);
//    Stat.resize(N);

    FOR(i,0,N)
    {
        WP[i].Val = 0;
        WP[i].All = 0;
        FOR(j,0,N)
        {
            if(Data[i][j] != '.')
            {
                ++WP[i].All;
                if(Data[i][j] == '1')
                    WP[i].Val += 1;
                else
                    ;//++Loose;
            }
        }
        if(WP[i].All == 0)
            throw 1;
        WP[i].Val/=WP[i].All;
    }

    FOR(i,0,N)
    {
        OWP[i].Val = 0;
        OWP[i].All = 0;
        FOR(j,0,N)
        {
            if(Data[i][j] != '.')
            {
                ++OWP[i].All;
                if(Data[i][j] == '1')
                    OWP[i].Val += (WP[j].Val * WP[j].All)/(WP[j].All - 1);
                else
                    OWP[i].Val += (WP[j].Val * WP[j].All-1)/(WP[j].All - 1);
            }
        }
        if(OWP[i].All == 0)
            throw 1;
        OWP[i].Val/=OWP[i].All;
    }

    FOR(i,0,N)
    {
        OOWP[i].Val = 0;
        OOWP[i].All = 0;
        FOR(j,0,N)
        {
            if(Data[i][j] != '.')
            {
                ++OOWP[i].All;
/*                if(Data[i][j] == '1')
                    OOWP[i].Val += (OWP[j].Val * OWP[j].All-WP[i].Val)/(OWP[j].All - 1);
                else
                    OOWP[i].Val += (OWP[j].Val * OWP[j].All-WP[i].Val)/(OWP[j].All - 1);*/
                OOWP[i].Val += OWP[j].Val;
            }
        }
        if(OOWP[i].All == 0)
            throw 1;
        OOWP[i].Val/=OOWP[i].All;
    }

    Result.resize(N);

    FOR(i,0,N)
    {
        Result[i] = 0.25*WP[i].Val + 0.5*OWP[i].Val + 0.25* OOWP[i].Val;
    }




}


TTestCase::~TTestCase()
{
    cout << endl;
    fsOut << endl;
    FOR(i,0,N)
    {
    cout << Result[i] << endl;
    fsOut << Result[i] << endl;
    //printf("%.12f\n", Result);
    }
}

void TTestCase::Print()
{
#ifndef PRINT
    return;
#endif
}








int main()
{
    if(!fsIn.is_open())
    {
        cout << "No input file found";
    }
    cin.rdbuf( fsIn.rdbuf() );

    int numberOfCases;
    cin >> numberOfCases;

	for( int caseNum = 1; caseNum <= numberOfCases; ++caseNum )
	{
        TTestCase testCase;

        
        cout << "Case #" << caseNum << ": ";
        fsOut << "Case #" << caseNum << ": ";
	}
	
	cout << "Finished";
    for(;;);
	return 0;
}
