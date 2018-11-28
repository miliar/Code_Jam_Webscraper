#include<iostream>
#include<conio.h>

using namespace std;

/*struct data
{
       bool r, c, d1, d2;
       data()
       {
             r = c = d1 = d2 = true;
       }
};*/

bool gowR(char **ar, int sr, int sc, int k, int n, char c)
{
     int p, q;
     p = sr,
     q = sc;
     int l = 0;
     while (q > 0 && ar[p][q - 1] == c) q--, l++;
     for (int i = sc; i < n; i++) if (ar[p][i] == c) l++; else break;
     if (l >= k) return true;
     return false;
}
bool gowC(char **ar, int sr, int sc, int k, int n, char c)
{
     int p, q;
     p = sr,
     q = sc;
     int l = 0;
     while (p > 0 && ar[p-1][q] == c) p--, l++;
     for (int i = sr; i < n; i++) if (ar[i][q] == c) l++; else break;
     if (l >= k) return true;
     return false;
}
bool gowD1(char **ar, int sr, int sc, int k, int n, char c)
{
     int p, q;
     p = sr,
     q = sc;
     int l = 0;
     while (p > 0 && q < n && ar[p-1][q+1] == c) p--, q++, l++;
     for (int i = sr, j = sc; i < n && j >= 0; i++, j--) if (ar[i][j] == c) l++; else break;
     if (l >= k) return true;
     return false;
}
bool gowD2(char **ar, int sr, int sc, int k, int n, char c)
{
     int p, q;
     p = sr,
     q = sc;
     int l = 0;
     while (p > 0 && q > 0 && ar[p-1][q-1] == c) p--, q--, l++;
     for (int i = sr, j = sc; i < n && j < n; i++, j++) if (ar[i][j] == c) l++; else break;
     if (l >= k) return true;
     return false;
}

bool search(char **ar, char c, int k, int n)
{
    /* data **br;
     br = new data*[n];
     for (int i = 0; i < n; i++) data[i] = new data[n];
     */
     for (int i = 0; i < n; i++)
     {
         for (int j = 0; j < n; j++)
         {
             if (ar[i][j] != c) continue;
             if (gowR(ar, i, j, k, n, c)) return true;
             if (gowC(ar, i, j, k, n, c)) return true;
             if (gowD1(ar, i, j, k, n, c)) return true;
             if (gowD2(ar, i, j, k, n, c)) return true;
         }
     }
     return false;   
}
void print(char **ar, int n)
{
     for (int i = 0; i < n; i++) {for (int j = 0; j < n; j++) cout << ar[i][j]; cout << endl;}
}
int main()
{
    freopen("A-large.in", "r", stdin);
     freopen("b.txt", "w", stdout);
    int t;
    int n;
    cin >> t;
    char **ar, **br;
    int l;
    char c;
    bool flag1, flag2;
    for (int i = 1; i <= t; i++)
    {
       cin >> n >> l;
        br = new char*[n];
        for (int j = 0; j < n; j++) br[j] = new char[n];
        ar = new char*[n];
        for (int j = 0; j < n; j++) ar[j] = new char[n];
        for (int j = 0; j < n; j++)
            for (int k = 0; k < n; k++) ar[j][k] = '.';
            
        int *cnt;
        cnt = new int [n];
        for (int j = 0; j < n; j++) cnt[j] = 0;
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                cin >> br[j][k];
                if (br[j][k] == '.') cnt[j]++;
            }
        }
        for (int j = 0; j < n; j++)
        {
            int ii = cnt[j];
            for (int k = 0; k < n; k++)
            {
                if (br[j][k] != '.') ar[j][ii++] = br[j][k];
            }
        }
        //print(ar, n);
        flag1 = search(ar, 'R', l, n);
        flag2 = search(ar, 'B', l, n);
        cout << "Case #" << i << ": ";
        if (flag1 && flag2) cout << "Both\n";
        else if (flag1) cout << "Red\n";
        else if (flag2) cout << "Blue\n";
        else cout << "Neither\n";
    }
    //getch();
    return 0;
}
