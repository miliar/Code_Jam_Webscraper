#include <fstream>
using namespace std;

int main()
{
    ifstream in("A-large (1).in");
	ofstream out("A-large (1).out");

    long N, K;
    long T, cnt;

    in >> T;
    cnt = 1;
    while(T--)
    {
        in >> N >> K;
        out << "Case #" << cnt << ": " ;
        long T = 1 << N;
        if ( K % T == T -1) out << "ON" << endl;
        else out << "OFF" << endl;
        cnt++;
    }

    in.close();
    out.close();
    return 0;
}
