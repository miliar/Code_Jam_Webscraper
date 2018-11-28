#include<iostream>
#include<algorithm>

using namespace std;

long long tstcss,n,w,l,r[20],lp;
long long i,pos[20][2],j,t1,t2;
bool bl;

int main()
{
    cin>>tstcss;
    for (lp=0;lp<tstcss;lp++)
    {
        cin>>n>>w>>l;
        for (i=0;i<n;i++)
        {
            cin>>r[i];
        }
        pos[0][0]=0;pos[0][1]=0;
        pos[1][0]=w;pos[1][1]=l;
        for (i=2;i<n;i++)
        {
            bl=false;
            while (bl==false)
            {
                pos[i][0]=rand();
                pos[i][0]=pos[i][0]<<16;
                pos[i][0]=pos[i][0]+rand();
                pos[i][0]%=w;
                pos[i][1]=rand();
                pos[i][1]=pos[i][1]<<16;
                pos[i][1]=pos[i][1]+rand();
                pos[i][1]%=l;
                bl=true;
                for (j=0;j<i;j++)
                {
                    t1=(pos[j][0]-pos[i][0])*(pos[j][0]-pos[i][0])+(pos[j][1]-pos[i][1])*(pos[j][1]-pos[i][1]);
                    t2=(r[i]+r[j]);
                    t2=t2*(r[i]+r[j]);
                    if (t1<t2)
                    {
                        bl=false;
                        break;
                    }
                }
            }
        }
        cout<<"Case #"<<lp+1<<":";
        for (i=0;i<n;i++)
        {
            cout<<" "<<pos[i][0]<<" "<<pos[i][1];
        }
        cout<<endl;
    }
    return 0;
}
            
    
            
