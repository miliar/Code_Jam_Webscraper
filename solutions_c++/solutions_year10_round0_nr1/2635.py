#include <fstream>
#include <math.h>
using namespace std;

int main()
{
    ifstream file1;
    file1.open("A-large.in");
    ofstream file2;
    file2.open("A-large.out");
    int T;
    file1>>T;
    int step=1;
    while(T>0){
        int N;
        unsigned long K;
        file1>>N>>K;
        unsigned int spow = pow(2,N);
        double v=(K+1)/spow;
        if((K+1)/v==spow) file2<<"Case #"<<step<<": ON"<<endl;
        else file2<<"Case #"<<step<<": OFF"<<endl;
        T--;
        step++;
    }
    file1.close();
    file2.close();
    system("PAUSE");
    return 0;
}
