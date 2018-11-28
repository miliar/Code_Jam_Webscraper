//BISMILLAHIRRAHMANIRRAHIM



#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cctype>
#include <climits>
#include <cmath>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define pii pair < int , int >
#define i64 long long

int main(int argc, char **argv)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,I,i,tt,n,m,t[2],b[2],cb,r;
	char rb[3];
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>n;
		t[0]=t[1]=0;
		b[0]=b[1]=1;
		m=0;
		while(n--) {
			cin>>rb>>cb;
			r=rb[0]=='O'?0:1;
			//cout<<m<<' '<<t[r]<<'\n';
			tt=abs(cb-b[r])+t[r];
			//cout<<tt<<'\n';
			t[r]=m=max(m,tt)+1;
			b[r]=cb;
		}
		printf("Case #%d: %d\n",I,m);
	}
	return 0;
}

