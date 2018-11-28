//#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream cin("B-small-attempt2.in");
ofstream cout("izlaz.txt");

int rezultat;
int sup;

void func(int ukp, int potrebno);

int main()
{
    int t;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        int n,tr;
        cin >> n >> sup >> tr;
        rezultat=0;
        for (int j=0;j<n;j++)
        {
            int k=0;
            cin >> k;
            func(k,tr);
        }
        cout << "Case #" << i+1 << ": " << rezultat;
        if (i!=t-1) cout << endl;
    }
}
void func(int ukp, int potrebno)
{
    if (ukp<potrebno) return;
    if (ukp/3>=potrebno)
    {
        rezultat++;
        return;
    }
    if ((ukp-1)/3==potrebno-1)
    {
        rezultat++;
        return;
    }
    if ((ukp/3==potrebno-1 || (ukp+1)/3==potrebno-1) && sup!=0)
    {
        rezultat++;
        sup--;
        return;
    }
    return;
}
