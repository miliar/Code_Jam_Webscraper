#include<iostream>
#include<list>
#include<fstream>
using namespace std;

int main()
{
  ofstream outfile;
  outfile.open("output.txt",ios::out);
  long T,R,K,N,temp,sum=0,max,curr;
  cin>>T;
  for(int t=1;t<=T;++t){
    sum=0;
    cin>>R;
    cin>>K;
    cin>>N;
    // cout<<R<<"\t"<<K<<"\t"<<N<<"\n";
    list<long>v;    
    for(long j=1;j<=N;++j){
      cin>>temp;
      v.push_back(temp);
      sum+=temp;
      //cout<<sum<<endl;
    }
    if(sum<=K){
      outfile<<"Case #"<<t<<": "<<(sum*R)<<endl;
    } else {
      max=R*K; 

      for(long j=1;j<=R;++j){
	sum=0;
	while(sum<=K){
	  curr=v.front();
	  v.pop_front();
	  sum+=curr;
	  v.push_back(curr);
	}
	curr=v.back();
	v.pop_back();
	v.push_front(curr);
	sum-=curr;
	max-=(K-sum);
      }
      outfile<<"Case #"<<t<<": "<<max<<endl;
    }
  }
  outfile.close();
  return 0;
}
