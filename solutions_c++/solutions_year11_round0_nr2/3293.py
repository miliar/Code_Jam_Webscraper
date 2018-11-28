#include<iostream>
#include<vector>
#include<map>
#define pb push_back
#define mp make_pair
using namespace std;



void print(vector<char> invk)
{
   cout<<"[";
   for(int i=0;i<invk.size();i++){
     cout<<invk[i];
      if(i+1<invk.size())
     cout<<", ";

   }
      cout<<"]"<<endl;
}
int main()
{
  int nt;
  cin>>nt;
  for(int p=1;p<=nt;p++)
  {
    map<pair<char,char>,char> pr;
    map<pair<char,char>,bool> opr;
    vector<char>  invk;
    int np,nop;
    int strlen;
    char a,b,c;
    cin>>np;
    for(int i=0;i<np;i++)
    {
       cin>>a>>b>>c;
       pr[mp(a,b)]=c;
       pr[mp(b,a)]=c;
    }
    cin>>nop;
   for(int i=0;i<nop;i++)
    {
       cin>>a>>b;
       opr[mp(a,b)]=true;
       opr[mp(b,a)]=true;
    }
    cin>>strlen;

    for(int i=0;i<strlen;i++)
    {
      cin>>c;
      int lmx=invk.size()-1;
      if(lmx>=0 && pr.find(mp(invk[lmx],c))!=pr.end())
      {
         a=pr[mp(invk[lmx],c)];
         invk.erase(invk.begin()+lmx);
         invk.pb(a);
         continue;
      }
      bool jump=false;
      for(int j=invk.size()-1;j>=0;j--)
      {
           bool k=opr[mp(invk[j],c)];
           if(k){
              invk.clear();
              jump=true;
           }
      }
      if(jump) continue;
      invk.pb(c);
    }
    cout<<"Case #"<<p<<": ";
    print(invk);
   invk.clear();
   pr.clear(); opr.clear();
  }
}
