#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ofstream o;
    o.open("out.txt");
    int T;
    cin >> T;
    long long N,K;
    for(int i=0;i<T;i++)
    {
        cin >> N >> K;
        
        long long pN = 1 << N;
        K = K % pN;
        o << "Case #" << i+1 << ": ";
        if (K == pN-1)o << "ON" << endl;
        else o << "OFF" << endl;
    }
    o.close();
    return 0;
}
