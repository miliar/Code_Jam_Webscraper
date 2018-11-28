#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outb-l.txt","w",stdout);

    vector <int> v;

    int cnt;
    cin >> cnt;
    for (int j=0; j<cnt; j++)
    {

        int n,s,p;
        cin >> n >> s >> p;

        for (int i=0; i<n; i++)
        {
            int x;
            cin >> x;
            v.push_back(x);
        }

        int ans=0;
        for (int i=0; i<n; i++)
        {
            if (v[i]!=0)
            {
                int b=v[i]/3;

                switch (v[i]%3)
                {
                    case 0:
                        if (b >= p)
                        {
                            ans++;
                        }
                        else
                        {
                            if (s > 0 && (b+1) >= p)
                            {
                                s--;
                                ans++;
                            }
                        }

                        break;
                    case 1:
                        if ((b+1) >= p)
                        {
                            ans++;
                        }

                        break;
                    case 2:
                        if (b+1 >= p)
                        {
                                ans++;
                        }
                        else
                        {
                            if (s > 0 && (b+2) >= p)
                            {
                                s--;
                                ans++;
                            }
                        }
                        break;
                }
            }
            else
            {
                if (v[i]>=p)
                {
                    ans++;
                }
            }
        }
        v.clear();
        cout << "Case #" << j+1 << ": " << ans << endl;
    }
    return 0;
}



