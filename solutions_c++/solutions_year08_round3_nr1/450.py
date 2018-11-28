#include<iostream>
#include<vector>
#include<string>
#include<cstdio>
using namespace std;

long long press(int k, int l, vector<int> f)
{ sort(f.begin(),f.end());
  reverse(f.begin(),f.end());
  long long res=0;
  int c=0;
  for(int i=0;i<k&&c<l;i++)
  { int j=i,n=1;
    while(j<l)
    { res+=f[j]*n;
      j=j+k;
      ++n;
    }
  }
  return res;
}
int main()
{ freopen("A-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  int n,p,k,l;
  cin>>n;
  for(int i=0;i<n;i++)
  { vector<int> f;
    int tem;
    cin>>p>>k>>l;
    if(p*k<l)
     { cout<<"Case #"<<i+1<<": Impossible"<<endl;
       continue;
     }
    for(int j=0;j<l;j++)
    { cin>>tem;
      f.push_back(tem);
    }
    cout<<"Case #"<<i+1<<": "<<press(k,l,f);
    cout<<endl;
  }
 return 0;
}  
      
    
  
