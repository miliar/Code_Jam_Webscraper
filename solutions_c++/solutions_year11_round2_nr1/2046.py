#include <iostream>
#include <vector>
#include <fstream>


using namespace std;

long double wp(vector<int>& v)
{
    long double oss=0;
    long double p=0;
    for(int i=0;i<(int)v.size();i++)
    {
        if(v[i]!=-1)
        {
            oss++;
            p+=v[i];
        }
    }
    return (p/oss);
}

long double owp(vector<vector<int> >& table, int k)
{
    long double p=0;
    long double oss=0;
    for(int i=0;i<(int)table[k].size();i++)
    {
        if(table[k][i]!=-1)
        {
            vector<int> v;
            v=table[i];
            v[k]=-1;
            p+=wp(v);
            oss++;
        }
    }
    return p/oss;
}

long double oowp(vector<vector<int> >& table, int k)
{
    long double p=0;
    long double oss=0;
    for(int i=0;i<(int)table[k].size();i++)
    {
        if(table[k][i]!=-1)
        {
            p+=owp(table,i);
            oss++;
        }
    }
    return p/oss;
}

long double rpi(vector<vector<int> >& table, int k)
{
    vector<int> v;
    v=table[k];
    return 0.25*(wp(v))+0.5*(owp(table, k))+0.25*(oowp(table, k));
}

int main()
{
    ifstream be("A-large.in");
    ofstream ki("ki.txt");
    int T;
    be>>T;
    for(int i=0;i<T;i++)
    {
        int n;
        be>>n;
        vector<vector<int> > table;
        for(int j=0;j<n;j++)
        {
            vector<int> v;
            for(int k=0;k<n;k++)
            {
                char ch;
                be>>ch;
                if(ch=='1')
                {
                    v.push_back(1);
                } else if(ch=='0')
                {
                    v.push_back(0);
                } else if(ch=='.')
                {
                    v.push_back(-1);
                } else
                {
                    k--;
                }
            }
            table.push_back(v);
        }
        /*for(int j=0;j<n;j++)
        {
            for(int k=0;k<n;k++)
            {
                cout<<table[j][k]<<" ";
            }
            cout<<endl;
        }*/
        ki<<"Case #"<<i+1<<":"<<endl;
        for(int j=0;j<n;j++)
        {
            //cout<<owp(table,j)<<" ";
            //cout<<oowp(table,j)<<" ";
            ki<< rpi(table,j)<<endl;
        }
    }
    return 0;
}
