#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<queue>
#include<fstream>
#include<sstream>
#include<stack>
#include<list>
#include<deque>
#include<bitset>
#include<utility>
#include<climits>
#include<iomanip>
#include<ctime>
#include<complex>

int high;
int Sur[40],Nor[40];
bool Surhoy[40];
void issurprise(int num)
{
    if(Sur[num]!=-1)return ;
    else
    {   int a;
        Sur[num]=0;
        Surhoy[num]=false;
        if((num+4)%3==0 && (((num+4)/3)-2)>=0)
        {
            Surhoy[num]=true;
            a=num+4;
            a/=3;
            if(a>=high )
            {
            Sur[num]=1;
            return ;

            }
        }

        if((num+3)%3==0 && (((num+3)/3)-2)>=0)
        {
            Surhoy[num]=true;
            a=num+3;
            a/=3;
            if(a>=high )
            {Sur[num]=1;
            return ;}

        }

        if((num+2)%3==0 && (((num+2)/3)-2)>=0)
        {
            Surhoy[num]=true;
            a=num+2;
            a/=3;
            if(a>=high )
            {Sur[num]=1;
            return ;}

        }

        return ;
    }
}

void isnormal(int num)
{
    if(Nor[num]!=-1)return ;
    else
    {   int a;
        Nor[num]=0;
        if((num+2)%3==0 )
        {
            Surhoy[num]=true;
            a=num+2;
            a/=3;
            if(a>=high )
            {Nor[num]=1;
            return ;}
        }

        if((num+1)%3==0 )
        {
            Surhoy[num]=true;
            a=num+1;
            a/=3;
            if(a>=high ){
            Nor[num]=1;
            return ;}

        }

        if((num)%3==0)
        {
            Surhoy[num]=true;
            a=num;
            a/=3;
            if(a>=high ){
            Nor[num]=1;
            return ;}

        }

        return ;
    }
}

int arr[105];
int A[105],B[105],C[105],D[105];
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-laout.txt","w",stdout);
    int ks,cas;
    int i,j,k;
    int n,sp;

    cin>>ks;

    for(cas=1;cas<=ks;cas++)
    {
        cin>>n>>sp>>high;
        memset(A,0,sizeof A);
        memset(B,0,sizeof B);
        memset(C,0,sizeof C);
        memset(D,0,sizeof D);
        memset(Sur,-1,sizeof Sur);
        memset(Nor,-1,sizeof Nor);
 //       cout<<"_______________\n\n";
        for(i=1;i<=n;i++)
        {
            cin>>arr[i];
            issurprise(arr[i]);
            isnormal(arr[i]);

            if(Surhoy[arr[i]]==true)D[i]=1; // D for Sur hoy
            if(Sur[arr[i]]==1 )C[i]=1;
            if(Nor[arr[i] ]==1)B[i]=1;

            if(C[i]==1 &&  B[i]==0) A[i]=1;

//            cout<<A[i]<<" "<<B[i]<<" "<<C[i]<<" "<<D[i]<<endl;

        }
        int cnt=0;
        // only surprise solution
        for(i=1;i<=n;i++)
        {
            if(A[i]==1 && cnt+A[i]<=sp)
            {  // cout<<cnt+1<<" "<<high<<endl;
                cnt++;
                A[i]=0,B[i]=0,C[i]=0,D[i]=0;
            }
        }

//        cout<<cnt<<" * ";

        //surprise hole o result ase
        if(cnt<sp)
        {

            for(i=1;i<=n;i++)
            {
                if(C[i]==1 && cnt+C[i]<=sp)
                {
                    cnt++;
                    A[i]=B[i]=C[i]=D[i]=0;
                }
            }
        }

        // surprise but tar normal kono result nai

        int total=cnt;
        if(total<sp)
        {
            for(i=1;i<=n;i++)
            {
                if(D[i]==1 && B[i]==0 && total+D[i]<=sp)
                {
                    total++;
                    A[i]=B[i]=C[i]=D[i]=0;
                }
            }

        }

        // baki jara ase and still surprise banate hobe

        if(total<sp)
        {
            for(i=1;i<=n;i++)
            {
                if(D[i]==1 && total+D[i]<=sp)
                {
                    total++;
                    A[i]=B[i]=C[i]=D[i]=0;
                }
            }

        }

        // baki ra nramll add hobe

            for(i=1;i<=n;i++)
            {
                if(B[i]==1 )
                {
                    cnt++;
                }
            }

            cout<<"Case #"<<cas<<": "<<cnt<<endl;

    }


    return 0;
}
