


#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() 
{
    int t;
    cin >> t;
    for(int i =0; i < t;++i)
    {
        int n;
        cin >> n;
        vector<int> c;
        for(int j = 0 ; j < n; ++j)
        {
            int temp;
            cin >> temp;
            c.push_back(temp);
        }
        int limite = 1 << c.size();
        int max_suma = 0;
        bool found = false;
        for(int k = 1 ; k <limite-1; ++k )
        {
            vector<int> sean, patrick;
            int suma_real_sean = 0;
            int suma_sean = 0;
            int suma_patrick = 0;
            int temp = k;
            for(int j=0; j < n; ++j)
            {
                if(temp % 2 ==0)
                {
                    sean.push_back(c[j]);
                    suma_sean = suma_sean ^ c[j];
                    suma_real_sean += c[j];
                }
                else
                {
                    patrick.push_back(c[j]);
                    suma_patrick = suma_patrick ^ c[j];
                }
                temp = temp >> 1;
            }
            if(suma_patrick == suma_sean) 
            {
                found = true;
                if(suma_real_sean > max_suma)
                {
                    max_suma = suma_real_sean;
                }
            }
        }
        if(!found)
        {
            cout << "Case #" << i+1 << ": NO" << endl;
        }
        else
        {
            cout << "Case #" << i+1 << ": " << max_suma<< endl;
        }
    }
    return 0;
}
