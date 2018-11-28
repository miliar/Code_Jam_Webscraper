#include<iostream>
#include<vector>
using namespace std;
struct input
{
    int N,S,P;
    vector<int> points;
};
int analysis(const input& x)
{
    int nosup = x.P*3-2;
    int sup = x.P*3-4;
    int count = 0;
    vector<int> tmparray;
    for(auto i:x.points)
    {
        if(i>=nosup)
            ++count;
        else
            if(i>=2)
            tmparray.push_back(i);
    }
    int i = x.S;
    for(vector<int>::iterator j = tmparray.begin();i!=0&&j!=tmparray.end();++j)
    {
        if (*j>=sup)
            --i,++count;
    }
    return count;
}
int main(int argc, char *argv[])
{
    int n;
    cin>>n;
    vector<input> in;
    for(int i = 0;i < n;++i)
    {
        input tmp;
        cin>>tmp.N>>tmp.S>>tmp.P;
        for(int j = 0;j<tmp.N;++j)
        {
            int t;
            cin>>t;
            tmp.points.push_back(t);
        }
        in.push_back(tmp);
    }
    int C=1;
    for(auto i:in)
        cout<<"Case #"<<C++<<": "<<analysis(i)<<endl;
    return 0;
}
