#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

typedef list<int> LI;
typedef LI::iterator LII;
typedef map <int, int> MII;
typedef MII::iterator MIII;
typedef vector<int> VI;
typedef vector<MII> VMII;
typedef VI::iterator VII;


#define fou(i, l) for (int i = 0, __l##i = (l); i < __l##i; i++)
#define fod(i, l) for (int i = (l) - 1; i >= 0; i--)

#define fouu(i, j, g) fou(i, (g).size()) fou(j, (g)[0].size())
#define fodd(i, j, g) fod(i, (g).size()) fod(j, (g)[0].size())


int main()
{
    int T;

    cin >> T;
    fou(i, T)
    {
    	int N;
        MII m;
        LI b;

        cin >> N;
        fou(j, N) 
        {
            int A, B;
            cin >> A >> B;
            m[A] = B;
            b.push_back(B);
        }
        b.sort();
        int s = 0;
        for (MIII mi = m.begin(); mi != m.end(); mi++)
            for(LII li = b.begin(); li != b.end(); li++)
            {
                if (*li >= mi->second) 
                {
                    b.erase(li);
                    break;
                }
                s++;
            }
        cout << "Case #" << i + 1 << ": " << s << endl;
    }

    return 0;
}

