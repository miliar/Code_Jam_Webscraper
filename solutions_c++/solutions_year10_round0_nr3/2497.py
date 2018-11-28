#include<iostream>
#include<queue>
using namespace std;
int main()
{
    int t,caso=1;
    unsigned long int r,k,n,g, res = 0;
    cin >> t;
    while (t--)
    {
        res = 0;
        queue<int> gs;
        cin >> r >> k >> n;
        for (unsigned long int i = 0; i < n; ++i)
        {
            cin >> g;
            gs.push(g);
        }
        for (unsigned long int i = 0; i < r; ++i)
        {
            bool lleno = false;
            int cant = 0;
            queue<int> gs1 = gs;
            while(!lleno)
            {
                int temp = gs1.front(), temp1 = gs.front();
                if(cant+temp > k || gs1.empty())
                    lleno = true;
                else
                {
                    cant+=temp;
                    gs1.pop();
                    gs.pop();
                    gs.push(temp1);
                }
            }
            res += cant;
        }
        cout << "Case #" << caso++ << ": " << res << endl;
    }
}
