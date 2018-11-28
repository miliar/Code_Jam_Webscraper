#include<iostream>
#include<queue>
using namespace std;
int main()
{
int t,count;
cin>>t;
long long r,k,n,temp;
long long s;
count=1;
while(t--)
{
 queue<int> p;
queue<int> buf;
    s=0;
cin>>r>>k>>n;
for(int i=0;i<n;i++)
{
    cin>>temp;
    p.push(temp);
}
int aa=p.size();
for(int i=0;i<r;i++)
{
    while(buf.size())
    {
        int val=buf.front();
        p.push(val);
        buf.pop();
    }
    int taken=0;
    while(taken<=k && p.size())
    {

        if((p.front()+taken)<=k)
        {
            s=s+p.front();
            taken=taken+p.front();
            buf.push(p.front());
            p.pop();
        }
        else
        break;
    }
}
cout<<"Case #"<<count<<": "<<s<<endl;
count++;
}
return 0;
}
