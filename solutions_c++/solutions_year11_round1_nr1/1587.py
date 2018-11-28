#include<iostream>
#include<cmath>
using namespace std;

int main()
{

//    cout<<a;
    int num;
    cin>>num;
    for(int round=1;round<=num;round++)
    {
        int n,pd,pg;
        cin>>n;
        cin>>pd;
        cin>>pg;
        double fwin;
        int win,rp;
        bool can1=false,can2=false;
        for(int i=1;i<=n;i++)
        {
            fwin=pd*i/100.0;
            //cout<<fwin<<endl;
            if(fwin==floor(fwin))
            {
                can1=true;
                rp=i;
                win=fwin;
                break;
            }
        }
        //cout<<win<<"---"<<rp<<endl;
        int twin,tr;
        double ftwin;
        for(int i=rp;i<(int)pow(2,15);i++)
        {
            ftwin=pg*i/100.0;
            if(ftwin==floor(ftwin)&&floor(ftwin)>=win)
            {
                can2=true;
                tr=i;
                twin=ftwin;
                break;
            }
        }
        if(pg==100&&win!=rp)
            can1=false;
        //cout<<twin<<"==="<<tr<<endl;
        if(can1&&can2&&win<=twin)
        {
            cout<<"Case #"<<round<<": Possible"<<endl;
        }
        else{
            cout<<"Case #"<<round<<": Broken"<<endl;
        }
    }
    return 0;
}
