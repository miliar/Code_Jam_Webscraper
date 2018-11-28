//#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream cin("B-large.in");
ofstream cout("out.txt");

int rez=0;
int suprising;

void func(int ukupno, int potrebno)
{
    if (ukupno<potrebno) return;
    if (ukupno/3>=potrebno)
    {
        rez++;
        return;
    }
    if ((ukupno-1)/3==potrebno-1)
    {
        rez++;
        return;
    }
    if ((ukupno/3==potrebno-1 || (ukupno+1)/3==potrebno-1) && suprising!=0)
    {
        rez++;
        suprising--;
        return;
    }
    return;
}

int main()
{
    int t;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        int n,tr;
        cin >> n >> suprising >> tr;
        rez=0;
        for (int j=0;j<n;j++)
        {
            int k=0;
            cin >> k;
            func(k,tr);
        }
        cout << "Case #" << i+1 << ": " << rez;
        if (i!=t-1) cout << endl;
    }
}
