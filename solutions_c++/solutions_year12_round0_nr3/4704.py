#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<sstream>

using namespace std;

int inArray(int val,int arr[])
{
    int ret;
    for(int i=0;i<10;i++)
    {
            if(val==arr[i])
            {
                           return 1;
            }
    }
    return 0;
}

int cnt(string a,string b)
{
 int cnt=0;
 int start,end;
 start=atoi(a.c_str());
 end=atoi(b.c_str());
 string s;


 
 for(int i=start;i<=end;i++)
 {
         stringstream out;
         out<<i;
         s=out.str();
         int sz=s.size();
         int arr[10];
         int index=0;
         for(int k=0;k<10;k++)
                 {
                         arr[k]=0;
                 }
         for(int j=0;j<sz;j++)
         {
                 
                 index=0;
                 string m,n;
                 m=s.substr(j);
                 
                 n=s.substr(0,j);
                 m+=n;
                 int val=atoi(m.c_str());
                 if(val>i && val>=start && val<=end)
                 {
                          if(!inArray(val,arr))
                          {
                          
                          cnt++;
                          arr[index++]=val;
                          }
                 }
         }
 }
 
 return cnt;
} 

int main()
{
    freopen("C:\\Users\\Deval Agrahari\\Downloads\\C-small-attempt0.in", "r", stdin);
    freopen("C:\\Users\\Deval Agrahari\\Downloads\\C-small-attempt0.out", "w", stdout);
 int t;
 cin>>t;


 for(int i=0;i<t;i++)
 {
         
         string a,b;
         cin>>a>>b;
         int ret=cnt(a,b);
         cout<<"Case #"<<i+1<<": "<<ret<<endl;

 }

 return 0;
}
