//
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

#define ita(i_,f_,t_) for(int i_=f_;i_<t_;++i_)
#define itd(i_,f_,t_) for(int i_=f_;i_>t_;--i_)

char ts[100][100];
double wp[100][100];
int gn[100];
int wn[100];
double owp[100];
double oowp[100];
//int oowp[100];

int main()
{
    int T;
    cin>>T;
    ita(t,0,T)
    {
        memset(ts,0,sizeof(ts));
        int N;
        cin>>N;
        ita(n,0,N)
        {
            string s;
            cin>>s;
            gn[n]=0;
            wn[n]=0;
            ita(i,0,s.size())
            {
                ts[n][i]=s[i]; 
                if (s[i]!='.')
                    gn[n]+=1;
                if (s[i]=='1')
                    wn[n]+=1;
            }
        }

        
        ita(n,0,N)
        {
            ita(i,0,N)
            {
                char c=ts[n][i];
                if (c=='.') continue;
                
                if (c=='1') 
                    wp[n][i]=(double)(wn[n]-1)/(gn[n]-1);
                else
                    wp[n][i]=(double)wn[n]/(gn[n]-1);
            }
        }

        ita(n,0,N)
        {
            owp[n]=0.0;
            ita(i,0,N)
            {
                char c=ts[i][n];
                if (c!='.') 
                    owp[n] += wp[i][n];
            }
            owp[n] = owp[n]/gn[n];
        }

        ita(n,0,N)
        {
            oowp[n]=0.0;
            ita(i,0,N)
            {
                char c=ts[i][n];
                if (c!='.') 
                    oowp[n] += owp[i];
            }
            oowp[n] = oowp[n]/gn[n];
        }

           
        cout<<"Case #"<<(t+1)<<": "<<endl;
        ita(n,0,N)
        {
            
           double r = 0.25 * (double)wn[n]/gn[n] + 0.5 * owp[n] + 0.25 * oowp[n];
           cout.setf(ios::fixed,ios::floatfield);
           cout.precision(9);
           cout<<r<<endl;
        }
    }
    return 0;
}