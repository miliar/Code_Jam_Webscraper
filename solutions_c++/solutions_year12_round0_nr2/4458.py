#include <iostream>
#include <vector>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <cstdio>
#include <string>
#include <utility>
#include <string>

using namespace std;

const bool input = 0;

long long solve(vector<long long> &tmp, int s, int p)
{
    //cout << "sdfsdf";
    long long i = 0, min = 10, j, rez = 0;
    sort(tmp.begin(), tmp.end());
    reverse(tmp.begin(), tmp.end());
    while((tmp[i] + 2) / 3 >= p)
    {
        i++;
        //cout << "dsfsdfsd";
        if(i == tmp.size())
            break;
    }
    rez += i;
    //cout << "i: " << i << "\n";
    for(j = i; j < tmp.size(); j++)
    {
        if(tmp[j] < 29 && tmp[j] > 1 && s > 0)
        {
            if(((tmp[j] + 1)/ 3) + 1 >= p)
            {
                rez++;
            }
            s--;
        }
        else
            break;
    }
    //cout << rez << "\n";
    return rez;
}

int main()
{
     if(input)
    {
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    }
    string Googlerese("yhesocvxduiglbkrztnwjpfmaq");
    long long n, t, i, p, s, j, x, ans;
    char c;
    vector<long long> tmp;
    cin >> t ;
    for(i = 0; i < t; i++)
    {
        tmp.clear();
        cin >> n >> s >> p;
        for(j = 0; j < n; j++)
        {
            cin >> x;
            tmp.push_back(x);
        }
        ans = solve(tmp, s, p);
        cout << "Case #" << i + 1 << ": " << ans << "\n";
    }
    return 0;
}
