#include <iostream>
using namespace std;

void printline (int i,long res,long sum,long mn)
{
    cout << "Case #" << i+1 << ": ";
    if (res) cout <<"NO\n";
    else cout << sum-mn << endl;

}

int main()
{
    int T,N;
    long res,temp,sum,mn;
    cin >>T;
    for (int i=0;i<T;i++)
    {
        cin >> N;
        sum = res = 0;
        for (int j=0;j<N;j++)
        {   
            cin >>temp;
            mn = (j==0?temp:
                  temp>mn?mn:temp);
            sum+=temp;
            res = res^temp;
        }
        printline(i,res,sum,mn);
    }
    return 0;
}
