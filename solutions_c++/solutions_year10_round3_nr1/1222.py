#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

struct wire
{
      long long a;
      long long b;
};

int main()
{
    freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
    
    int T, N;
    long long a, b, intersect;
    vector<wire> builds;
    vector<wire>::iterator it;
    wire w;
    
    cin >> T;
    
    for (int t = 0; t < T; t++) // Tests
    {
        cin >> N;
        intersect = 0;
        builds.clear();
        
        for (int n = 0; n < N; n++)
        {
            cin >> a >> b;
            
            for (it = builds.begin(); it < builds.end(); it++)
            {
                if ((it->a > a && it->b < b) || (it->a < a && it->b > b))
                   intersect++;
            }
            w.a = a;
            w.b = b;
            builds.push_back(w);
        }
        
        cout << "Case #" << t + 1 << ": " << intersect << endl;
    }
    
    return 0;  
}
