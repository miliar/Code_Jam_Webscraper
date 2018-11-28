#include<iostream>

using namespace std;
int main()
{
    int t;
    cin>>t;
    int counter=0;
    while(t>0)
    {
    counter++;
    int c,d,n,i,j;
    char oppose[2],ar[10];
    string mer;
    cin>>c;
    if(c==1)
        cin>>mer;
    cin>>d;
    if(d==1)
    cin>>oppose;
    cin>>n;
    cin>>ar;
    char final[10];
    int count=0;
    char st='1';
    mer.c_str();
    for(i=0;i<n;i++)
    {
    if((d==1&&i>=-1)&&((ar[i]==oppose[0]||ar[i]==oppose[1])&&(ar[i]!=st)))
        {
            
                count++;
                st=ar[i];
                if(count==2)
                {
                 
                                int p=0;
                                for(j=i+1;j<n;j++)
                                  ar[p++]=ar[j];
                                  
                                n=n-i-1;
                                i=-1;
                                count=0;
                                st='1';
                               
                }
                }
        
        if((c==1)&&((ar[i]==mer[0]&&ar[i+1]==mer[1])||(ar[i]==mer[1]&&ar[i+1]==mer[0])))
        {
                ar[i]=mer[2];
                for(j=i+1;j<n-1;j++)
                                ar[j]=ar[j+1];
                n--;
                i=-1;
                count=0;
                st='1';
        }
        }
           
    cout<<"Case #"<<counter<<": ";
    cout<<"[";
    for(i=0;i<n-1;i++)
       cout<<ar[i]<<", ";
    if(n>0)
       cout<<ar[n-1];
    cout<<"]"<<endl;
    t--;
    }
    }
