#include<iostream>
#include<vector>
using namespace std;
char arr[50010];
int perm[20];
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { int k;
    cin>>k;
    cin>>arr;
    string str=arr;
    for(int i=0;i<k;i++)
    perm[i]=i+1;
    int size=str.size();
    int mx=size;
    do
    { string res="";
      string s1="";
      for(int i=0;i<size/k;i++)
      { s1=str.substr(i*k,k);
        for(int j=0;j<k;j++)
        res+=s1[perm[j]-1];
        
      }
      int cs=0;
      for(int i=0;i<size;)
      { 
        char ch=res[i];
        while(i<size&&ch==res[i])
        i++;
        cs++;
      }
      mx=min(mx,cs);
    }while(next_permutation(perm,perm+k));
    cout<<"Case #"<<t+1<<": "<<mx<<"\n";
  }
}
