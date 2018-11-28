#include <algorithm>
#include <deque>
#include <iostream>

using namespace std;

#define NMAX 10000

int n;
int d[NMAX];
int l[NMAX];
int dist;

int best_tried[NMAX];
int best_untried[NMAX];
deque<int> to_try;

void func(int i, int j)
{
    int k = min(d[j]-d[i], l[j]);
    if (k > best_tried[j] && k > best_untried[j])
    {
        if (best_untried[j] == 0)
            to_try.push_back(j);
        best_untried[j] = k;
    }
}

int main()
{
    int t, c;
    const char *result;
    int i, j;
    
    cin >> t;
    for (c = 1; c <= t; c++)
    {
        cin >> n;
        for (i=0; i<n; i++)
            cin >> d[i] >> l[i];
        cin >> dist;
        
        fill(best_tried, best_tried+n, 0);
        fill(best_untried, best_untried+n, 0);
        to_try.clear();
        result = "NO";
        
        best_untried[0] = d[0];
        to_try.push_back(0);
        while (!to_try.empty())
        {
            i = to_try.front();
            to_try.pop_front();
            if (best_untried[i] >= dist - d[i])
            {
                result = "YES";
                break;
            }
            for (j = i-1; j >= 0 && d[i]-d[j] <= best_untried[i]; j--)
            {
                func(i, j);
            }
            for (j = i+1; j < n && d[j]-d[i] <= best_untried[i]; j++)
            {
                func(i, j);
            }
            best_tried[i] = best_untried[i];
            best_untried[i] = 0;
        }
        
        cout << "Case #" << c << ": " << result << endl;
    }
    return 0;
}
