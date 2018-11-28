#include<stdio.h>
#include<iostream>
#include<vector>
#include<math.h>
#include<algorithm>
#include<memory.h>
#include<map>
#include<queue>

using namespace std;


int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);	
	int t=0;
	cin >> t;
	for (int ee=1;ee<=t;ee++){
		int n;
		string s="";
		char q[33][33],e[33][33],g[111111];
		memset(q,0,sizeof(q));
		memset(e,0,sizeof(e));
		cin >> n;
		for (int i=0;i<n;i++){
			cin >> s;
			q[s[0]-'A'][s[1]-'A']=q[s[1]-'A'][s[0]-'A']=s[2];
		}
		cin >> n;
		for (int i=0;i<n;i++){
			cin >> s;
			e[s[0]-'A'][s[1]-'A']=e[s[1]-'A'][s[0]-'A']='F';
		}
		cin >> n;
		char w;
		int v=0;
		for (int i=0;i<n;i++){
			cin >> w;
			g[v++]=w;
			while (v>1&&q[g[v-2]-'A'][g[v-1]-'A']){
				g[v-2]=q[g[v-2]-'A'][g[v-1]-'A'];
				v--;
			}
			for (int ii=0;ii<v;ii++)for (int jj=ii;jj<v;jj++)if (e[g[ii]-'A'][g[jj]-'A']=='F')v=0;
		}
		cout << "Case #" << ee << ": ";
		cout << "[";
		for (int i=0;i<v-1;i++)cout << g[i] << ", ";
		if (v)cout << g[v-1];
		cout  << "]" << endl;
	}
	return 0;
}


