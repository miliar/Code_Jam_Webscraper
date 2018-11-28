#include <iostream>
using namespace std;
int getLen(int a)
{
    int len=1;
    while (a/10>0)
    { 
      len++;
      a=a/10;
    }
    return len;
}
int Jlen(int a,int b)
{
    if (getLen(a)!=getLen(b)) return 1;
    return 0;
}
int Jmax(int a,int b)
{
    int i,j;
    int maxa=0,maxb=0;
    int len=getLen(a);
    for(i=0;i<len;i++)
    {
        maxa+=a%10;
        a=a/10;
    }
    
    for(i=0;i<len;i++)
    {
       maxb+=b%10;
       b=b/10;
    }
    
    if (maxa==maxb)
    { 
     
      return 1;
    }
    return 0;
}
int Jmarch(int a,int b)
{
    int i,j,mark;
    char as[10],bs[10];
    int len=getLen(a);
    for(i=0;i<len;i++)
    {
        as[i]=char(a%10+48);
        a/=10;
        bs[i]=char(b%10+48);
        b/=10;
    }
    as[i]='\0';bs[i]='\0';
    for(i=0;i<len;i++)
    {
        if (bs[i]==as[0]) 
        {
            mark=i;
            bool c=true;
            for(j=0;j<len;j++)
            {
                if (as[j]!=bs[(j+mark)%strlen(bs)]) {c=false; break;}
            }
            if (c==true) return 0;
            
        }
    }
    
    return 1;
}
int main()
{
  
    freopen("C-small-attempt0.in","r",stdin);
    freopen("x.out","w",stdout);  
    int num;
    cin>>num;
    int x,A,B,i,j;
    for(x=1;x<=num;x++)
    {
        cin>>A>>B;
        cout<<"Case #"<<x<<": ";
        int code=0;
        for(i=A;i<=B;i++)
            for(j=A;j<=B;j++)
            {
               if (i==j) continue;
               if (Jlen(i,j)==1) continue;
               if  (Jmax(i,j)==0) continue;
               if  (Jmarch(i,j)==1) continue;
               code++;
               //cout<<i<<" "<<j<<endl;
            }
        cout<<code/2<<endl;
    }
    return 0;
}