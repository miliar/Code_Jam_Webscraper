#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,TT=0;
    cin>>T;
    while(T--)
    {
       TT++;
       int c,d,n,i,j,k,l,f=0;
       string sc[100],sd[100],sn;
       cin>>c;
        for(i=0;i<c;i++)
        {
            cin>>sc[i];
        }
        cin>>d;
        for(i=0;i<d;i++)
        {
            cin>>sd[i];
        }
        cin>>n>>sn;
        //cout<<sd[0]<<endl;
        string a="",at;
        a = sn[0];
        
        for(i=1;i<n;i++)
        {
            a = a + sn[i];
            f = 0;
            
            while(1)
            {
                f = 0;
                /* Replace */
                int l = a.size() - 1;
                if(c==0)
                break;
                
                if((a[l]==sc[0][0] && a[l-1]==sc[0][1]) || (a[l-1]==sc[0][0] && a[l]==sc[0][1]))
                {
                     a[l-1] = sc[0][2];
                     a.erase(a.size()-1);
                     f = 1;
                }
                if(f==0)
                break;
            }

            while(1)
            {
                f = 0;
                /* Replace */
                int l = a.size() - 1;
                if(d==0)
                break;
                
                int j,k,x,y;
                for(k=0;k<a.size();k++)
                {
                    for(j=k+1;j<a.size();j++)
                    {
                        if( (a[k]==sd[0][0] && a[j]==sd[0][1] ) || (a[j]==sd[0][0] && a[k]==sd[0][1]))
                        {
                            f = 0;
                            a="";
                            break;
                        }
                     }   
                    
                }
                if(f==0)
                break;
            }
          }
           cout<<"Case #"<<TT<<": [";
            if(a=="")
            {
                cout<<"]"<<endl;
                continue;
            }
            for(i=0;i<a.size()-1;i++)
            {
                cout<<a[i]<<", ";
            }
            if(a.size()>0)
            cout<<a[a.size()-1];
            cout<<"]"<<endl;
        }
    return 0;
} 
           
       
