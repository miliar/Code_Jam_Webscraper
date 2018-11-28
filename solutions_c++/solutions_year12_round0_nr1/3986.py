#include <fstream>
#include <cstdio>
using namespace std;

ifstream cin("a.in");
ofstream cout("a.out");

char map[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
              'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
    int n;
    freopen("a.in", "r", stdin);
    scanf("%d\n", &n);

    string a;
    getline(cin, a);

    for(int i = 1; i <= n; i++)
    {
        getline(cin, a);
        for(int j = 0; j < a.size(); j++)
        {
            if(a[j] >= 'a' && a[j] <= 'z')
                a[j] = map[ a[j] - 'a' ];
        }
        cout << "Case #" << i << ": "<< a << endl;
    }

    return 0;
}
