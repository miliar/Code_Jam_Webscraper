#include<iostream>
#include<fstream>
using namespace std;

int recycle(int a, int b);

int main()
{
    int t,a,b,n;
    freopen("C-small-attempt3.in","r",stdin);
    freopen("out.txt","w",stdout);

    int i= 1;
    cin>>t;
    while(t--)
    {
        int c;
        cin>>a;
        cin>>b;
        c = recycle(a,b);
        cout<<"Case #"<<i<<": "<<c<<endl;
        i++;
    }
    return 0;
}

int recycle(int a, int b)
{
    int count =0,i,r,x,y,n;
    if(a<10 && a>=1)
        {
            return 0;
        }
    if(a<100 && a>=10)
        {
            for(i=a;i<b;i++)
            {
                r = (i%10)*10 + (i/10);
                if(r>i && r<=b)
                {
                    count++;
                }


            }
            return count;
        }
        if(a<1000 && a>=100)
        {
            for(i=a;i<b;i++)
            {
                x = (i%10)*100 + (i/10);
                y = (i%100)*10 + (i/100);

                if(x>i && x<=b)
                    count++;
                if(y>i && y<=b)
                    count++;
            }
            return count;
        }

}
