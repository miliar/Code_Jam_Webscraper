#include <iostream>
using namespace std;
#include <cstdio>
#include <algorithm>
#include <deque>
#include <map>
#include <set>
typedef pair<int,int> pii;
#include <vector>
typedef vector<int> vi;
#include <queue>
#include <stack>
#define For(i,a,b) for(int i=(a);i<(b);++i)

#define ForI(i,a,b) for(int i=(a);i<=(b);++i)
#define ForAll(it,set) for(typeof(set.begin()) it = set.begin(); it!=set.end(); ++it)

typedef set<int> si;
typedef queue<int> qi;


#define mod(a) (((a)%n+n)%n)

int n,m;

vector<si> groups;
int colors[2001];
bool canDo(int maxColors, int cur=0){
	if(cur == n){
		ForAll(group,groups){
			si achieved;
			ForAll(it,(*group))
				achieved.insert(colors[*it]);
			if(achieved.size() != maxColors)
				return false;
		}
		return true;
	}
	For(i,0,maxColors){
		colors[cur] = i;
		if(canDo(maxColors,cur+1))
			return true;
	}
	return false;
}


int main(){
	int t;
	cin>>t;
	ForI(tt,1,t){
		int start[n],end[n];
		cin>>n>>m;
		For(i,0,m){
			cin>>start[i];
			start[i]--;
		}
		For(i,0,m){
			cin>>end[i];
			end[i]--;
		}
		groups.clear();
		si edges[n];
		For(i,0,n){
			edges[i].insert((i+1)%n);
			edges[(i+1)%n].insert(i);
		}
		For(i,0,m){
			edges[start[i]].insert(end[i]);
			edges[end[i]].insert(start[i]);
		}
		set<pii> used;
		#define debug(a) cerr<<#a" = "<<(a)<<endl;
		
		For(i,0,n){
			/*cerr<<i<<" ";
			ForAll(it,edges[i])cerr<<(*it)<<";";
			cerr<<endl;*/
			ForAll(it,edges[i]){
				if(mod(*it - i) <= n/2 && used.count(pii(i,*it)) == 0){
					//debug(i);
					used.insert(pii(i,*it));
					used.insert(pii(*it,i));
					si group;
					group.insert(i);
					for(int cur = *it,prev=i; cur != i; )
					{
						//debug(cur);
						//debug(prev);
						group.insert(cur);
						si::iterator pos = edges[cur].find(prev);
						if(pos==edges[cur].begin())
							pos = edges[cur].end();
							
						--pos;
						prev = cur;
						cur = *pos;
						used.insert(pii(prev,cur));
						used.insert(pii(cur,prev));
					}
					//ForAll(it,group)cerr<<(*it)<<" ";
					//cerr<<endl;
					groups.push_back(group);
				}
			}		
		}
		int smallest = n;
		ForAll(group,groups){
			smallest = min(smallest, (int)group->size());
		}
		cout<<"Case #"<<tt<<": ";
		if(smallest == n){
			cout<<n<<endl;
			ForI(i,1,n)
				cout<<" "<<i;
			cout<<endl;
		}
		else{
			int maxColors = 1;
			while(maxColors < smallest){
				if(canDo(maxColors+1))
					maxColors++;
				else
					break;
			}
			cout<<maxColors<<endl;
			For(i,0,n){
				if(i>0)cout<<" ";
				cout<<(colors[i]+1);
			}
			cout<<endl;
		}
	
	}

	return 0;
}
