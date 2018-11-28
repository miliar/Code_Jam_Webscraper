#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef vector<vector<int> > mtrx;

mtrx mul(mtrx a,mtrx b)
{
    mtrx c(2,vector<int>(2));
    for(int i=0;i<2;i++)
        for(int j=0;j<2;j++)
            for(int k=0;k<2;k++)
            {
                c[i][k] += a[i][j]*b[j][k];
                c[i][k] %= 1000;
            }
    return c;
}

mtrx pow(mtrx a, int n)
{
    mtrx ret(2,vector<int>(2));
    if(n==0)
    {
        ret[0][0]=ret[1][1]=1;
        return ret;
    }
    ret = pow(mul(a,a),n/2);
    if(n%2)
        ret = mul(ret,a);
    return ret;
}

int tst(int n)
{
    if(n==0)
        return 1;
    mtrx ret(2,vector<int>(2));
    ret[0][0]=6;
    ret[0][1]=1000-4;
    ret[1][0]=1;
    ret[1][1]=0;

    ret = pow(ret,n-1);
    int r = (ret[0][0]*6+ret[0][1]*2)%1000;
    return (r+999)%1000;
}

string fil(int r)
{
    if(r<10)
        return "00";
    if(r<100)
        return "0";
    return "";
}

int main()
{
    int n;
    cin >> n;
    for(int i=1;i<=n;i++)
    {
        int x;
        cin >> x;
        int r = tst(x);
        cout << "Case #" << i << ": " << fil(r) << r << endl;
    }
}
