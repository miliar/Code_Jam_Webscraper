#include<iostream.h>
#include<stdio.h>
#include<fcntl.h>
int main()
{
    int i,j,k,l,m,cnt,diff,g;
    int t,nv;
    char c;
    int opos,ocount,bpos,bcount,tcount;
    cin>>t;
    g=1;
     freopen( "file.txt", "w", stdout );
    while(t--)
    {
    cin>>nv;
    ocount=bcount=tcount=0; 
    bpos=opos=1;
  while(nv--)
  {

  cin>>c;
  cin>>cnt;
            if(c=='B')
            {  
                diff=cnt-bpos;
                if(diff<0)
                diff*=-1;
                diff-=bcount;
                if(diff<0)
                diff=0;
                bcount=0;                    
                tcount+=diff+1;      
                ocount+=diff+1;
                bpos=cnt;
            }
            if(c=='O')
            {
                      
                diff=cnt-opos;
                if(diff<0)
                diff*=-1;
                diff-=ocount;
                if(diff<0)
                diff=0;
                ocount=0;
                tcount+=diff+1;      
                bcount+=diff+1;
                opos=cnt;
            }            
  }
    cout<<"Case #"<<g++<<": "<<tcount<<"\n";
    }                  
        cout<<"end of results";
        cin>>i;     
    return(0);
}
