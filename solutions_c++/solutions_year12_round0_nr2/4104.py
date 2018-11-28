#include<iostream>

using namespace std;
int in[101];
int arr[101][3];
int main()
{
    int t, n, s, p, i, j, c, x;
    cin>>t;
    
    for (i =1; i<=t; ++i)
    {
        cin>>n>>s>>p;
        c = 0;
        x = s;
        for (j=0; j<n; ++j)
            cin>>in[j];
        for (j=0; j<n; ++j)
            arr[j][0] = in[j]/3 , arr[j][1] = in[j]%3;
        for (j=0; j<n; ++j)
        {
            if (arr[j][1] == 0)
            {
               if (arr[j][0] >= p)
               {
                  ++c;
               }
               else if ((arr[j][0]!=0 || arr[j][1]!=0) && (arr[j][0] + 1) >= p && x > 0 )
                    ++c , --x;
            }
            else if (arr[j][1] == 1)
            {
                 if ((arr[j][0] + 1) >= p)
                    ++c;
            }
            else if (arr[j][1] == 2)
            {
                 if ((arr[j][0] + 1) >= p)
                    ++c;
                 else if ((arr[j][0] + 2) >= p && x > 0)
                      ++c , --x;
            }
        }
        cout<<"Case #"<<i<<": "<<c<<endl;
    }
    return 0;
}
