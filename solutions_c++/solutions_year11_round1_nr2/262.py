#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include<queue>
using namespace std;
#define Check(a) if(a)while(1)puts("kero");

int n;
int len[20000],key[20000];
char list[100];
int nlen,nkey;
string nn;
string D[20000];
bool used[100];

bool pat(int x){
	if(nlen != len[x])return 0;
	if((nkey & key[x]) != nkey)return 0;
	for(int i=0;i<len[x];i++)if(nn[i]!='_' && nn[i] != D[x][i] || (used[D[x][i] - 'a'] && nn[i]=='_'))
		return 0;
	return 1;
}

int mm[200];
int kero(){
	int amax = -1;
	int ans = -1;
	int i,j,k;
	
	for(i=0;i<n;i++){
		int bmax = 0;
		memset(used,0,sizeof(used));	
		nlen = len[i];
		nkey = 0;
		nn = "";
		for(j=0;j<len[i];j++) nn+="_";
		
		int tot=n;
		for(j=0;j<n;j++)mm[j]=j;
		
		for(j=0;j<26;j++){
			int can = 0,ntot=0;
			for(k=0;k<tot;k++)if(pat(mm[k])){
				can |= key[mm[k]];
				//mm[ntot++] = mm[k];
			}
			//tot = ntot;
			
			if(can & (1<<(list[j] - 'a'))){
				if(key[i] & (1<<(list[j] - 'a'))){
					nkey |= (1<<(list[j] - 'a'));
					for(k=0;k<len[i];k++) if(D[i][k] == list[j])
						nn[k]=list[j];
				}else bmax++;
			}
			used[list[j] - 'a'] = 1;
			//cout<<nn<<endl;
		}
		if(bmax > amax){
			amax = bmax;
			ans = i;
		}
	}
	//printf(" (%d) ",amax);
	return ans;
}

int main(){
	int T,TC=1,m,i;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			cin>>D[i];
			len[i] = D[i].length();
			key[i] = 0;
			for(int j=0;j<len[i];j++)
				key[i] |= (1<<(D[i][j]-'a'));
		}
		printf("Case #%d:",TC++);
		for(i=0;i<m;i++){
			cin>>list;
			cout<<" "<<D[kero()];
		}
		printf("\n");
	}
}
