#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;
int con(string s)
{
int num=0;
num=((s[0]-'0')*10+(s[1]-'0'))*60+((s[3]-'0')*10+s[4]-'0');
return num;
}
int main()
{
int t,penalty;
scanf("%d",&t);
for(int kk=0;kk<t;++kk)
{
scanf("%d",&penalty);
int A,B,c[2]={0};
scanf("%d%d",&A,&B);
vector< pair <pair<int,int>,int> >v;
for(int i=0;i<A;++i)
{
string s1,s2;
cin>>s1>>s2;
//cout<<s1<<" "<<s2<<endl;
int a1,a2;
a1=con(s1);
a2=con(s2);
v.push_back(make_pair(make_pair(a1,a2),0));
}
for(int i=0;i<B;++i)
{
string s1,s2;
int a1,a2;
cin>>s1>>s2;
//cout<<s1<<" "<<s2<<endl;
a1=con(s1);
a2=con(s2);
v.push_back(make_pair(make_pair(a1,a2),1));
}

sort(v.begin(),v.end());
vector<int> f[2];
//for(int i=0;i<v.size();++i)
//cout<<v[i].first.first<<" "<<v[i].second<<" "<<v[i].first.second<<endl;
for(int i=0;i<v.size();++i)
{
int pdep=v[i].first.first;
int train=v[i].second,state=-1;
for(int j=0;j<f[train].size();++j)
{
if(f[train][j]<=pdep){state=j;break;}
}
if(state!=-1)
{
f[1-train].push_back(v[i].first.second+penalty);
f[train].erase(f[train].begin()+state);
}
else
{
c[train]++;
f[1-train].push_back(v[i].first.second+penalty);
}
}
cout<<"Case #"<<kk+1<<": "<<c[0]<<" "<<c[1]<<endl;
}
return 0;
}
