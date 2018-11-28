#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <math.h>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
using namespace std;

typedef long long ll;
#define pb push_back
#define mp make_pair
const int inf = 2000000000;
const double eps = 1e-9, Pi = 2 * acos(0.0);

char a[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
    ifstream cin ("input.txt");
    ofstream cout("output.txt");
    string s;
    getline(cin, s);
    int cur = 1;
    while (getline(cin, s))
    {
          cout << "Case #" << cur++ << ": ";
          for (int i = 0; i < s.length(); i++)
              if (s[i] != ' ')
                 s[i] = a[s[i] - 'a'];
          cout << s << endl;
    }
    
    return 0;
}
