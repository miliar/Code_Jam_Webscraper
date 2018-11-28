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

#define _for(i,x,n) for(int i=x;i<n;i++)
#define _ifor(i,x,n) for(int i=(n);i>=x;i++)
#define _forv(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)

#define _dv(var) cout<<"L"<<__LINE__<<": "<<#var<<": "<<var<<endl;
#define _dav(i,f) cout<<"L"<<__LINE__<<": "<<#i<<"-"<<#f<<": "; dav(i,f);
template<typename it> void dav(it i,it f)
	{ cout<<"[ "; while(i!=f) cout<<*(i++)	<<" "; cout<<"]"<<endl; }
#define _ln cout<<"_ln: "<<__LINE__<<endl;

std::vector<std::string> partirACadenas(const std::string& s,const std::string& sep)
{
	std::vector<std::string> r;
	if(s.length()==0)
	  return r;
	int i=0;
	while(true)
	{
		int j=s.find(sep,i);
		if(j==std::string::npos)
			break;
		int l=j-i;
		if(l>0) //evita cadenas vacias
			r.push_back(s.substr(i,l));
		i=j+sep.length();
	}
	if(i<s.length())
		r.push_back(s.substr(i));
	return r;
}

struct Dir
{
 string nom;
 map<string,Dir*> hijos;

 bool operator<(const Dir& d)
 {
      return nom<d.nom;
 }
};

int main()
{
 int T;
 cin>>T;
 for(int Z=1;Z<=T;Z++)
 {
         int M,N;
         cin>>N>>M;
         Dir raiz;
         raiz.nom="/";
			string path;
         getline(cin,path);
         for(int i=0;i<N;i++)
         {
                 getline(cin,path);
                 vector<string> ps=partirACadenas(path.substr(1),"/");
                 Dir * actual=&raiz;
                 for(int j=0;j<ps.size();j++)
                 {
                         Dir * nuevo=new Dir();
                         nuevo->nom=ps[j];
                         map<string,Dir*>::iterator it=actual->hijos.find(ps[j]);
                         if(it!=actual->hijos.end())
                                                    actual=it->second;
                         else
                         {
                             actual->hijos.insert(make_pair(ps[j],nuevo));
                             actual=nuevo;
                         }
                 }
         }

         int res=0;
         for(int i=0;i<M;i++)
         {
                 string path;
                 getline(cin,path);
                 vector<string> ps=partirACadenas(path.substr(1),"/");
                 Dir * actual=&raiz;
                 for(int j=0;j<ps.size();j++)
                 {
                         Dir * nuevo=new Dir();
                         nuevo->nom=ps[j];
                         map<string,Dir*>::iterator it=actual->hijos.find(ps[j]);
                         if(it!=actual->hijos.end())
                                                    actual=it->second;
                         else
                         {
                             actual->hijos.insert(make_pair(ps[j],nuevo));
                             actual=nuevo;
                             res++;
                         }
                 }
         }
         cout<<"Case #"<<Z<<": "<<res<<endl;
 }

 return 0;
}


