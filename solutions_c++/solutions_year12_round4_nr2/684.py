#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<queue>

using namespace std;

const int MX=11111;
long long N,W,L;

long long R[MX];

long long X[MX],Y[MX];

int bigrand()
{
    int ret=0;
    int i;

    for(i=0;i<7;i++)
    {
        ret=ret*16+rand()%16;
    }

    return ret;
}
void test()
{
    bool flag;
    long long dx,dy,dr;
    int i,j,cnt;
    cin>>N>>W>>L;


    for(i=0;i<N;i++) cin>>R[i];

    for(i=0;i<N;i++)
    {
        //cout<<i<<" ";
        cnt=0;
        while(1)
        {
            X[i]=bigrand()%(W+1);
            Y[i]=bigrand()%(L+1);


            for(j=0;j<i;j++)
            {
                dr=R[i]+R[j]; dr*=dr;
                dx=X[i]-X[j]; dx*=dx;
                dy=Y[i]-Y[j]; dy*=dy;

                if(dx+dy<dr) {
                //cout<<dx<<" "<<dy<<" "<<dr<<" "<<X[i]<<" "<<Y[i]<<" "<<X[j]<<" "<<Y[j]<<endl;;
                break;}
            }

            if(j==i) break;
            cnt++;

            if(cnt>10)
            {
                //cout<<"*";
                i=j-1;
                break;
            }
        }


    }

    for(i=0;i<N;i++)
    {
        cout<<X[i]<<" "<<Y[i]<<" ";
    }

}
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);

    int i,I;
    cin>>I;

    for(i=0;i<I;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        test();
        cout<<endl;
    }
    return 0;
}
