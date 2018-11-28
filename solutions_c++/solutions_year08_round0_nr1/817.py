#include <iostream>
#include <map>

using namespace std;

int *best, *next;

int main()
{
    int n;
    cin >> n;
    best = new int[100];
    next = new int[100];
    for (int c = 1; c <= n; c++)
    {
        int s, q;
        map<string, int> nameMap;
        cin >> s >> ws;
        for (int i = 0; i < s; i++)
        {
            string name;
            getline(cin, name);
            nameMap[name] = i;
        }

        for (int i = 0; i < s; i++)
            best[i] = 0;

        cin >> q >> ws;
        for (int i = 0; i < q; i++)
        {
            string name;
            getline(cin, name);
            int index = nameMap[name];
            next[index] = 10000;
            for (int j = 0; j < s; j++)
            {
                if (j == index)
                    continue;
                next[j] = best[j];
                for (int k = 0; k < s; k++)
                {
                    int inc = best[k] + 1;
                    if (inc < next[j])
                        next[j] = inc;
                }
            }

            swap(next, best);
        }

        int min = best[0];
        for (int i = 1; i < s; i++)
            if (best[i] < min)
                min = best[i];

        cout << "Case #" << c << ": " << min << endl;
    }
}
