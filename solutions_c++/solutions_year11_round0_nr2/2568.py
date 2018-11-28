#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main()
{
    char str[105],co[40][5],op[30][5],str2[105];
    int t,c,d,n;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>c;
        for(int j=0;j<c;j++)
            cin>>co[j];
        cin>>d;
        for(int j=0;j<d;j++)
            cin>>op[j];
        cin>>n>>str;
        str2[0]=str[0];
        int p=0,biaoji=1;
        for(int j=1;j<n;j++)
        {
            biaoji=1;
            if(p>-1)
            {
                for(int k=0;k<c;k++)
                {
                    if((co[k][0]==str2[p]&&co[k][1]==str[j])||(co[k][1]==str2[p]&&co[k][0]==str[j]))
                    {
                        str2[p]=co[k][2];
                        biaoji=0;
                        break;
                    }
                }
                if(biaoji)
                {
                    for(int k=0;k<d;k++)
                    {
                        if(op[k][0]==str[j])
                        {
                            for(int r=0;r<=p;r++)
                            {
                                if(op[k][1]==str2[r])
                                {
                                    p=-1;
                                    biaoji=0;
                                    break;
                                }
                            }
                        }
                        else if(op[k][1]==str[j])
                        {
                            for(int r=0;r<=p;r++)
                            {
                                if(op[k][0]==str2[r])
                                {
                                    p=-1;
                                    biaoji=0;
                                    break;
                                }
                            }
                        }
                        if(!biaoji) {break;}
                    }
                }
                if(biaoji)
                    {str2[++p]=str[j];}
            }
            else
            {
                str2[++p]=str[j];
            }
        }
        cout<<"Case #"<<i<<": [";
        if(p!=-1)
        {
            for(int j=0;j<p;j++)
                cout<<str2[j]<<", ";
            cout<<str2[p];
        }
        cout<<"]\n";
    }
    return 0;
}
