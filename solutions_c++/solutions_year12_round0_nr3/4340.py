#include<iostream>
#include<cmath>
#include<fstream>

using namespace std;

int digcount(int a)
{
    int count = 0;
    while(a != 0)
    {
        a = a/10;
        count += 1;
    }
    return(count);
}

bool inlist(int a[100], int b, int size)
{
    for(int i = 0; i < size; i++)
        if(a[i] == b)
            return true;
    return false;
}

int list(int a, int u)
{
    int count = 0, rec = a, poss[4];
    int i;
    for(i = 0; i < digcount(a); i++)
    {
        rec = (rec % 10) * pow(10, (digcount(a)-1)) + rec/10;
        if(rec > a && rec <= u && !inlist(poss, rec, count))
        {
            poss[i] = rec;
            count += 1;                    
        }
    }
    return(count);
}
int count(int l, int u)
{
    int grand_total = 0, i;
    for(i = l; i <= u; i++)
        grand_total += list(i, u);
    return(grand_total);
}

int main()
{
    int cases, i, l, u;
    fstream x, y;
    x.open("C-small-attempt0.in", ios::in);
    y.open("recycle.txt", ios::out);
    x >> cases;
    x.seekg(3, ios::beg);
    for(i = 0; i < cases; i++)
    {
        x >> l >> u;
        y << "Case #" << i + 1 << ": " << count(l, u) << endl;
    }
    x.close();
    y.close();
    return 0;
}
