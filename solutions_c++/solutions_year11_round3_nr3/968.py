#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
#define rep(X,Y) for ( int X=0; X<Y ; X++)

using namespace std;

void run ( vector<unsigned> &v,int T ,int U, int L)
{
    int smallest=-1;

    for ( int lim = L ; lim <=U;lim++ )
    {
        int check=0;


        rep(i,v.size())
        {

            if (v[i] % lim==0 ||  lim%v[i]==0  )
            {
                check++;

            }

        }

        if ( check == v.size())
        {

            smallest=lim;
            break;
        }


    }
    cout<<"Case #"<<T+1<<": ";
    if (smallest == -1)
    {
        cout<<"NO\n";
    }
    else
    {
        cout<<smallest<<endl;
    }

}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
  freopen("output.txt","w",stdout);
  unsigned T=0,L=0,U=0,N=0;
  cin>>T;
  rep(i,T)
  {
      cin>>N;
      vector<unsigned> V(N);

      cin>>L>>U;
      rep(j,N)
      {
          cin>>V[j];
      }
//      rep(j,N)
//      {
//          cout<<V[j]<<" ";
//      }

        run(V,i,U,L);

  }
  return 0;
}
