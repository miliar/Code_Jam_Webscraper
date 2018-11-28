#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int calc(int arr[],int n)
{
  int rv=0,i,j,k;
  for(i=0;i<n;++i)
    for(j=i;j<n;++j)
      if(arr[j]<=i) 
      { rv+=j-i;
        int t=arr[j];
        for(k=j;k>i;--k) arr[k]=arr[k-1];
        arr[i]=t;
        break;
      }
  return rv;
}

int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { string s;
    int arr[40],n,i,j;
    cin>>n;
    for(i=0;i<n;++i)
    { cin>>s;
      for(j=n-1;j>=0;--j) if(s[j]=='1') break;
      arr[i]=j;
    }
    cout<<"Case #"<<ci<<": "<<calc(arr,n)<<endl;
  }
}
