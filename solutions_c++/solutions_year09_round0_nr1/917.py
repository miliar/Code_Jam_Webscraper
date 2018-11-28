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

char w[5001][20];
char p[1000];

int main(){
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int L,D,N;
	scanf("%d%d%d",&L,&D,&N);
	int i,j,c;
	gets(p);
	for(i=0;i<D;i++)gets(w[i]);
	for(i=0;i<N;i++){
		gets(p);
		c=0;
		int t=0,t1,k,l=strlen(p);
		string s,ss;
		for(k=0;k<l;k++){
			if(p[k]=='('){
				s=s+' ';
				t++;
			}else if(p[k]==')'){
				s=s+' ';
				t--;
			}else if(t==0){
				s=s+' ';
				s=s+p[k];
			}else s=s+p[k];
		}
		for(j=0;j<D;j++){
			istringstream is(s);
			int t1=0;
			for(k=0;k<L;k++){
				int b=0;
				is >> ss;
				for(t=0;t<ss.length();t++)
					if(ss[t]==w[j][k])b=1;
				t1+=b;
			}
			if(t1==L)c++;
		}
		printf("Case #%d: %d\n",i+1,c);
	}
	return 0;
}
