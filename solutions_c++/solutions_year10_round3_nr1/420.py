#include<iostream>
#include<algorithm>

using namespace std;

struct nod_t
{
       int a, b;
};
nod_t nod[1111];
int n;

bool cmp(const nod_t& a, const nod_t& b)
{
     if(a.a < b.a) return true;
     if(a.a==b.a && a.b<b.b) return true;
     return false;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int cas, icas;
    int i, j;
    cin >> cas;
    for(icas = 1; icas <= cas; icas++)
    {
             cout << "Case #" << icas << ": ";
             cin >> n;
             for(i = 1; i <= n; i++)
             {
                   scanf("%d %d", &nod[i].a, &nod[i].b);
             }
             sort(nod+1, nod+1+n, cmp);
             int sum = 0;
             for(i = 1; i <= n; i++)
             {
                   for(j = 1; j < i; j++)
                   {
                         if(nod[j].b > nod[i].b)
                             sum++;
                   }
             }
             cout << sum << endl;
    }
    return 0;
}
