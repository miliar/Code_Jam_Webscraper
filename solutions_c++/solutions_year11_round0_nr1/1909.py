/*	SURENDRA KUMAR MEENA	*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back

vector<char> color;
vector<int> pos, opos, bpos;

void allClear(){
	color.clear();
	pos.clear();
	opos.clear();
	bpos.clear();
}

int getNext(int i,int j){
	if(j==-1 || i==j)	return i;
	return j<i?i-1:i+1;
}

int main(){
	int t;
	cin>>t;
	FF(kase,1,t+1){
		cout<<"Case #"<<kase<<": ";
		int n;
		cin>>n;
		allClear();
		char ch;
		int p;
		F(i,n){
			cin>>ch>>p;
			color.PB(ch);
			pos.PB(p);
			if(ch=='O')	opos.PB(p);
			else			bpos.PB(p);
		}
		opos.PB(-1);
		bpos.PB(-1);
		int i=0,j=0,k=0,ans=0;
		int cur_opos=1,cur_bpos=1;
		while(j<opos.size()-1 || k<bpos.size()-1){
			if(color[i]=='O' && cur_opos==pos[i]){
				i++;
				cur_bpos = getNext(cur_bpos, bpos[k]);
				j++;
			}
			else if(color[i]=='B' && cur_bpos==pos[i]){
				i++;
				cur_opos = getNext(cur_opos, opos[j]);
				k++;
			}
			else{
				cur_bpos = getNext(cur_bpos, bpos[k]);
				cur_opos = getNext(cur_opos, opos[j]);
			}
			ans++;
		}
		cout<<ans<<endl;
	}
	return 0;
}
