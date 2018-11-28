#include <iostream>
using namespace std;
int main()
{
    int cases,a,b,i,j,x,y;
    cin>>cases;
    int k=0;
    while(k<cases)
    {
        cin>>a>>b;
        int count=0;
        //if(a/10==0){cout<<"Case #"<<k+1<<": 0"<<endl;continue;}
        for(i=b,j=1;i>10;i=i/10,j*=10);
        //cout<<j<<endl;
        if(j==10)
        {
            for(i=a;i<=b;i++)
            {
                x=i/10;
                y=i%10;
                y=y*10+x;
                if(y>i&&y<=b)count++;
            }
            cout<<"Case #"<<++k<<": "<<count<<endl;
        }
        else if(j==100)
        {
            for(i=a;i<=b;i++)
            {
                x=i/10;
                y=i%10;
                y=y*100+x;
                if(y>i&&y<=b){count++;}
                x=i/100;
                y=i%100;
                y=y*10+x;
                if(y>i&&y<=b){count++;}

            }
            cout<<"Case #"<<++k<<": "<<count<<endl;
        }
        else{cout<<"Case #"<<++k<<": 0"<<endl;}


    }

}
