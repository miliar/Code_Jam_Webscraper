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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int n,sz,g,h,m,i,j,c,T,pos1,pos2,i1,i2,d;
string s;
char ch,ch2;
map< pair<char,char> , char > Cmp;
set<pair<char,char> > Dst;
vector<char> st;
void rec(char ch){
			if(st.empty()){
				st.push_back(ch);
			}else{
				ch2=st.back();
				if(Cmp.count(make_pair(ch2,ch))){
					st.pop_back();	
					rec(Cmp[make_pair(ch2,ch)]);
				}else if(Cmp.count(make_pair(ch,ch2))){
					st.pop_back();
					rec(Cmp[make_pair(ch,ch2)]);
				}else{
					for(j=0;j<st.size();j++){
						if(Dst.count(make_pair(st[j],ch)) || Dst.count(make_pair(ch,st[j]))){
							st.clear();
							break;
						}
					}
					if(j && j==st.size())st.push_back(ch);
				}
			}
}
int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	vector<int> a;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		scanf("%d",&c);
		Cmp.clear();
		for(i=0;i<c;i++){
			cin>>s;
			Cmp[make_pair(s[0],s[1])]=s[2];			
		}
		scanf("%d",&d);
		Dst.clear();
		for(i=0;i<d;i++){cin>>s; Dst.insert(make_pair(s[0],s[1]));}
		scanf("%d",&n);
		st.clear();
		cin>>s;
		for(i=0;i<n;i++)
			rec(s[i]);
		if(st.size()){
			printf("Case #%d: [",t+1);
			for(i=0;i<st.size()-1;i++)printf("%c, ",st[i]);
			printf("%c]\n",st[i]);
		}else{printf("Case #%d: []\n",t+1);}
		
	}
	
return 0;
}

//Powered by [KawigiEdit] 2.0!