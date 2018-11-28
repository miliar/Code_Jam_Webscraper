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


int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int Te=1,cas; scanf("%d",&cas);
	while( cas-- ){
		int C,D,N,top;
		char ch[1005],buf[1005];
		map<pair<char,char>,char>mp;
		set<pair<char,char> >st;
		scanf("%d",&C);
		for(int i=0;i<C;i++){
			for(int j=0;j<3;j++) scanf(" %c",ch+j);
			mp[make_pair(ch[0],ch[1])]=ch[2];
			mp[make_pair(ch[1],ch[0])]=ch[2];
		}
		scanf("%d",&D);
		for(int i=0;i<D;i++){
			for(int j=0;j<2;j++) scanf(" %c",ch+j);
			st.insert(make_pair(ch[0],ch[1]));
			st.insert(make_pair(ch[1],ch[0]));
		}
		scanf("%d",&N);
		for(int i=0;i<N;i++) scanf(" %c",ch+i);
		top=0;
		for(int i=0;i<N;i++){
			if( top && mp.find(make_pair(ch[i],buf[top-1]))!=mp.end() ){
				buf[top-1]=mp[make_pair(ch[i],buf[top-1])];
			}else{
				bool del=false;
				for(int j=0;top && j<top;j++){
					if( st.find(make_pair(ch[i],buf[j]))!=st.end() ){
						top=0;
						del=true;
						break;
					}
				}
				if( !del ){
					buf[top++]=ch[i];
				}
			}
		}
		printf("Case #%d: [",Te++);
		for(int i=0;i<top;i++){
			if( i ) printf(", ");
			putchar(buf[i]);
		}
		puts("]");
	}
}