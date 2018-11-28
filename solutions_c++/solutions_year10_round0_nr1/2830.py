#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int num_test_cases = 0;
    cin >> num_test_cases;
    string junk;
    getline(cin, junk);

    for(int i = 1; i <= num_test_cases; i++)
    {
        int n = 0, k = 0;
        cin >> n >> k;
        getline(cin, junk);
        
        cout << "Case #" << i << ": ";
        if((k + 1) % (int)pow(2,(double)n) == 0)
            cout << "ON\n";
        else
            cout << "OFF\n";
    }
    
    return 0;
}

        
