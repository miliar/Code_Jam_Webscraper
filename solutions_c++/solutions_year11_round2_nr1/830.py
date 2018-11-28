#include<fstream>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

int main()
{
    int I,T,n,i,j;
    cin>>T;
    vector<double> WP,OWP,OOWP;
    vector<vector<char> > a;
    int num_won;
    vector<int> num_games;
    cout.setf(ios::fixed);
    cout.precision(12);
    for(I=1;I<=T;I++)
    {
        cin>>n;
        OWP.clear();OOWP.clear();
        a.resize(n);WP.resize(n);OWP.resize(n);OOWP.resize(n);num_games.resize(n);
        for(i=0;i<n;i++)
        {
            a[i].resize(n);
            num_games[i]=num_won=0;
            for(j=0;j<n;j++)
            {
                cin>>a[i][j];
                if(a[i][j]=='1'){num_games[i]++;num_won++;}
                if(a[i][j]=='0')num_games[i]++;
            }
            WP[i]=double(num_won)/double(num_games[i]);
            if(num_games[i]==0)WP[i]=0;
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(num_games[j]!=1)
                {
                    if(a[i][j]=='1')
                        OWP[i]+=WP[j]*num_games[j]/(num_games[j]-1);
                    if(a[i][j]=='0')
                        OWP[i]+=(WP[j]*num_games[j]-1)/(num_games[j]-1);
                }
            }
            OWP[i]/=double(num_games[i]);
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(a[i][j]!='.')
                    OOWP[i]+=OWP[j];
            }
            OOWP[i]/=double(num_games[i]);
        }
        cout<<"Case #"<<I<<": "<<endl;
        for(i=0;i<n;i++)
        {
            cout<<0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]<<endl;
        }
    }
}
