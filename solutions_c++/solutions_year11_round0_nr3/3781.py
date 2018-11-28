#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int test, n;
    vector<int> candy;
    bool flag;
    cin >> test;
    for (int cs = 1; cs <= test; cs++)
    {
        cin >> n;
        candy.clear();
        candy.resize(n,0);
        for (int i = 0; i < n; i++)
            cin >> candy[i];
        sort(candy.begin(),candy.end());
        int a, b, value;
        flag = false;
        for (int i = 1; i < n; i++)
        {
            a = 0;
            b = 0;
            value = 0;
            for (int j = 0; j < n; j++)
            {
                if (j < i) a ^= candy[j];
                else
                {
                    b ^= candy[j];
                    value += candy[j];
                }
            }
            if (a == b)
            {
                flag = true;
                break;
            }
        }
        cout << "Case #" << cs << ": ";
        if (flag) cout << value << endl;
        else cout << "NO" << endl;
    }
    return 0;
}
        
