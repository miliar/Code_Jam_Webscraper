#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector <int> num;

int main()
{
    int xor1,xor2,sum;

    int n,m;
    int id;
    cin >> n;
    for (int i=0; i<n; ++i)
    {
        cin >> m;
        num.clear();

        for (int j=0; j<m; ++j)
        {
            cin >> id;
            num.push_back(id);
        }
        sort(num.begin(),num.end());
        xor1=0;
        sum=0;
        xor2=num[0];
        for (int j=1; j<m; ++j)
        {
            xor1=xor1^num[j];
            sum=sum+num[j];
        }
        for (int j=1; j<m; ++j)
        {
            if (xor1==xor2) {break;}
            xor1=xor1^num[j];
            xor2=xor2^num[j];
            sum=sum-num[j];
        }
        if (sum!=0)
        {
                cout <<"Case #" <<i+1 << ": "<< sum << endl;
        }
        else
        {
            cout <<"Case #" <<i+1 << ": NO" << endl;
        }

    }
    return 0;
}
