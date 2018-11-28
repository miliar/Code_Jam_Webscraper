#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>

using namespace std;

inline string GetName(void)
{
    string t;
    for (; ;) {
        int c = cin.get();
        if (t.empty() && !((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c == ' ') || (c >= '0' && c <= '9')))
            continue;
        if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c == ' ') || (c >= '0' && c <= '9'))
            t.push_back(char(c));
        else break;
    }
    return t;
}

inline int find(vector <string>& S, string s)
{
    for (int i = 0; i < S.size(); ++i) if (S[i] == s) return i;
    exit(0);
}

inline bool appeared(bool* T, int n)
{
    for (int i = 0; i < n; ++i) 
        if (!T[i]) return false;
    return true;
}


int main(void)
{
    int N;
    cin >> N;
    for (int i = 1; i <= N; ++i) {
        vector <string> P, Q;
       
        int Pn;
        cin >> Pn;
        for (int j = 0; j < Pn; ++j) P.push_back(GetName());
    
        int Qn;
        cin >> Qn;
        for (int j = 0; j < Qn; ++j) {
            string str = GetName();
            if (j > 0 && str == Q[Q.size() - 1]) continue;
            Q.push_back(str);
        }
       
        int result = 0;
        bool T[Pn];
        for (int j = 0; j < Pn; ++j) T[j] = false;
        for (int j = 0; j < Q.size(); ++j) {
            int no = find(P, Q[j]);
            T[no] = true;
            if (appeared(T, Pn)) {
                for (int k = 0; k < Pn; ++k) T[k] = false;
                ++result;
                T[no] = true;
            }
        }
        
        cout << "Case #" << i << ": " << result << endl;

    }
    return 0;
}
