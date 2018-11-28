#include<iostream>
#include<vector>
using namespace std;
#define pb push_back
#define po pop_back()
#include<algorithm>
bool find1(char c,char v[],int top)
{
     for(int i=0;i<top;i++)
       if(v[i]==c) return true;
     return false;
}  
int main()
{
    int t,count=0;
    cin>>t;
    while(t--)
    {
        char f[30][2]={{0}};
        char o[30]={0};
        int c,d,n,i;
        char c1,c2,c3;
        count++;
        char v[1000]={0};
        int top=0;
        cin>>c;
        for(i=0;i<c;i++) { c1=' ';
                           while(c1==' ') cin>>c1;
                           cin>>c2>>c3;
             //              cout<<"c1"<<c1<<c2<<c3<<endl;
                           f[c1-'A'][0]=c2;
                           f[c2-'A'][0]=c1;
                           f[c1-'A'][1]=c3;
                           f[c2-'A'][1]=c3;
                         }
       cin>>d;
       for(i=0;i<d;i++) {
                          do{cin>>c1;} while(c1==' ');
                          cin>>c2;
           //               cout<<"c1"<<c1<<c2<<c3<<endl;
                          o[c1-'A']=c2;
                          o[c2-'A']=c1;
                        }
       cin>>n;
       top=0;
       for(i=0;i<n;i++)
         { cin>>c1;
           while(c1==' ')cin>>c1;
       //    cout<<"C1"<<c1<<endl;
           if(top==0) {v[top++]=c1;}//cout<<"top"<<v[top-1]<<endl;}
           else {
                  if(f[c1-'A'][0]==v[top-1])
                                         {top--;
                                          v[top++]=f[c1-'A'][1];
                                         // cout<<"1st"<<v[top-1]<<endl;
                                         }                       
                 else {
                        c2=o[c1-'A'];
                        //cout<<"find:"<<find1(c2,v,top)<<endl;
                        if(find1(c2,v,top)) top=0;
                        else v[top++]=c1;
         //               cout<<"v"<<v[top]<<endl;
                       }
                                 
                  }
       }
       cout<<"Case #"<<count<<": [";
       for(i=0;i<top-1;i++)
        cout<<v[i]<<", ";
       if(top) cout<<v[i]<<"]"<<endl;
       else cout<<"]"<<endl;
    }
    return 0;
}     
