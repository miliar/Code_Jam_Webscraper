#include <iostream>
#include <vector>
using namespace std;

bool cansplit(vector<int> vec)
{
    int res = 0;
    for (int i = 0; i < vec.size(); i++)
        res = (res ^ vec[i]);
    if (res) return false;
    else return true;
}

int main()
{
    int T, N, t;
    cin >> T;
    for (t = 0; t < T; t++) {
        cin >> N;
        vector<int> vec;
        int val, min = 1000000;
        long sum = 0;
        for (int i = 0; i < N; i++) {
            cin >> val;
            sum += val;
            if(min > val) min = val;
            vec.push_back(val);
        }

        cout << "Case #" << t+1 << ": ";
        if (!cansplit(vec)){
            cout << "NO" << endl;
            continue;
        }
        cout << sum -min << endl;
    }
    return 0;
}
