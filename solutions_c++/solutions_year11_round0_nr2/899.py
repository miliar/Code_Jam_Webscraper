#include <iostream>
#include <vector>
using namespace std;

char combine[26][26];
bool opposite[26][26];
void solve()
{
     memset(combine, -1, sizeof(combine));
     memset(opposite, 0, sizeof(opposite)); 
     
     int C, N, D;
     cin >> C;
     for (int i = 0; i < C; i++)
     {
         char a[4];
         cin >> a;
         combine[ a[0] - 'A'][ a[1] - 'A' ] = 
         combine[ a[1] - 'A'][ a[0] - 'A' ] = a[2] - 'A';         
     }
     cin >> D;
     for (int i = 0; i < D; i++)
     {
         char a[3];
         cin >> a;
         opposite[ a[0] - 'A'][ a[1] - 'A' ] = 
         opposite[ a[1] - 'A'][ a[0] - 'A' ] = 1;
     }
     
     cin >> N;
     char niz[101];
     vector<int> rez;
     cin >> niz;
     for (int i = 0; i < N; i++)
     {
         int num = niz[i] - 'A';
         
         if (rez.empty()) rez.push_back(num);
         else
         {
             int num2 = rez.back();
             if (combine[num][num2] != -1)
             {
                  rez.pop_back();
                  rez.push_back(combine[num][num2]);
             }
             else
             {
                  rez.push_back(num);
             }
             
             for (int j = 0; j < rez.size() - 1; j++)
             {
                 if (opposite[rez[j]][rez.back()])
                 {
                       rez.clear();
                       break;
                 }
             }
         }
     }
     
     string ans = "[";
     for (int i = 0; i < rez.size(); i++)
     {
         if (i != 0) ans += ", ";
         ans += 'A'+rez[i];
     }
     ans += "]";
     cout << ans << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
}
