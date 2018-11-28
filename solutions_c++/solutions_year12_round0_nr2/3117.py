#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int mxscore[34]={0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,11,11,11};
    int surp[34]={0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1};
    int sss;
        int tc;
        cin>>tc;
        for(int sss=1;sss<=tc;sss++)
        {
                int N,S,p;
                cin>>N>>S>>p;
                int cnt=0;
                while(N--)
                {
                        int a;
                        cin>>a;
                        if(mxscore[a]>=p)
                        cnt++;
                        else if(mxscore[a]+surp[a] >= p && S>0)
                        {
                                S--;
                                cnt++;
                        }
                }
                cout << "Case #" <<sss << ": " << cnt << "\n";
        }
    return 0;
}
