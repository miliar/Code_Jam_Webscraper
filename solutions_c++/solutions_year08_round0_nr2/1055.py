#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct data
{
    int arrive;
    int depart;
    int station;
}
temp;

bool cmp(data a, data b)
{
    if(a.depart != b.depart) return a.depart < b.depart;
    return a.arrive < b.arrive;
}

int main()
{
    freopen("B.in","r",stdin); freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int T=1; T<=t; T++)
    {
        int turnover;
        cin >> turnover;
        int na, nb;
        cin >> na >> nb;
        vector <data> v;
        for(int i=0; i<na; i++)
        {
            int a, b, c, d;
            scanf("%d:%d %d:%d", &a, &b, &c, &d);
            temp.depart = a*60 + b;
            temp.arrive = c*60 + d;
            temp.station = 1;
            v.push_back(temp);
        }
        for(int i=0; i<nb; i++)
        {
            int a, b, c, d;
            scanf("%d:%d %d:%d", &a, &b, &c, &d);
            temp.depart = a*60 + b;
            temp.arrive = c*60 + d;
            temp.station = -1;
            v.push_back(temp);
        }
        sort(v.begin(), v.end(), cmp);
        bool vis[na+nb];
        memset(vis, 0, sizeof(vis));
        int A = 0, B = 0;
        for(int i=0; i<v.size(); i++) if(vis[i] == 0)
        {
            vis[i] = 1;
            if(v[i].station == 1) A++;
            else B++;
            
            int start = v[i].arrive + turnover;            
            int station = -v[i].station;
            for(int j=i+1; j<v.size(); j++) if(vis[j] == 0 && v[j].station == station && v[j].depart >= start)
            {
                vis[j] = 1;
                start = v[j].arrive + turnover;
                station = -v[j].station;
            }
        }
        
        printf("Case #%d: %d %d\n", T, A, B);
    }
}
