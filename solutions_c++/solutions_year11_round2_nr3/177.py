#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN=8;

int debut[MAXN],fin[MAXN];
int S,A;
int couleurs[MAXN];
bool present[MAXN];
vector<int> next[MAXN];

bool backtrack(int pos,int C){
//	printf("%d %d\n",pos,C);
	if (pos==S){
		fill(present,present+C,false);
		for (int cur=0;cur<S;cur=next[cur].back())
			present[couleurs[cur]]=true;
		for (int c=0;c<C;c++)
			if (!present[c])
				return false;
		printf("%d\n",C);
		for (int i=0;i<S;i++)
			printf("%d ",couleurs[i]+1);
		return true;
	}
	for (int couleur=0;couleur<C;couleur++){
		couleurs[pos]=couleur;
		bool ok=true;
		for (int i=0;i<A;i++)
			if (fin[i]==pos){
				fill(present,present+C,false);
//				printf("%d : %d\n",i,fin[i]);
				present[couleurs[debut[i]]]=true;
				int cur;
				for (int j=0;j<next[debut[i]].size();j++)
					if (next[debut[i]][j]==pos)
						cur=next[debut[i]][j-1];
				for (;cur!=pos;cur=next[cur].back()){
					present[couleurs[cur]]=true;
				}
				present[couleurs[pos]]=true;
				for (int c=0;c<C;c++)
					ok=ok && present[c];
			}
		if (ok && backtrack(pos+1,C))
			return true;
	}
	return false;
}


void resoud(){
	scanf("%d%d",&S,&A);
	for (int i=0;i<S;i++){
		next[i].clear();
		next[i].push_back(i+1);
	}
	for (int i=0;i<A;i++)
		scanf("%d",&debut[i]);
	for (int i=0;i<A;i++){
		scanf("%d",&fin[i]);
		debut[i]--;fin[i]--;
		if (debut[i]>fin[i])
			swap(debut[i],fin[i]);
		next[debut[i]].push_back(fin[i]);
	}
	for (int i=0;i<S;i++)
		sort(next[i].begin(),next[i].end());
	for (int C=S;C>=0;C--)
		if(backtrack(0,C))
			return ;
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		resoud();
		puts("");
	}
	return 0;
}
