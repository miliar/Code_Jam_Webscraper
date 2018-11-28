#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{

    int T, N;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        cout<<"Case #"<<t+1<<":"<<endl;
        cin>>N;
        vector<vector<char> > v(N, vector<char>(N) );
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                char c;
                cin>>c;
                v[i][j] = c;
            }
        }
        for(int i=0;i<N;i++)
        {
            double wp=0;
            int wins = 0;
            int loss = 0;
            for(int j=0;j<N;j++)
            {
                if(v[i][j] =='1')
                    wins++;
                else if(v[i][j] == '0')
                    loss++;

            }
            if(wins==0)
                wp = 0;
            else
            wp = (double)wins/(wins+loss);
            
            double owp=0;
            int counter=0;
            for(int j=0;j<N;j++)
            {
                
                if(v[i][j]!='.')
                {
                    wins = 0;
                    loss = 0;
                    counter++;
                    for(int k=0;k<N;k++)
                    {
                        if(k==i)
                            continue;
                        else
                        {
                            if(v[j][k]=='1')
                                wins++;
                            else if(v[j][k]=='0')
                                loss++;

                        }
                    }
                    if(wins==0)
                        wins=0;
                    else
                    owp +=(double)wins/(wins+loss);
                }
            }
            if(owp == 0)
                owp = 0;
            else
            owp = (double)owp/counter;

            double oowp=0;
            int c=0;
            for(int l=0;l<N;l++)
            {
                if(v[i][l]!='.')
                {
                    c++;
                    double owp=0;
                    int counter = 0;
                    for(int j=0;j<N;j++)
                    {
                    if(v[l][j]!='.')
                    {
                        wins = 0;
                        loss = 0;
                         counter++;
                    for(int k=0;k<N;k++)
                    {
                        if(k==l)
                            continue;
                        else
                        {
                            if(v[j][k]=='1')
                                wins++;
                            else if(v[j][k]=='0')
                                loss++;
                        }
                    }
                if(wins == 0)
                    wins = 0;
                else
                    owp += (double)wins/(wins+loss);
                }

            }
                
                oowp+=(double)owp/counter;
                }

            }
            if(oowp==0)
                oowp = 0;
            else
            oowp = (double)oowp/c;
            cout<<(0.25*wp)+(0.50*owp)+(0.25*oowp)<<endl;

        }

    }

    return 0;
}
