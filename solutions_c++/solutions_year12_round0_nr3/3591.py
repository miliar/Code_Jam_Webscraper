#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int count=0;
    string s;
    int n;
    while(t!=count)
    {
        int a,b;
        cin>>a;
        cin>>b;
        count++;
        int sat=0;
        for(int i=a;i<b;i++)
        {
                char n[10];
                sprintf(n,"%d",i);
                string s=n;
                s+=s;
          for(int j=i+1;j<=b;j++)
          {
                char m[10];
                sprintf(m,"%d",j);
                string s1=m;
                for(int k=0;k<s.size();k++)
                {
                        if(s.substr(k,s1.size())==s1)
                        {
                            sat++;
                            break;
                        }
                }
          }
        }
        
        cout<<"Case #"<<count<<":"<<" ";
        cout<<sat<<endl;
    }
    return 0;
} 
