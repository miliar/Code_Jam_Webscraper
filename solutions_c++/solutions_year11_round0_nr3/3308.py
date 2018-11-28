#include<fstream>
#include<iostream>
#include<vector>
#include<string>
#include<cmath>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int T, N;

vector<int> sweets;
int answer = -1;

void get_sweet(int deep, int realsum, int sum1, int sum2)
{
    if(deep == sweets.size())
    {
        if(sum1 == sum2 && sum1 > 0 && realsum > answer)
        {
 //           cout << sweets[deep - 1] << endl;
            cout << "sum1 = " << sum1 << ", sum2 = " << sum2 << ", realsum = " << realsum << endl;
            answer = realsum;
        }
        return;
    }
    get_sweet(deep + 1, realsum + sweets[deep], sum1^sweets[deep], sum2);
    get_sweet(deep + 1, realsum, sum1, sum2^sweets[deep]);
}

int main()
{
    in >> T;
    for(int t = 0; t < T; t++)
    {
        in >> N;
        sweets.resize(N);
        for(int i = 0; i < N; i++)
            in >> sweets[i];
        answer = -1;
        get_sweet(0, 0, 0, 0);
        if(answer == -1)
            out << "Case #" << t + 1 << ": NO" << endl;
        else
            out << "Case #" << t + 1 << ": " << answer << endl;
    }
    return 0;
}
