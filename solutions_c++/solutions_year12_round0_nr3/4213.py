#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<cmath>
#include<map>
using namespace std;

int main()
{
    int t,a,b,count = 0;
    ifstream fin("C-small-attempt2.in");
    ofstream fout("out.in");
    fin>>t;
    int ans = 0;
    while(t--)
    {
              fin>>a>>b;
              count++;
              
              vector < pair<int, int> > ans;
              if (a / 10 == 0)
              {
                    fout<<"Case #"<<count<<": 0"<<endl;
                    continue;
              }
              if (a / 100 == 0)
              {
                    for (int i = a; i <= b; i++)
                    {
                        if ( i % 10 == 0)continue;
                        int c = (i%10)*10 + (i/10);
                        if ( i == c)continue;
                        if (c < i || c > b)continue;
                        pair <int, int> p1,p2;
                        p1.first = i;
                        p1.second = c;
                        p2.first = c;
                        p2.second = i;
                        bool found = false;
                        for (int j = 0; j < ans.size(); j++)
                        if (ans[j] == p2)
                        {found = true;break;}
                        if (!found)
                        {//cout << p1.first << " " << p1.second << endl;
                         ans.push_back(p1);}
                    }
                    fout<<"Case #"<<count<<": "<<ans.size()<<endl;
                    continue;
              }
              if (a / 1000 == 0)
              {
                    for (int i = a; i <= b; i++)
                    {
                        if ( i % 100 == 0)continue;
                        int c = (i%10)*100 + (i/10);
                        // cout << c << endl;
                        int d = (i%100)*10 + (i/100);
                        // cout << c << "   " << d << endl;
                        if ( i != c)
                        {
                             if (c < i || c > b)goto second;
                             if (c / 100 == 0)goto second;
                             pair <int, int> p1,p2;
                             p1.first = i;
                             p1.second = c;
                             p2.first = c;
                             p2.second = i;
                             bool found = false;
                             for (int j = 0; j < ans.size(); j++)
                             if (ans[j] == p2)
                             {found = true;break;}
                             if (!found)
                             {//cout << p1.first << " " << p1.second << endl;
                              ans.push_back(p1);}
                        }
                        second:
                        if ( i != d)
                        {
                             if (d < i || d > b)continue;
                             if (d/100 == 0)continue;
                             pair <int, int> p1,p2;
                             p1.first = i;
                             p1.second = d;
                             p2.first = d;
                             p2.second = i;
                             bool found = false;
                             for (int j = 0; j < ans.size(); j++)
                             if (ans[j] == p2)
                             {found = true;break;}
                             if (!found)
                             {//cout << p1.first << " " << p1.second << endl;
                              ans.push_back(p1);}
                        }
                        // system("pause");
                    }
                    fout<<"Case #"<<count<<": "<<ans.size()<<endl;
                    continue;
              }
              else
              {
                    fout<<"Case #"<<count<<": 0"<<endl;
              }
    }
    // system("pause");
    return 0;
}

// 1 QFT 1 QF 7 FAQFDFQ
