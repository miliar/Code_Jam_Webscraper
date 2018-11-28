#include<iostream>
#include<cstdio>
#include<cmath>
#include<sstream>

using namespace std;

bool visited[2000002];

int ratate(int num);
int s,e;

int main()
{
    int T,total,n,kk=1;

    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    //scanf("%d",&T);
    cin>>T;

    while(T--)
    {
       // scanf("%d %d",&s,&e);
        cin>>s>>e;

        total = 0;
        for(int i=s;i<=e;i++)
        {
            if(!visited[i]){

            n = ratate(i);

            total += (n*(n+1))/2;
            }
            else visited[i] = 0;

        }

  //  printf("Case #%d: %d\n",kk++,total);
    cout<<"Case #"<<kk++<<": "<<total<<endl;
//    cout<<"Total is "<<total<<endl;
    }

return(0);
}

int ratate(int num)
{
    int hisab=0;

    int dnum,temp,q,m,in,p;

    dnum = log10(num);

    //cout<<"num "<<num<<endl;

    for(p = pow(10,dnum);p>1;p/=10)
    {
      //  cout<<"p is "<<p<<endl;

        m = num % p;

        q = num/p;

        in = log10(q);
      //  cout<<"q is "<<q<<endl;
        temp = m*pow(10,(in+1)) + q;

     //   cout<<"temp "<<temp<<endl;

    if(s<=temp && temp<=e){

        int tt = log10(temp);

        if(num!=temp && dnum == tt && visited[temp]==0)
        {
            hisab++;

            visited[temp] = 1;

      //      cout<<"Temp is "<<temp<<endl;
        }
                        }
    }
return(hisab);
}
