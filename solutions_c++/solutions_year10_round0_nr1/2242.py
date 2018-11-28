#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t=0;t<T;t++)
    {
        int N,K;
        cin >> N >> K;
        int X = 1 <<N;
        int M = (K % X);
        bool on = (M) == (X-1);
        cout << "Case #" << t+1 << ": " << (on? "ON":"OFF") << endl;
    }
}
