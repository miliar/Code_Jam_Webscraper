#include <iostream>
#include <map>
#include <iomanip>
using namespace std;

int main()
{
    int T; 
    cin >> T;
    while(T--)
    {
        int N;
        cin >> N;

        int s[256];
        int total = 0;
        for(int i = 0; i < N; i++)
            cin >> s[i], total += s[i];

        int tmp = total;
        int alc[256] = {};
        double ans[256] = {};
        while(total)
        {
            map<int, int> table;
            for(int i = 0; i < N; i++)
                table[s[i] + alc[i]]++;
        
            if(table.size() == 1)
                break;
            
            map<int, int>::iterator it = table.begin();

            int a = it->first;
            int b = it->second;
            int c = (++it)->first;

            if((c - a) * b > total)
                break;

            for(int i = 0; i < N; i++)
                if(s[i] + alc[i] == a)
                    alc[i] += c - a, total -= c - a;
        }

        map<int, int> table;
        for(int i = 0; i < N; i++)
        {
            ans[i] = alc[i] / (double)tmp;
            table[s[i] + alc[i]]++;
        }

        for(int i = 0; i < N; i++)
            if(s[i] + alc[i] == table.begin()->first)
                ans[i] += (total / (double)table.begin()->second) / tmp;


        cout.precision(10);
        static int tn = 0;
        cout << "Case #" << ++tn << ":";
        for(int i = 0; i < N; i++)
            cout << " " << fixed << ans[i] * 100;
        cout << '\n';
    }

    return 0;
}
