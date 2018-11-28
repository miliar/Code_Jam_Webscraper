#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int map[600][600];
bool check(int x, int y , int l ) { 
     for (int i = 0; i<l; i++)
       for (int j = 0; j<l; j++)
         if ((map[i+y][j+x]<0)||((map[i+y][j+x]+i+j) % 2!=map[y][x])) return false;
     
     return true;
}
int fill(int x, int y ,int l ) 
{
     for (int i = 0; i<l; i++)
       for (int j = 0; j<l; j++)
          map[i+y][j+x] = -1;
     return 0;
}
int main()
{
    int n0; int nn; cin>> nn; for (n0 = 1; n0<=nn; n0++) {
        int n , m ;
        cin >> m  >> n;
        memset(map,0,sizeof(map));
        for (int i = 1 ; i <=m; i++)  {
            string s;
            cin >> s;
            for (int j = 0; j<n/4; j++) {
                //0123 4567 89AB CDEF h
                if ((s[j]>='A')||(s[j]>='8')) map[i][4*j+1] =1;
                if ((s[j]=='2')||(s[j]=='3')||(s[j]=='6')||(s[j]=='7')||(s[j]=='A')||(s[j]=='B')||(s[j]=='E')||(s[j]=='F'))
                    map[i][4*j+3] =1;
                if ((s[j]=='1')||(s[j]=='3')||(s[j]=='5')||(s[j]=='7')||(s[j]=='9')||(s[j]=='B')||(s[j]=='D')||(s[j]=='F'))
                    map[i][4*j+4] =1;
                if ((s[j]>='C')||((s[j]<'8')&&(s[j]>='4'))) map[i][4*j+2] = 1;
            }
        }
  /*      for (int i = 1; i<=m; i++) {
            for (int j =1; j<=n; j++)
               cout <<map[i][j];
            cout << endl;
        }
        cout << endl;
    */        int ans = 0 ;
            int list[600],id[600];
            memset(list,0,sizeof(list));
            for (int l = min(m,n); l>=1; l--) { bool flag =false; 
            for (int y = 1; y<=m-l+1; y++)
              for (int x =1; x<=n-l+1; x++)
                if (check(x,y,l)) {
                  if (!flag) { flag = true; ans++; id[ans]=l;}
                  list[ans]++;
                  fill(x,y,l);
                }
              }
        
        cout << "Case #"<<n0<<": "<<ans <<endl;
        for (int i = 1; i<=ans;i++) cout << id[i] <<' '<< list[i] << endl;
    }
}
