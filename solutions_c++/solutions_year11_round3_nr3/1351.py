#include<iostream>
using namespace std;

int LCM(int x,int y)
{
  int prod;
  if(y%x==0)
     return y;
  else
  {
     prod=x*y;
     while(x!=y) // get the GCD of 2 given integers
     {
        if(x>y)
           x=x-y;
        else
           y=y-x;   //x now is the GCD
     }
     return LCM(y,prod/x);  //recurse, changing x to y and vice versa
  }   //LCM = (x*y)/(GCD)
}

int main()
{
    int T;
    cin>>T;
    
    for(int l=1;l<=T;l++)
    {
        int N,L,H,J=0;
        cin>>N>>L>>H;
        
        int *O=new int[N];
        int i,j;
        
        int lcm=1;
        int max=0;
        for(i=0;i<N;i++)
        {
            cin>>O[i];
            if(O[i]>max)
                max=O[i];
        }
        
        int temp;
        bool flag;
        for(i=L;i<=H;i++)
        {
            flag=true;
            for(j=0;j<N && flag==true;j++)
            {
                temp=LCM(i,O[j]);
                if(temp==i || temp==O[j])
                    J=i;
                else
                    flag=false;
            }
            if(flag==true)
                break;
        }
        if(flag==false)
            J=0;

        cout<<"Case #"<<l<<": ";
        if(J==0)
            cout<<"NO\n";
        else
            cout<<J<<endl;
    }
    
    return 0;
}
