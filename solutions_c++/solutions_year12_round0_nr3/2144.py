#include <iostream>
#include <vector>
#include <list>
#include <set>
using namespace std;
int change(int n,int x);
vector<int> everD(int n)
{
    vector<int> ret;
    int i,j=1;
    for(i= 10;;i*=10)
    {
        if(i > n)
            break;
        ++j;
    }
    i/=10;
    for(;i!=0;i/=10)
    {
        int d = n/i;
        n -= d*i;
        ret.push_back(d);
    }
    return ret;
}
vector<int> findD(int n,int max)
{
    vector<int> tmp,ret,tmpmax,ret2;
    tmp = everD(n);
    tmpmax = everD(max);
    int j = tmp.size();
    for (int i = 1; i < j; ++i)
    {
        bool t = false;
        for (int k = 0; k < j; ++k)
        {
            if(tmp[(j-i+k)%j]>tmp[k])
            {
                t = true;
                break;
            }
            else if(tmp[(j-i+k)%j]==tmp[k])
                continue;
            else
                break;
        }
        if(t == true)
            ret.push_back(i);
    }
    if(j == tmpmax.size())
    {
        for(auto i:ret)
        {
            bool t = true;
            for(int k=0;k <j;++k)
            {
                if(tmpmax[k]>tmp[(j-i+k)%j])
                    break;
                else if(tmpmax[k]==tmp[(j-i+k)%j])
                    continue;
                else
                {
                    t=false;
                    break;
                }
            }
            if(t == true)
                ret2.push_back(i);
            // int changed = change(n, i);
            // if(changed <=max)
            //     ret2.push_back(i);
        }
    }
    ret.clear();
    set<int> ttt;
    for(auto i:ret2)
    {
        int changed =change(n,i);
        if(ttt.insert(changed).second)
        {
            ret.push_back(i);
        }
    }
    return ret;
}
int change(int n,int x)
{
    vector<int> tmp,ret;
    int i,j=1;
    for(i= 10;;i*=10)
    {
        if(i > n)
            break;
        ++j;
    }
    i/=10;
    for(;i!=0;i/=10)
    {
        int d = n/i;
        n -= d*i;
        tmp.push_back(d);
    }
    for (int k = j-x; k < j; ++k)
    {
        ret.push_back(tmp[k]);
    }
    for(int k = 0;k<j-x;++k)
    {
        ret.push_back(tmp[k]);
    }
    int sum = 0;
    i=1;
    for(vector<int>::reverse_iterator k = ret.rbegin();k!=ret.rend();++k)
    {
        sum += i*(*k);
        i*=10;
    }
    return sum;
}
int main(int argc, char *argv[])
{
    int n;
    cin>>n;
    vector<vector<int> > in;
    for (int i = 0; i < n; ++i)
    {
        vector<int> tmp;
        int a,b;
        cin>>a>>b;
        tmp.push_back(a);
        tmp.push_back(b);
        in.push_back(tmp);
    }
    for (int i = 0; i < n; ++i)
    {
        int count=0;
        int min = in[i][0],max =in[i][1];
        for (int j = min; j <= max; ++j)
        {
            count+= findD(j,  max).size();
        }
        cout<<"Case #"<<i+1<<": "<<count<<endl;
    }
    // for(int i=1;i<=2000000;i++)
    // {
    //     // cout<<i<<':';
    //     for(auto j:findD(i, 2000000))
    //         int k=0;
//cout<<j<<',';
        // cout<<'\n';         
    // }
    // for(auto i:findD(1212,2222))
    //     cout<<i<<endl;
    return 0;
}
