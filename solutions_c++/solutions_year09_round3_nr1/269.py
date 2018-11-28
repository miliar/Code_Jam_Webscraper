#include<iostream>
#include<vector>
#include<cstring>
#include<map>
#include<algorithm>
#define ll long long
using namespace std;
ll step(int a,int b)
{
    int i;
    ll res=1;
    for(i=0;i<b;++i)res*=(ll)a;
    return res;
}
ll convert(vector<int> num,int bs)
{
    int i;
    ll res=0;
    for(i=0;i<num.size();++i)res+=step(bs,num.size()-i-1)*(ll)num[i];
    return res;
}
int main()
{
    int i,j,T;
    char S[64],u;
    int asg[]={1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37},ind;
    vector<int> A;
    scanf("%d\n",&T);
    for(i=0;i<T;++i)
    {
        scanf("%s\n",S);
        A.clear();
        map<char,int> E;
        for(u='0';u<='9';++u)E[u]=-1;
        for(u='a';u<='z';++u)E[u]=-1;
        ind=0;
        for(j=0;j<strlen(S);++j)
        {
            if(E[S[j]]==-1)E[S[j]]=asg[ind++];
            A.push_back(E[S[j]]);
        }
        int base=0;
        for(j=0;j<A.size();++j)base=max(base,A[j]);
        ++base;
        cout<<"Case #"<<i+1<<": "<<convert(A,base)<<'\n';
    }
    return 0;
}
