#include <iostream>
using namespace std;
int main()
{
    int t,n,po,pb,no=0,nb=0,i,j,p,s,x,a;
    char ch;
    cin>>t;
    for(i=0;i<t;++i)
    {
        cin>>n;
        int butt[n+1][2];
        for(x=0;x<=n;x++) {butt[n][1]=butt[n][0]=0;}
        for(j=0;j<n;j++)
        {
            cin>>ch;
            if(ch=='O') {cin>>butt[j][0];butt[j][1]=0;}
            else
            if(ch=='B') {cin>>butt[j][1];butt[j][0]=0;}
        }
        butt[j][0]=butt[j][1]=-2;
        for(po=1,pb=1,s=0,p=0;butt[p][0]!=-2;s++)
        {
            a=0;
            for(x=p;x<n;x++)
                if(butt[x][0]!=0) {no=butt[x][0];break;}
            for(x=p;x<n;x++)
                if(butt[x][1]!=0) {nb=butt[x][1];break;}
            //cout<<"\n\n po="<<po<<"  pb="<<pb<<"  no="<<no<<"  nb="<<nb;
            if(no>po) po++;
            else if(no<po) po--;
            else if(butt[p][0]==po){ p++;a=1;}
            //else cout<<"stays";
            if(nb>pb) pb++;
            else if(nb<pb) pb--;

            else if((butt[p][1]==pb)&&(a==0)) p++;
            //else cout<<"stays";

        }
        cout<<"Case #"<<i+1<<": "<<s<<endl;
    }
}
