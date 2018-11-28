#include <iostream>
using namespace std;

int num[4][100];

void bigInput(int a)
{
    string str;
    cin>>str;
    int l = str.length();

    num[a][0] = l;
    for (int i=0; i<num[a][0]; ++i)
        num[a][l-i] = str[i] - '0';
}

void bigOut(int a)
{
    for (int i=num[a][0]; i>0; --i)
        cout<<num[a][i];
    cout<<endl;
}

bool isLarger(int a, int b)
{
    int l = num[a][0];
    if (num[b][0] > l)
        l = num[b][0];
    while (l>=2 && num[a][l] == num[b][l])
        --l;
    if (num[a][l] > num[b][l])
        return true;
    else return false;
}

bool isZero(int a)
{
    return num[a][0] == 0 ||
        num[a][0] == 1 && num[a][1] == 0;
}

void bigDel(int a, int b, int c)
{
    int comp = 0;
    for (int i=1; i<=num[a][0]; ++i)
    {
        int t = (i<=num[b][0])?num[b][i]: 0;
        
        if (num[a][i] >= t+comp)
        {
            num[c][i] = num[a][i] - t - comp;
            comp = 0;
        }
        else
        {
            num[c][i] = num[a][i] +10 - t - comp;
            comp = 1;
        }
    }
    
    num[c][0] = num[a][0];
    while (num[c][0]>1 && num[c][num[c][0]] == 0)
        --num[c][0];
}

void copy(int a, int b)
{
    for (int i=0; i<=num[a][0]; ++i)
        num[b][i] = num[a][i];
}

void bigLcd(int a, int b)
{
    do
    {
        if (isLarger(a,b))
            bigDel(a,b,a);
        else bigDel(b,a,b);
    }while (!isZero(b));
    
}

int main(){

    freopen("A-large.in","r",stdin);
    // freopen("input","r",stdin);
    int N;
    cin >> N;
    for (int tests=0; tests<N;++tests){
        cout << "Case #" << tests+1 << ": ";
        int n,k;
        cin >> n >> k;
        int t = 1;
        for (int i=0; i<n; ++i) t*=2;
        if (k%t == t-1)
            cout<<"ON";
        else cout<<"OFF";
        cout<<endl;
    }
}
