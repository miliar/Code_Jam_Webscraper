//Dinic .注意T一定要是点数是从0...T.所以T一定要是最大的点
#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

const int maxn = 10000;

char word[maxn][100];
int L,D,N;
char pat[maxn];
vector<char>vs[20];
void GetPat(){
	int i,j,k;
	for(i=0;i<L;i++)vs[i].clear();
	int id=0;
	for(i=0;pat[i];){
		if( pat[i]=='(' ){
			i=i+1;
			while(pat[i]!=')'){
				vs[id].push_back( pat[i] );i++;
			}
			i++;
		}
		else {
			vs[id].push_back( pat[i] );
			i++;
		}
		sort(vs[id].begin(),vs[id].end() );
		id++;
	}

	//for(i=0;i<L;i++)cout<<vs[i].size()<<" ";cout<<endl;
}
bool Match(char *s){
	//cout<<s<<endl;
	int i,j;
	for( i=0;i<L;i++){
		for(j=0;j<vs[i].size();j++)if( vs[i][j] == s[i] )break;
		if( j>=vs[i].size() )return false;
	}
	return true;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int i,j,k;
	scanf("%d%d%d",&L,&D,&N);
	for(i=0;i<D;i++)scanf("%s",word[i]);
	for(i=1;i<=N;i++){
		scanf("%s",pat);
		GetPat();
		int ret =0;
		for(j=0;j<D;j++)if( Match(word[j]) )ret++;
		printf("Case #%d: %d\n",i,ret);
	}
}

