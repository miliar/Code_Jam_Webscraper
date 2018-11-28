#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstring>
using namespace std;
const int Max=110;
char board[Max][Max];
int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    double wp[Max],owp[Max],oowp[Max];
    double rpi[Max];
    for(int cas=1;cas<=t;++cas)
    {
        cout<<"Case #"<<cas<<":"<<endl;
        int n;
        cin>>n;
        int s[Max];
        int num[Max];
        for(int i=0;i<n;++i)
        {
            cin>>board[i];
            s[i]=0;
             num[i]=0;
            for(int j=0;j<n;++j)
            {
                if(board[i][j]=='1')s[i]++;
                if(board[i][j]!='.')num[i]++;
            }
            wp[i]=1.0*s[i]/num[i];
//            cout<<"we"<<wp[i]<<endl;
        }
        double sum;
        int k;
        for(int i=0;i<n;++i)
        {
            k=0;sum=0;
            for(int j=0;j<n;++j)
            {
                if(i==j)continue;
                if(board[i][j]!='.')
                {
                    if(board[j][i]=='1')s[j]--;
                    num[j]--;
                    sum+=1.0*s[j]/num[j];
//                    cout<<sum<<endl;
                    k++;
                    num[j]++;
                    if(board[j][i]=='1')s[j]++;
                }
            }
            owp[i]=sum/k;
//            cout<<sum<<" "<<k<<" "<<owp[i]<<endl;
        }
        for(int i=0;i<n;++i)
        {
            k=0;sum=0;
            for(int j=0;j<n;++j)
            {
                if(board[i][j]!='.')
                {
                    sum+=owp[j];
                    k++;
                }
            }
            oowp[i]=sum/k;
            rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
            cout<<rpi[i]<<endl;
        }
//        cout<<wp[0]<<owp[0]<<oowp[0]<<endl;
    }
    return 0;
}
