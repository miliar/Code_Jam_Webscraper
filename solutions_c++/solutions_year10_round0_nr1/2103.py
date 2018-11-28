#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define all(c) ((c).begin()), ((c).end()) 
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define inf (1<<29)
int T,N,K;
bool flag;

int showbit(int x,int i){
	return x&(1<<i);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for(int i=1;i<=T;i++){
		cin>>N>>K;    flag=0;
		for(int k=0;k<N;k++)
		    if(!showbit(K,k))  {flag=1; break;}

		    if(flag) printf("Case #%d: OFF\n",i);  else
                    printf("Case #%d: ON\n",i);
	}                                      



	return 0;
}
