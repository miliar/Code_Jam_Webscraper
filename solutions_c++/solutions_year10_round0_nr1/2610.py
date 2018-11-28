#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

string IsTurnedOn(int _n, int _k);

int main(int argc, char *argv[]) {
    if(argc <= 1)
        cout<<"Move the input file above the executable\n\n";
    else {
        int N, K, T;

        ifstream FileIn(argv[1]);
        ofstream FileOut("output.txt");

        FileIn>>T;

        for(register int i = 0; i < T; ++i) {
            FileIn>>N>>K;

            FileOut<<"Case #"<<i+1<<": "<<IsTurnedOn(N, K)<<endl;
        }

        cout<<"Done!\n\nCheck the output.txt file\n\n";
    }

    system("PAUSE");

    return 0;
}

string IsTurnedOn(int _n, int _k) {
    bool OnOff;

    for(register int i = _n; i >= 1; --i) {
        if(_k % int(pow(2, i)) < int(pow(2, i - 1))) {
            OnOff = false;

            break;
        } else
            OnOff = true;
    }

    if(OnOff)
        return "ON";

    return "OFF";
}
