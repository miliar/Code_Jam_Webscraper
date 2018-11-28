#include<iostream>
#include<algorithm>
#include<queue>
#include<fstream>
using namespace std;
ifstream fin("Csmall.in");
ofstream fout("Csmall.out");
int arr[1010];
int main()
{
    int R,K,N,T;
    fin>>T;
    for(int cs=0;cs<T;cs++)
    {
       fout<<"Case #"<<cs+1<<": ";
       fin>>R>>K>>N;
       for(int i=0;i<N;i++)
       fin>>arr[i];
       int tu=0,ccap=0,u=0;
       long long ans=0;
       for(int i=0;tu<R;i++)
       {
          if(ccap+arr[i%N]<=K&&u<N)
          ccap+=arr[i%N],u++;
          else
          ans+=ccap,ccap=arr[i%N],tu++,u=1;
       }
       fout<<ans<<endl;
    }
    fout<<endl;
}
