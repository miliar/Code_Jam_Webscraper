#include <iostream>
#include <vector>
#include <algorithm>

const int MAX_BUTTONS=1000;

using namespace std;

//Orange == 0
//Blue == 1

int combination[30][30];
int bad_combination[30][30];
int my_set[30];

int main ()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests_count;
    cin >> tests_count;
    
    for (int test_num=0; test_num<tests_count; test_num++)
    {
        int n;
        cin >> n;
        int sum=0;
        int mini=1000000000;
        int for_xor=0;
        for (int i=0; i<n; i++)
        {
            int x;
            cin >> x;
            sum+=x;
            mini=min(mini, x);
            for_xor=for_xor^x;
        }
        
        cout << "Case #" << test_num+1 << ": ";
        if (for_xor==0) cout << sum - mini << endl;
        else cout << "NO\n";        
    }
    
    return 0;
}

