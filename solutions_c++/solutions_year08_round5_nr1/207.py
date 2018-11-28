#include <string>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

int tst()
{
    int dx = 1;
    int dy = 0;
    int x=150;
    int y=150;
    vector<int> minx(300,1000000);
    vector<int> maxx(300,-1000000);
    vector<int> miny(300,1000000);
    vector<int> maxy(300,-1000000);
    int l;
    cin >> l;
    int area=0;
    for(int i=0;i<l;i++)
    {
       string s;
       cin >> s;
       int ile;
       cin >> ile;
       for(int j=0;j<ile;j++)
           for(int t=0;t<s.size();t++)
           {
               if(s[t]=='L')
               {
                   swap(dx,dy);
                   dx *= -1;
               }
               else if(s[t]=='R')
               {
                   swap(dx,dy);
                   dy *= -1;
               }
               else
               {
                   if(dx == 1)
                   {
                       area += y;
                       maxy[x] >?= y;
                       miny[x] <?= y;
                       x += dx;
                   }
                   else if(dx == -1)
                   {
                       area -= y;
                       x += dx;
                       maxy[x] >?= y;
                       miny[x] <?= y;
                   }
                   else if(dy == 1)
                   {
                       maxx[y] >?= x;
                       minx[y] <?= x;
                       y += dy;
                   }
                   else
                   {
                       y+=dy;
                       maxx[y] >?= x;
                       minx[y] <?= x;
                   }
               }


           }
    }

    int area2=0;
    for(int x=0;x<300;x++)
        for(int y=0;y<300;y++)
            if((x >= minx[y] && x < maxx[y]) || (y >= miny[x] && y < maxy[x]))
                area2++;
//    cout << area2 << ' ' << area << endl;
    return area2 - abs(area);
}
int main()
{
    int n;
    cin >> n;
    for(int i=0;i<n;i++)
    {
        printf("Case #%d: %d\n",i+1,tst());
    }

}
