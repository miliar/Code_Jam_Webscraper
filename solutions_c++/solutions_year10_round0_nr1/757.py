#include <iostream>
#include <fstream>

using namespace std;

int T, N, K, powN, del,ans;


int main()
{

    ifstream b_file ( "input.txt" );
    ofstream a_file ( "output.txt" );

    b_file >> T;
    for (int i=1; i<=T; i++)
        {
        b_file >> N;
        b_file >> K;


        powN = 1;
        for (int j=1; j<=N; j++)
        {
            powN *= 2;
        }

        del = K%powN;

        cout<<powN<<"\n";
        cout<<del<<"\n";

        if (del == powN-1)
            {a_file<<"Case #"<<i<<": "<<"ON"<<"\n";}
        else
            {a_file<<"Case #"<<i<<": "<<"OFF"<<"\n";}

        }


    cin.get(); 
    return 0;
}
