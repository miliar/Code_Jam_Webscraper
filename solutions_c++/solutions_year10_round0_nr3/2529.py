#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int RollerEarnings(int _r, int _k, int _n, ifstream &file);
void DoStep(int &num, int size);

int main(int argc, char *argv[]) {
    if(argc <= 1)
        cout<<"Move the input file above the executable\n\n";
    else {
        int T, R, K, N;

        ifstream FileIn(argv[1]);
        ofstream FileOut("output.txt");

        FileIn>>T;

        for(register int i = 0; i < T; ++i) {
            FileIn>>R>>K>>N;

            FileOut<<"Case #"<<i+1<<": "<<RollerEarnings(R, K, N, FileIn)<<endl;
        }

        FileIn.close();
        FileOut.close();
    }

    system("PAUSE");

    return 0;
}

int RollerEarnings(int _r, int _k, int _n, ifstream &file) {
    int Groups[_n], Times = 0, Earnings = 0, STimes = 0, SEarnings = 0,
        Roller = 0, Pos = 0, PosMark;

    for(int i=0; i < _n; ++i)
        file>>Groups[i];

    while(STimes < _r) {
        PosMark = Pos;

        Roller = 0;
        do {
            Roller += Groups[Pos];

            DoStep(Pos, _n);
        } while((Roller + Groups[Pos] <= _k) && (Pos != PosMark));

        STimes++;
        SEarnings += Roller;

        if(Pos == 0)
            break;
    }

    Times += _r/STimes * STimes;
    Earnings += _r/STimes * SEarnings;

    if(STimes < _r) {
        while(Times < _r) {
            PosMark = Pos;

            Roller = 0;
            do {
                Roller += Groups[Pos];

                DoStep(Pos, _n);
            } while((Roller + Groups[Pos] <= _k) && (Pos != PosMark));

            Times++;
            Earnings += Roller;
        }

        return Earnings;
    } else
        return Earnings;
}

void DoStep(int &num, int size) {
    num++;

    if(num >= size)
        num = 0;
}
