#include <fstream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;
int main()
{
    ifstream f;
    ofstream g;

    f.open("C-small.in");
    g.open("C-small.out");

    string S,X;
    int N;
    S="welcome to code jam";
    int T[100][501];



    f>>N;
    f.get();

    for(int cnt=1; cnt<=N; cnt++)
    {

        getline(f, X);
        for(int i=1; i<=X.size(); i++)
            for(int j=1; j<=S.size(); j++)
                T[i][j]=0;

        T[0][0] = (X[0] == S[0]);

        for(int i=1; i<=X.size(); i++)
            for(int j=0; j<=S.size(); j++)
            {
                T[i][j] = T[i-1][j];
                if(X[i] == S[j])
                if(j>0) T[i][j] = (T[i][j] + T[i-1][j-1]) % 10000;
                    else T[i][j] = (T[i][j] +1) % 10000;
            }

        g<<"Case #"<<cnt<<": "<<setfill('0')<<setw(4)<<T[X.size()][S.size()]<<endl;

    }

    f.close();
    g.close();
    return 0;
}
