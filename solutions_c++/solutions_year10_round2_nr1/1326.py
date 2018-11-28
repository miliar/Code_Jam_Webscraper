#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <set>

#define rei(i,a,b) for(int i=a;i<b;i++)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define pb(a,x) a.push_back(x)
#define sort(v) sort(v.begin(),v.end())

using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	rei(t,0,T){
		int N,M;
		cin>>N>>M;
		vector<string> ex;
		string s;
		rei(i,0,N){
			cin>>s;
			pb(ex,s);
		}
		vector<string> toc;
		rei(i,0,M){
			cin>>s;
			pb(toc,s);
		}
		map<string,bool> p;
		rei(i,0,ex.size()){
			string path=ex[i];
			string dir="";
			rei(j,1,path.size()){
				if(path[j]!='/'){
					pb(dir,path[j]);
				}else{
					p[dir]=true;
				}
			}
			p[dir]=true;
		}
		int ret=0;
		rei(i,0,toc.size()){
			string path=toc[i];
			string dir="";
			rei(j,1,path.size()){
				if(path[j]!='/'){
					pb(dir,path[j]);
				}else{
					if(!p[dir]){
						ret++;
						p[dir]=true;
					}
				}
			}
			if(!p[dir]){
				p[dir]=true;
				ret++;
			}
		}
		cout<<"Case #"<<t+1<<": "<<ret<<"\n";
	}
	return 0;
}