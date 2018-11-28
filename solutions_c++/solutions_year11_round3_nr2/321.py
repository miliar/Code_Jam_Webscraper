#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
long long int L,T,t,N,C,temp;
vector<long long int>data;
vector<long long int>dist;
vector<long long int>ans;
vector<long long int>sub;
long long int in;
long long int sum;
long long int times;
int main()
{
cin>>T;
for(int q=0;q<T;q++)
{
cin>>L>>t>>N>>C; 
sum=times=0;
 for(long long int i=0;i<C;i++)
  {
   cin>>temp;
   data.push_back(temp);
  }
 for(long long int i=0;i<N;i++)
 {
  dist.push_back(   data.at(i%C)*2);
  sum+=data.at(i%C);
 }
 times=sum*2;
 sum=0;
 for(long long int i=0;i<N;i++)
 {
  if(sum<=t)
  {
//   cout<<sum<<endl;
   temp=(t-sum)+dist.at(i)/2-(t-sum)/2;
   if(temp<dist.at(i))
     ans.push_back( temp);
   else
     ans.push_back(dist.at(i));
  }
  else
  {
   ans.push_back(dist.at(i)/2);
  }
  sum+=dist.at(i);
 }
 
 for(int i=0;i<ans.size();i++)
  sub.push_back( ans.at(i) - dist.at(i));


/* for(int i=0;i<ans.size();i++)
  cout<<sub.at(i)<<" ";
  cout<<endl; */
 
 sort(sub.begin(),sub.end());

 for(int i=0;i<sub.size() && i<L;i++)
    times+=sub.at(i);
  
 cout<<"Case #"<<q+1<<": ";
 cout<<times<<endl;
 
 data.clear();
 dist.clear();
 ans.clear();
 sub.clear(); 
}
return 0;
}
