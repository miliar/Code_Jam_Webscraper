#include <iostream>
#include <vector>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int caseNum, i, n, tmp;
    int k, pow;
    cin >> caseNum;
    for(i = 0; i < caseNum; ++i)
    {
        cin >> n >> k;
        tmp = pow = 1;
        //cout << n << k;
        while(tmp <= n)
        {
            pow *= 2;
            tmp++;
        }
        //cout << "pow" << pow << endl;

        cout << "Case #" << i + 1<< ": ";
        if((k+1) % pow ==0) cout << "ON"<<endl;
        else cout << "OFF" << endl;
    }

    return 0;
}
