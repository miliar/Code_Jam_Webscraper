#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std;

string
order(char a, char b)
{
    string str;
    if(a>b){char temp;temp=a;a=b;b=temp;}
    str.push_back(a);
    str.push_back(b);
    return str;
}

bool found(char &rtn, map<string, char> m, string s)
{
    map<string, char>::iterator itr;
    bool __b = false;
    if((itr=m.find(s))!=m.end())
    {
        __b = true;
        rtn = itr->second;
    }
    return __b;
}

bool found(set<string> st, string s)
{
    bool __b = false;
    if(st.find(s)!=st.end())
    {
        __b = true;
    }
    return __b;
}

int main()
{
    int T, t;
    cin >> T;
    for (t = 0; t < T; ++t)
    {
        map<string, char> combine;
        set<string> oppos;
        int C, c_;
        cin >> C;
        for (c_ = 0; c_ < C; ++c_)
        {
            string str;
            cin >> str;
            combine[order(str[0], str[1])] = str[2];
        }
        int D, d;
        cin >> D;
        for (d = 0; d < D; ++d)
        {
            string str;
            cin >> str;
            oppos.insert(order(str[0], str[1]));
        }
        int N;
        cin >> N;
        string str;
        str.reserve(N);
        cin >> str;
        int cur = 1;
        while (cur < (int)str.length())
        {
            char cur_ch = str[cur];
            char comb;
            if(found(comb, combine, order(str[cur-1],cur_ch)))
            {
                str.replace(cur-1, 2, string(1, comb));
                cur_ch = str[cur];
            }
            int i;
            for (i = 0; i < cur; ++i)
            {
                if(found(oppos, order(str[i],cur_ch)))
                {
                    str.erase(0, cur + 1);
                    cur = 0;
                    break;
                }
            }
            ++cur;
        }
        cout << "Case #" << t + 1 << ": [";
        int i, n=str.length()-1;
        if (n>=0){
            for (i=0;i<n;++i)
            {
                cout << str[i] << ", ";
            }
            cout << str[n];
        }
        cout << "]" << endl;
    }
    return 0;
}
