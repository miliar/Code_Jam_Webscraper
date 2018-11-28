#include <iostream>
#include <fstream>
using namespace std;

struct Point
{
   int l;
   int r;
   int cost;
   bool flag;
};

Point Tree[5000];
int M[2000];
int P;
int T;

void Make(int lkey,int rkey,int key)
{
   Tree[key].flag=false;
   Tree[key].l=lkey;
   Tree[key].r=rkey;
   if (lkey+1<rkey) 
   {
      Make(lkey,(rkey+lkey)/2,key*2);
      Make((rkey+lkey)/2+1,rkey,key*2+1);
   }
}

void Check(int rest,int p,int ptr)
{
 // cout<<ptr<<endl;system("pause");
  Tree[ptr].flag = true;
  if (rest>1) 
  {
    int mid;
    mid = (Tree[ptr].l+Tree[ptr].r)/2;
    if ((Tree[ptr].l<=p)&&(p<=mid)) Check(rest-1,p,ptr*2);
       else Check(rest-1,p,ptr*2+1);
  }
}

int main()
{
    ifstream fin("Bsmall.in");
    ofstream fou("Bsmall.out");
    fin>>T;
    for (int t=0;t<T;t++)
    {
      fin>>P;
      int tmp;tmp =1;
      for (int i=1;i<=P;i++) tmp=tmp*2;tmp--;
      for (int i=0;i<=tmp;i++) fin>>M[i];
      Make(0,tmp,1);
      for (int i=tmp;i>=1;i--) fin>>Tree[i].cost;
      for (int i=1;i<=tmp;i++)
     // cout<<i<<":"<<Tree[i].l<<"_"<<Tree[i].r<<":"<<Tree[i].cost<<endl;
      //system("pause");
      //Calculate Answer
      for (int k=0;k<P;k++)
        for (int i=0;i<=tmp;i++)
        {
      //    cout<<k<<" "<<i<<endl;system("pause");
          if (k==M[i]) Check(P-k,i,1);
          }
      int ans;
      ans = 0;
      for (int i=1;i<=tmp;i++)
      if (Tree[i].flag) ans++;
      fou<<"Case #"<<t+1<<": "<<ans<<endl;
    }
    fin.close();
    fou.close();
    return 0;
}
