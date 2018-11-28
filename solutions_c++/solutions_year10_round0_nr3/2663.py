#include<iostream>
using namespace std;
int main()
{
    int n,i,j,t,pos,ct,flag ;
    long r,k,g[1100],mon,temp ;
    cin>>t ;
    for(i=0;i<t;i++)
    {
        mon=0;
        pos=0;
        cin>>r>>k>>n;
        for(j=0;j<n;j++)
        {
            cin>>g[j] ;
        }
        for(j=0;j<r;j++)
        {
            temp=0 ;
            ct=0 ;
            flag = 0;           
            while(temp<k && ct<n)
            {
                temp+= g[pos] ;
                if(temp>k)
                {
                    temp -= g[pos] ;
                    flag = 1 ;
                    pos-- ;
                }
                pos++ ;
                if(pos==n) pos=0 ;
                ct++ ;
                if(flag==1) break ;
                
            }
            mon += temp ;
        } 
        cout<<"Case #"<<i+1<<": "<<mon<<endl ;   
    }
    return 0 ;
}
