#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()
{
    int N,S,Q;
    cin >> N;
    for (int ti = 0; ti < N; ++ ti)
    {
        cin >> S;
        string s;
        getline(cin,s);
        map<string,int> engines_map;
        for (int si = 0; si<S; ++si)
        {
            getline(cin,s);
            engines_map.insert(make_pair(s,si));
        }

        int zeros = S;
        vector<int> flag(S,0);

        cin >> Q;
        getline(cin,s);
        int count = 0;

        for (int qi = 0; qi<Q; ++qi)
        {
            getline(cin,s);
            int e = engines_map[s];
            if (!flag[e])
            {
                flag[e] = 1;
                zeros --;
            }
            if(zeros==0)
            {
                count ++;
                zeros = S-1;
                flag = vector<int>(S,0);
                flag[e] = 1;
            }
        }

        cout << "Case #" << ti+1 << ": " << count << endl;
    }
    return 0;
}
