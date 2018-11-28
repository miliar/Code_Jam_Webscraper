#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main(int, char**)
{
    int T;
    cin >> T;
    for(int ca = 1; ca <= T; ca++)
    {
        int C,D,N;
        cin >> C;
        bool opposed[256][256];
        char composite[256][256];
        for(int i=0; i<256; i++)
            for(int j=0; j<256; j++)
            {
                opposed[i][j] = false;
                composite[i][j] = 0;
            }
        for(int i=0; i<C; i++)
        {
            string s;
            cin >> s;
            composite[s[0]][s[1]] = composite[s[1]][s[0]] = s[2];
        }
        cin >> D;
        for(int i=0; i<D; i++)
        {
            string s;
            cin >> s;
            opposed[s[0]][s[1]] = opposed[s[1]][s[0]] = true;
        }
        cin >> N;
        string elements;
        cin >> elements;
        char el[100];
        int s = 0;
        for(int i=0; i<N; i++)
        {
            el[s++]=elements[i];
            if(s > 1)
            {
                char c;
                if(c = composite[el[s-1]][el[s-2]])
                {
                    el[s-2]=c;
                    s--;
                }
            }
            for(int j=0; j<s; j++)
                if(opposed[el[s-1]][el[j]]) s=0;
        }

        cout << "Case #" << ca << ": [";
        for(int i=0; i<s; i++)
        {
            if(i) cout << ", ";
            cout << el[i];
        }
        cout <<"]\n";
    }
    return 0;
}
