#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#define cin fin
#define cout fout
using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");


int main()
{
    int t;
    cin>>t;
    for(int qw=1;qw<=t;qw++)
    {
            vector<int> scores;
    int n, s, p, tem;
    cin>>n>>s>>p;
    p--;
    for(int i=1;i<=n;i++)
    {
            cin>>tem;
            scores.push_back(tem);
    }
    sort(scores.begin(), scores.end());
    int sol=0;
    for(int i=n-1;i>=0;i--)
    {
            if((scores[i]+2)/3>p)
            {
                         sol++;
                         continue;
            }
            if((scores[i]+2)/3==p)
            {
                 if(s==0)
                         break;
                 if(scores[i]<2)
                                break;
                 if(scores[i]%3==1)
                           continue;
                     sol++;
                     s--;
            }
            if((scores[i]+2)/3<p)
                         break;
    }
    cout<<"Case #"<<qw<<": "<<sol<<'\n';
    }
    system("pause");
}
