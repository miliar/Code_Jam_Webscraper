#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <fstream>

using namespace std;
vector<int>blocks;
map<string ,string >users;
string nm = "admin";
struct root
{
       map<string , root*>mFolder;
       root(){}
int insert(vector<string >&vs,int idx)
{
    if(idx == vs.size()-1)
    {
       if(idx == 0)
         if(mFolder.count(vs[0])  )return 0;


	   if( mFolder.count(vs[vs.size()-1])  )return 0;

        mFolder[vs[vs.size()-1]]=new root();
	   return 1;
    }

    if( !mFolder.count(vs[idx]) )return 0;
    return mFolder[vs[idx]]->insert(vs,idx+1);

    return 0;
}
void display(string pth,string spaces)
{
     cout<<spaces+pth<<endl;

     for(map<string ,root*>::iterator it=mFolder.begin();it!=mFolder.end();it++)
        it->second-> display(it->first,spaces+" ");
}

};

vector<string >parsePath(string str)
{
   for(int i=0;i<str.size();i++)
    if(str[i]=='/')str[i]=' ';
   stringstream ss(str);
   vector<string >ret;
   string tmp;
   while(ss>>tmp)
    ret.push_back(tmp);
   return ret;
}

int main()
{
#ifndef ONLINE_JUDGE
freopen("a.txt", "rt", stdin);
freopen("b.txt", "wt", stdout);
#endif

	int t;scanf("%d",&t);
	for (int ii = 0; ii < t; ++ii) {
		cout<<"Case #"<<ii+1<<": ";
		int n,m;scanf("%d%d",&n,&m);
		root r;
		vector<string >path;
		string dir;
		for (int i = 0; i < n; ++i) {
			cin>>dir;
			path = parsePath(dir);
//			r.insert(path,0);
			vector<string >cur;
			for (int j = 0; j < path.size(); ++j) {
				cur.push_back(path[j]);
				r.insert(cur,0);
			}
//
//			cout<<"------------\n";
//			r.display("","");
//			cout<<"------------\n";
		}
		int res= 0 ;
		for (int i = 0; i < m; ++i) {
			cin>>dir;
			path = parsePath(dir);
//			if(r.insert(path,0))res++;
			vector<string >cur;
			for (int j = 0; j < path.size(); ++j) {
				cur.push_back(path[j]);
				if(r.insert(cur,0))res++;
			}

		}
		cout<<res<<endl;

	}
	return 0;
}
