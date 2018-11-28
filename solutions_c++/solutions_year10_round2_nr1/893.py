#include<algorithm>
#include<iostream>
#include<cmath>
#include<string>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<list>

#define mn(a,b) ( (a) < (b) ? (a) : (b) )
#define mx(a,b) ( (a) > (b) ? (a) : (b) )
#define ab(a) ( (a) < (0) ? (-a) : (a) )

#define MP make_pair
#define PB push_back
#define F first
#define S second

using namespace std;


int T,n,m;
char buf[200];
string str;
set<list<string> > dirs;
set<list<string> >::iterator sit;
list<string>::iterator lit;
list<string> path;
void solve(int x){
dirs.clear();
int ans=0;
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++){
		scanf("%s",&buf);
		str.assign(buf);
		str+='/';
		path.clear();
		string tmp="";
		for(int i=1;i<str.length();i++){
          		if(str[i]=='/'){ path.PB(tmp);tmp="";}
			else tmp+=str[i];
		}
		//for(lit=path.begin();lit!=path.end();lit++)
		//cout<<*lit<<" ";
		//cout<<endl;
	        dirs.insert(path);
		
	}
	for(int i=0;i<m;i++){
		path.clear();
		scanf("%s",&buf);
		str.assign(buf);
		str+='/';
		string tmp="";
		for(int i=1;i<str.length();i++){
          		if(str[i]=='/'){
				//path.clear();
				path.PB(tmp); 
				tmp="";
				if(dirs.find(path)==dirs.end()){
					//cout<<"inserting path"<<endl;
		//for(lit=path.begin();lit!=path.end();++lit)
		//cout<<*lit<<" ";
		//cout<<endl;
					ans++;
					dirs.insert(path);
				}
			}
			else{
				tmp+=str[i];
			}
		}
	}
	printf("Case #%d: %d\n",x,ans);
}


int main(){

freopen("input.txt","r",stdin);
freopen("output.out","w",stdout);
scanf("%d",&T);
for(int i=1;i<=T;i++){
	solve(i);
}

return 0;
}


