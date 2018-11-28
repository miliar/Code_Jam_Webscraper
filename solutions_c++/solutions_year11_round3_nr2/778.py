#include<iostream>
using namespace std;

double x[10013];
int main()
{

int tt;
cin>>tt;

for(int ii=1;ii<=tt;ii++)
{
    long long L,t,n,c;
    cin>>L>>t>>n>>c;
    for(int i=0;i<c;i++)cin>>x[i];
    double tt=0;
long long an=0;
    if(L==1)
    {
        for(int i=0;i<n;i++)
        {
            if(tt<t)
            {
                    if(x[i%c]>(t-tt)*0.5)
                    {
                        long long g=(double(x[i%c])-(t-tt)*0.5);
                        if(g>an)an=g;
                    }
            }
            else
            {
                long long g=(x[i%c]);
                        if(g>an)an=g;
            }
            tt=tt+(x[i%c]*2);
        }
    }
    else if(L==2)
    {
        for(int i=0;i<n-1;i++)
        {
            if(tt<t)
            {
                    if(x[i%c]>(t-tt)*0.5)
                    {
                        long long g=(x[i%c]-(t-tt)*0.5);
                        //if(g>an)an=g;
                        for(int ii=i+1;ii<n;ii++)
        {

                        long long gg=(x[ii%c]);
                        if(gg+g>an)an=gg+g;

        }
                    }
            }
            else
            {
                long long g=(x[i%c]);
                        //if(g>an)an=g;
                        for(int ii=i+1;ii<n;ii++)
        {

                        long long gg=(x[ii%c]);
                        if(gg+g>an)an=gg+g;



        }
            }
            tt=tt+(x[i%c]*2);
        }
    }
    //cout<<"===="<<an<<endl;
    long long ggg=0;
    for(int i=0;i<n;i++)ggg=ggg+(x[i%c]*2);
    cout<<"Case #"<<ii<<": ";
    cout<<(ggg-an)<<endl;
}
return 0;
}
