
# include<iostream>
# include<cstdio>
# include<queue>
using namespace std;

int main()
{
freopen("C-small-attempt0.in","rt",stdin);
freopen("output.txt","wt",stdout);

int T,r,n,k,test;
cin>>T;
for(int p=1;p<=T;p++)
{
cin>>r>>k>>n;
queue<int >people;
for(int i=0;i<n;i++)
{
cin>>test;
people.push(test);
}
//end of i/o
int prof=0;
for(int i=0;i<r;i++)
{
int ppl=0,s=0;
while(ppl+people.front()<=k && s++<people.size())
{
ppl+=people.front();
test=people.front();
people.pop();
people.push(test);
}
prof+=ppl;
//cout<<i<<" "<<ppl<<" "<<prof<<endl;

}
printf("Case #%d: %d\n",p,prof);
}
}
