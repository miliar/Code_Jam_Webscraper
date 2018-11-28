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
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	rei(t,0,T){
		int N;
		cin>>N;
		vector<vector<int> > l;
		vector<int> pos(2,0);
		rei(i,0,N){
			int a,b;
			cin>>a>>b;
			pos[0]=a,pos[1]=b;
			pb(l,pos);
		}	
		sort(l);
		int ret=0;
		rei(i,0,N){
			rei(j,i+1,N){
				if(l[j][1]<l[i][1])
					ret++;
			}
		}
		cout<<"Case #"<<t+1<<": "<<ret<<endl;
	}
	return 0;
}
