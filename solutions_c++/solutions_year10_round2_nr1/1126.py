#include<iostream>
#include<vector>
#include<map>
#include<conio.h>

using namespace std;

struct data
{
       int val;
       int par;
};

int cnt;
vector<int> pars(string s, map<string, int> &M)
{
    vector<int> v;
    string s1;
    v.push_back(0);
    for (int i = 1; i < s.size(); i++)
    {
        if (s[i] != '/') s1 += s[i];
        else 
        {
             if (!M[s1]) M[s1] = cnt++;
             v.push_back(M[s1]);
             s1 = "";
        }
    }
    if (!M[s1]) M[s1] = cnt++;        
    v.push_back(M[s1]);
    return v;
}
void makeTree(vector<vector<data> > &u, vector<int> p)
{
     int par = -1;
     bool flag = false;
     data d;
     vector<data> v;
     for (int i = 0; i < p.size(); i++)
     {
         if (i < u.size())
         {
              flag = false;
              for (int j = 0; j < u[i].size(); j++)
              {
                  if (u[i][j].val == p[i] && u[i][j].par == par)
                  {
                 //     cout << "j1\n";
                      par = j;
                      flag = true;
                      break;
                  }
              }
              if (!flag)
              {
               //         cout << "j2\n";
                        d.val = p[i];
                        d.par = par;
                        u[i].push_back(d);
                        par = u[i].size() - 1;      
              }
         }
         else
         {
             //cout << "j3\n";
             d.val = p[i];
             d.par = par;
             v.push_back(d);
             u.push_back(v);
             v.clear();
             par = 0;
         }
     }
}
int addD(vector<vector<data> > &u, vector<int> p)
{
    int par = -1;
    bool flag = false;
    data d;
    vector<data> v;
    int x = 0;
    for (int i = 0; i < p.size(); i++)
    {
         if (i < u.size())
         {
              flag = false;
              for (int j = 0; j < u[i].size(); j++)
              {
                  if (u[i][j].val == p[i] && u[i][j].par == par)
                  {
                 //     cout << "j1\n";
                      par = j;
                      flag = true;
                      break;
                  }
              }
              if (!flag)
              {
               //         cout << "j2\n";
                        x++;
                        d.val = p[i];
                        d.par = par;
                        u[i].push_back(d);
                        par = u[i].size() - 1;      
              }
         }
         else
         {
             //cout << "j3\n";
             x++;
             d.val = p[i];
             d.par = par;
             v.push_back(d);
             u.push_back(v);
             v.clear();
             par = 0;
         }
    }
    return x;
}
void print(vector<int> v)
{
     for (int i = 0; i < v.size(); i++) cout << v[i] << " ";
     cout << endl;
}
void print1(vector<vector<data> > u)
{
     for (int i = 0; i < u.size(); i++)
     {
         for (int j = 0; j < u[i].size(); j++)
           cout << u[i][j].val << " ";
         cout << endl;
     }
     cout << endl;
}
int main()
{
    freopen("A.in", "r", stdin);
    freopen("a1.txt", "w", stdout);
    int t;
    cin >> t;
    int m, n;
    string s;
    vector<vector<data> > u;
    vector<data> v;
    vector<int> p;
    int ans;
    for (int cas = 1; cas <= t; cas++)
    {
        ans = 0;
        map<string, int> M;
        data d;
        d.val = 0;
        d.par = -1;
        v.push_back(d);
        u.push_back(v);
        cin >> n >> m;
        cnt = 1; 
        for (int i = 0; i < n; i++)
        {
            cin >> s;
            p = pars(s, M);
            //print(p);
            makeTree(u, p);
            //print1(u);
        }
        for (int i = 0; i < m; i++)
        {
            cin >> s;
            p = pars(s, M);
            ans += addD(u, p);
            //cout << ans << endl;
        }
        v.clear();
        u.clear();
        cout << "Case #" << cas << ": " << ans << endl;
    }
    getch();
    return 0;
}
