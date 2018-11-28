#include<iostream>
#include<algorithm>

#define forn(i,n) for(int i=0;i<n;i++)

using namespace std;

int a[200];
int main()
{
    int n;
    cin>>n;
    int p,q;
    bool pr[100];
    string s;
    for(int caseno=1;caseno<=n;caseno++)
    {
              
            cin>>p>>q;
            for(int i=0;i<100;i++)
              pr[i]=false;
            for(int i=0;i<q;i++)
            {
                     cin>>a[i];
                     a[i]--;
            }
            s="";
            for(int i=0;i<q;i++)
            {
                     s+=(char)(i+48);
            }
            int res=10000000,temp,t2;
            do
            {
                     temp=0;
                     for(int i=0;i<p;i++)
                       pr[i]=false;
                     for(int i=0;i<s.length();i++)
                     {
                                       t2=a[s[i]-48];
                                       for(int j=t2-1;j>=0;j--)
                                       {
                                               if(pr[j]==true)
                                                 break;
                                               temp++;
                                       }
                                       for(int j=t2+1;j<p;j++)
                                       {
                                               if(pr[j]==true)
                                                 break;
                                               temp++;
                                       }
                                       pr[t2]=true;
                     }
                     if(temp<res)
                       res=temp;
            }while(next_permutation(s.begin(),s.end()));
            
            cout<<"Case #"<<caseno<<": "<<res<<endl;
           
    }                      
    return 0;
}
