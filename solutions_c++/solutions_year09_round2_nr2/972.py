#include <iostream>
#include <string>
using namespace std;
int sol(int x)
{
     string a;
     cin>>a;
     for(int i=a.size()-2;i>=0;i--)
     {int mini_p=-1;
      for(int j=a.size()-1;j>i;j--)
       if((a[j]<a[mini_p]&&a[j]>a[i])||(mini_p==-1&&a[j]>a[i]))mini_p=j;
      if(mini_p!=-1)
       {swap(a[mini_p],a[i]);sort(a.begin()+i+1,a.end());cout<<"Case #"<<x<<": "<<a<<endl;return 0;}
     }
     a+='0';
     sort(a.begin(),a.end());
     int p=0;
     while(a[p]=='0')p++;
     swap(a[0],a[p]);
     cout<<"Case #"<<x<<": "<<a<<endl;
     return 0;
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
     sol(i+1);
    return 0;
}
