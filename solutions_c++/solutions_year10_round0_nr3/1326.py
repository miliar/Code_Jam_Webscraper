#include<iostream>
#include<vector>
#include<queue>

using namespace std;


queue<int> q;
vector<int> v;

int r,k,n;  // r raz po k 4eloverk, n-grupp


long long init(){

scanf("%d%d%d",&r,&k,&n);

q = queue<int>();
int temp;
for(int i=0;i<n;i++)
{
  scanf("%d",&temp);
  q.push(temp);
}
int col=0;
int t;
long long ans=0;

for(int i=0;i<r;i++)
  {
  col=0;
   v.clear();
  
   for(int j=0;col+q.front()<=k && q.size();j++)
   {
   col+=q.front();
   temp=q.front(); v.push_back(temp);q.pop();
   }

  for(int j=0;j<v.size();j++)
  q.push(v[j]);

  ans+=col;
  }

return ans;
}

int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);

int t;  //koli4estvo testov
cin>>t;

for(int i=1;i<=t;i++)
{
  cout<<"Case #"<<i<<": "<<init()<<endl;

}


return 0;}