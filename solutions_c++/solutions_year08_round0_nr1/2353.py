#include<iostream>
#include<vector>
#include<string>
#include<conio.h>

using namespace std;

string getstring(void)
{
    int c;
    string t;
    for (; ;)
    {
        c = getch();
        if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c == ' ') || (c >= '0' && c <= '9'))
            t.push_back(char(c));
        else break;
    }
    return t;
}

bool allappeared(bool* Tn)
{
    for (int i = 0; i < (sizeof (Tn) / sizeof (bool)); ++i)
        if (Tn[i] == false) return false;
    for (int i = 0; i < (sizeof (Tn) / sizeof (bool)); ++i)
        Tn[i] = false;
    return true;
}

int findit(vector <string>& P, string t)
{
    for (int i = 0; i < P.size(); ++i)
        if (P[i] == t) return i;
}

int main(void)
{
    vector <string> P, Q;
    int N;
    cin >> N;

    for (int i = 1; i <= N; ++i) {

        int Pn;
        cin >> Pn;
        for (int j = 0; j < Pn; ++j) P.push_back(getstring());

        int Qn;
        cin >> Qn;
        for (int j = 0; j < Qn; ++j) {
            string t = getstring();
            if (j > 1 && t == Q[Q.size() - 1]) continue;
        }

        

   
        int result = 0;
        bool Tn[Pn];
        for (int j = 0; j < Pn; ++j) Tn[j] = false;
        for (int j = 0; j < Q.size(); ++j) {
            int t = findit(P, Q[j]);
            if (!Tn[t]) Tn[t] = true;
            if (allappeared(Tn)) {
                ++result;
                Tn[t] = true;
            }
        }
        cout << "Case #" << i << ": " << result << endl;

        P.clear();
        Q.clear();
    }
    return 0;
}
