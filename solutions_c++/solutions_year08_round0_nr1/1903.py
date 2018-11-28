#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

typedef stringstream ss;

typedef string str;

typedef long double doub;

typedef vector< pair<int,int> > vpii;

typedef vector<int>::iterator vit;
typedef vector<int>::reverse_iterator vrit;

#define pb(what) push_back(what)
#define w(what) while(what)
#define re return
#define all(a) (a).begin(), (a).end()
#define F(i,b,a) for(int i=(int)b; i<(int)a; i++)
#define ln length()
#define s size()
#define SA(a) sort(a.begin(), a.end())// sort
#define SO(a,f,t) sort(a[f], a[t])// sort part
#define SB(a) sort(a.rbegin(), a.rend())// backsort
#define UN(a) unique(a.begin(), a.end())
#define mset(a,b) memset(a,b,sizeof(a))
#define sdel(v,n) v.erase(n,1)
#define soff(v,n) v.erase(n) // cut's off all the elements after n in STRING


int main()
{

 ifstream cin ("c:\A-small.in");
 ofstream cout ("c:\A-small.out");

int n;

cin>> n;




F(test,1,n+1)
{
int ans=0;

////
int engs=0;
 cin>>engs;
vs es(engs);

vi ct(engs, 0);
////
string spam;
 getline(cin, spam);
F(eng,0,engs)
{
 getline(cin, es[eng]);
}
////
int ques=0;
 cin>>ques;

 string engn;
int k=0;
getline(cin, engn);

F(que,0,ques)
{
 getline(cin, engn);
 
  // index of SE
  F(i,0,engs)
  {
	  if(es[i]==engn)
	    {ct[i]++;
	      if(ct[i]==1) { k++; }
		 break;
	    }
  }

  if(k==engs) 
  {F(i,0,engs)
   {
   ct[i]=0;
   }
   ans++;
   k=0;
  }

  F(i,0,engs)
  {
	  if(es[i]==engn)
	    {ct[i]++;
	      if(ct[i]==1) { k++; }
		 break;
	    }
  }

}

//
  /*F(i,1,engs)
  {
	 ans=min(ans,ct[i]);
  }*/
//

  cout<<"Case #"<<test<<": "<< ans << endl;
}



	return 0;
}