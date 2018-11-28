#include<iostream>
#include<iomanip>
#include<cstdio>
#include<fstream>
using namespace std;
int g[105][105];
double wp[105],owp[105],oowp[105];
int main()
{
    int T,n;
    ifstream cin("A-large.in");
    ofstream cout("A-large.out");
    cin>>T;
    for(int jj=1;jj<=T;++jj){
        cin>>n;
        char ch;
        for(int i=1;i<=n;++i){
            int a0=0,a1=0;
            for(int j=1;j<=n;++j){
                cin>>ch;
                if(ch=='.')
                g[i][j]=-1;
                else if(ch=='0'){
                g[i][j]=0;
                a0++;
                }
                else{
                g[i][j]=1;
                a1++;

                }
                wp[i]=(double)a1/(a0+a1);
            }
        }
        for(int i=1;i<=n;++i){
            int ans=0;
            double sum=0;
            for(int j=1;j<=n;++j){
                int a0=0,a1=0;
                if(g[i][j]!=-1){
                    ans++;
                    for(int k=1;k<=n;++k){
                        if(k!=i){
                            if(g[j][k]==0)
                            a0++;
                            else if(g[j][k]==1)
                            a1++;
                        }
                    }
                    sum+=(double)a1/(a0+a1);
                }
            }
           // cout<<sum<<endl;
            owp[i]=sum/ans;
            }
            for(int i=1;i<=n;++i){
                oowp[i]=0.0;
                int ans=0;
                for(int j=1;j<=n;++j){
                    if(g[i][j]!=-1){
                        ans++;
                        oowp[i]+=owp[j];
                    }
                }
                oowp[i]=oowp[i]/ans;
            }
            cout<<"Case #"<<jj<<":"<<endl;

            for(int i=1;i<=n;++i){
               cout<<setprecision(12)<<0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]<<endl;
               //printf("%.12lf\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
            }

    }
    return 0;
}

