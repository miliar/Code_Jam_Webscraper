#include<iostream>

using namespace std;

int a[1001];

int main()
{
    int c,m,i,l,p,f;
    cin>>c;
    for(int i1=1;i1<=c;i1++)
    {
            cin>>l>>p;
            f=0;
    for(i=l;i<=p;i++)
    {
                        
                        if(i<10)
                        {
                                f=0;
                        }
                        else if(i<100)
                        {
                             a[i]=a[i-1];
                           m=i;
                           m=((m%10)*10)+(m/10);
                           if(m>i && m<=p)
                                  f++;  
                           
                           
                        }
                        else if(i<1000)
                        {
                             a[i]=a[i-1];
                             m=i;
                           m=((m%10)*100)+(m/10);
                           if(m>i && m<=p)
                                  f++;  
                           m=((m%10)*100)+(m/10);
                           if(m>i && m<=p)
                                  f++; 
                        }
                           
    }
    cout<<"Case #"<<i1<<": "<<f<<endl;
}
    
    //cin>>i;
}

