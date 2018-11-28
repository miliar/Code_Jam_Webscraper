#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    //ifstream cin("A-small-attempt0.in");
    ifstream cin("A-small-attempt1.in");
    ofstream cout("A-out.txt");

    int N;
    string str;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        char used[1000] = {false};
        int numUnique = 0;
        cin >> str;
        for (int j = 0; j < str.length(); j++)
        {
            if (!used[str[j]])
            {
                used[str[j]] = true;
                numUnique++;
            }
        }
        int minBase = numUnique;
        if (minBase == 1)
            minBase = 2;
        int used2[1000];
        int digits[1000];
        for (int k = 0; k < 1000; k++)
        {
            digits[k] = -1;
            used2[k] = -1;
        }

        digits[0] = 1;
        used2[str[0]] = 1;
        int idx = 0;
        for (int k = 1; k < str.length(); k++)
        {
            if (used2[str[k]] != -1)
            {
                digits[k] = used2[str[k]];
            }
            else
            {
                digits[k] = idx;
                used2[str[k]] = idx;
                if (idx == 0)
                {
                    idx = 2;
                }
                else
                    idx++;
            }
        }

        int num = 0;
        int pow = str.length() - 1;
        int base = 1;
        for (int k = 0; k < pow; k++)
        {
            base *= minBase;
        }
        for (int k = 0; digits[k] != -1; k++)
        {
            num += digits[k] * base;
            base /= minBase;
        }
        cout << "Case #" << i+1 << ": " << num << endl;
    }
    
}



/*
    int num;
    string str;
    cin.get();
    for (int i = 0; i < N; i++)
    {
        getline(cin, str);

        stringstream instr(str);
        
        while (instr >> num)
        {
            cout << num << " ";
        }
        cout << endl;
    }
*/