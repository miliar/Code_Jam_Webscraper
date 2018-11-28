#include <fstream>
using namespace std;

int main()
{
    ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

    long N, K;
    long T, cnt;

    infile >> T;
    cnt = 1;
    while(T--)
    {
        infile >> N >> K;
        outfile << "Case #" << cnt << ": " ;
        long temp = 1 << N;
        if ( K % temp == temp -1) outfile << "ON" << endl;
        else outfile << "OFF" << endl;
        cnt++;
    }

    infile.close();
    outfile.close();
    return 0;
}
