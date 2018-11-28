#include <iostream>

using namespace std;


void testAlphabet(string& s, char a[3])
{
    if ((s[s.length() - 1] == a[0] && s[s.length() - 2] == a[1]) ||
        (s[s.length() - 1] == a[1] && s[s.length() - 2] == a[0]))
    {
        s = s.substr(0, s.length() - 2);
        s.push_back(a[2]);
    }
};

void testOpposed(string& s, char o[2])
{
    if (s.length() <= 1)
        return;
    if (s[s.length() - 1] == o[0])
    {
        for (int i = 0; i < s.length() - 1; ++i)
        {
            if (s[i] == o[1])
            {
                s.clear();
                break;
            }
        }
    }
    else if (s[s.length() - 1] == o[1])
    {
        for (int i = 0; i < s.length() - 1; ++i)
        {
            if (s[i] == o[0])
            {
                s.clear();
                break;
            }
        }
    }
};

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    
    
    for (int i = 0; i < t; ++i)
    {
        int c;
        cin >> c;
        char alphabet[c][3];
        for (int j = 0; j < c; ++j)
        {
            cin >> alphabet[j];
        }
        
        int d;
        cin >> d;
        char opposed[d][2];
        for (int j = 0; j < d; ++j)
        {
            cin >> opposed[j];
        }
        
        int n;
        cin >> n;
        char invoke[n];
        cin >> invoke;
        
        string out;
        for (int j = 0; j < n; ++j)
        {
            out.push_back(invoke[j]);
            for (int k = 0; k < c; ++k)
                testAlphabet(out, alphabet[k]);
            for (int k = 0; k < d; ++k)
                testOpposed(out, opposed[k]);
        }
        cout << "Case #" << i + 1 << ": [";
        for (int j = 0; j < static_cast<int>(out.length() - 1); ++j)
        {
            cout << out[j] << ", ";
        }
        if (!out.empty())
            cout << out[out.length() - 1];
        cout << "]" << endl;
    }
    return EXIT_SUCCESS;
}
