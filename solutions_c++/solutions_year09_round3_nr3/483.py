#include <iostream>
using namespace std;
bool used[100];
int p, q, qm[100], a[100], mins;
int f()
{
    int i, ctr = 0, c;
    bool released[10001] = {false};
    for(i = 0; i < q; i++)
    {
        released[a[i]] = true;
        c = a[i] - 1;
        while(c > 0 && !released[c])
        {
            ctr++;
            c--;
        }
        c = a[i] + 1;
        while(c <= p && !released[c])
        {
            ctr++;
            c++;
        }
    }
    return ctr;
}
void permute(int c)
{
    int i;
    if(c == q)
    {
        int temp = f();
        if(mins > temp)
            mins = temp;
        return;
    }
    for(i = 0; i < q; i++)
        if(!used[i])
        {
            used[i] = true;
            a[c] = qm[i];
            permute(c + 1);
            used[i] = false;
        }
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n, i, j;
    cin >> n;
    for(i = 1; i <= n; i++)
    {
        mins = 1000000;
        cin >> p >> q;
        for(j = 0; j < q; j++)
            cin >> qm[j];
        for(j = 0; j < q; j++)
            used[j] = false;
        permute(0);
        cout << "Case #" << i << ": " << mins << endl;;
    }
    return 0;
}
