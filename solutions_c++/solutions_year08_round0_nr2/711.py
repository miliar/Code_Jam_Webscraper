#include <iostream>
#include <string>
using namespace std;
int T, NA, NB;

struct Time
{
    int be_hh;
    int be_mm;
    int ed_hh;
    int ed_mm;
}TA[101], TB[101];

bool fress(Time a, Time b)
{
    return ((a.be_hh<b.be_hh) 
            || ((a.be_hh==b.be_hh)&&(a.be_mm<b.be_mm)));
};

bool fress1(Time a, Time b)
{
    return ((a.ed_hh<b.ed_hh) 
            || ((a.ed_hh==b.ed_hh)&&(a.ed_mm<b.ed_mm)));
};

bool Compare(Time A, Time B)
{
    int a, b;
    if (B.ed_mm+T>=60)
    {
        a = B.ed_mm + T - 60;
        b = B.ed_hh + 1;
    }
    else
    {
        a = B.ed_mm + T;
        b = B.ed_hh;
    }
    
    if (A.be_hh>b)
    {
        return true;
    }
    else
    if ((A.be_hh==b) && (A.be_mm>=a))
    {
        return true;
    }
    else
    {
        return false;
    }
};

void Solve(int &ans_A, int &ans_B)
{
    sort(TB, TB+NB, fress1);
    sort(TA, TA+NA, fress);
    for (int i=0, j=0; i<NA; i++)
    {
        if (j<NB && Compare(TA[i], TB[j]))
        {
                j++;
        }
        else
        {
                ans_A++;
        }
    }
    
    sort(TA, TA+NA, fress1);
    sort(TB, TB+NB, fress);
    for (int i=0, j=0; i<NB; i++)
    {
        if (j<NA && Compare(TB[i], TA[j]))
        {
                j++;
        }
        else
        {
                ans_B++;
        }
    }
};
int main()
{
    int cases;
    int ii = 1;
    cin >> cases;
    while (cases--)
    {
        cin >> T >> NA >> NB;
        string begain, end;
        for (int i=0; i<NA; i++)
        {
                cin >> begain >> end;
                TA[i].be_hh = int(begain[0]-'0')*10+int(begain[1]-'0');
                TA[i].be_mm = int(begain[3]-'0')*10+int(begain[4]-'0');
                TA[i].ed_hh = int(end[0]-'0')*10+int(end[1]-'0');
                TA[i].ed_mm = int(end[3]-'0')*10+int(end[4]-'0');
        }
        
        for (int i=0; i<NB; i++)
        {
                cin >> begain >> end;
                TB[i].be_hh = int(begain[0]-'0')*10+int(begain[1]-'0');
                TB[i].be_mm = int(begain[3]-'0')*10+int(begain[4]-'0');
                TB[i].ed_hh = int(end[0]-'0')*10+int(end[1]-'0');
                TB[i].ed_mm = int(end[3]-'0')*10+int(end[4]-'0');
        }
        
        /*for (int i=0; i<NA; i++)
        {
                cout << TA[i].be_hh << ":" <<TA[i].be_mm << " "
                     << TA[i].ed_hh << ":" << TA[i].ed_mm << endl;
        }
        for (int i=0; i<NB; i++)
        {
                cout << TB[i].be_hh << ":" <<TB[i].be_mm << " "
                     << TB[i].ed_hh << ":" << TB[i].ed_mm << endl;
        }*/
        int ans_A = 0, ans_B = 0;
        Solve(ans_A, ans_B);
        cout << "Case #" << ii << ": " << ans_A << " " << ans_B << endl;
        ii++;
    }
    return 0;
}
