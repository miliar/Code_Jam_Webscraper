#include<cstdio>
#include<cstring>

int f[260];
bool bo[260][260];
char mp[260][260];

char out[200];

int N,Ans;

void output(){
	printf("[");
	if( Ans ) printf("%C",out[0]);
	for( int i = 1 ; i < Ans ; ++i ) printf(", %C",out[i]);
	printf("]\n");
}
void solve(){
	memset(f,0,sizeof(f));
	memset(bo,false,sizeof(bo));
	memset(mp,0,sizeof(mp));
	scanf("%d",&N);
	for( int i = 0 ; i < N ; ++i ){
		char Pair[4];
		scanf("%s",Pair);
		mp[Pair[0]][Pair[1]] = mp[Pair[1]][Pair[0]] = Pair[2];
	}
	scanf("%d",&N);
	for( int i = 0 ; i < N ; ++i ){
		char Pair[3];
		scanf("%s",Pair);
		bo[Pair[0]][Pair[1]] = bo[Pair[1]][Pair[0]] = true;
	}

	char str[200];
	Ans = 0;
	scanf("%d",&N);
	scanf("%s",str);
	for( int i = 0 ; i < N ; ++i ){
		out[Ans++] = str[i];
		f[str[i]]++;
		if( Ans > 1 && mp[out[Ans-1]][out[Ans-2]] != 0 ){
			//printf("%d %c\n",Ans,mp[out[Ans-1]][out[Ans-2]]);
			f[out[Ans-1]]--;
			f[out[Ans-2]]--;
			out[Ans-2] = mp[out[Ans-1]][out[Ans-2]];
			Ans--;
			//output();
			continue;
		}
		for( int j = 'A' ; j <= 'W' ; ++j )
			if( bo[str[i]][j] && f[j] > 0 ){
				Ans = 0;
				memset(f,0,sizeof(f));
				break;
			}
		//output();
	}
	output();
}
int main(){
	freopen("Magicka.in","r",stdin);
	freopen("Magicka.out","w",stdout);
	int T;
	scanf("%d",&T);
	for( int i = 1 ; i <= T ; ++i ){
		printf("Case #%d: ",i);
		solve();
	}
}