#include<iostream>
#include<algorithm>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int len,all,n,m,ans;
int g[5010*16][28],f[20][27];
string s;

void dfs(int x,int t){
	 if (x>len)
	 	ans++;
	 else
	 	fo(i,1,f[x][0])
	 		if (g[t][f[x][i]])
	 			dfs(x+1,g[t][f[x][i]]);
}

int creat(){
	 fo(i,0,26)g[all+1][i]=0;
	 return ++all;
}

int main(){
	freopen("al.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d%d%d\n",&len,&n,&m);
	all=0;
	creat();
	fo(i,1,n){
		cin>>s;
		int t=1;
		fo(j,0,len-1){
			if (!g[t][s[j]-97])
				g[t][s[j]-97]=creat();
			t=g[t][s[j]-97];
		}
	}
	fo(i,1,m){
		cin>>s;
		fo(j,1,len){
			f[j][0]=0;
			if (s[0]=='('){
				fo(k,1,s.find(')')-1)
					f[j][++f[j][0]]=s[k]-97;
				s.erase(0,s.find(')')+1);
			}
			else{
				f[j][++f[j][0]]=s[0]-97;
				s.erase(0,1);
			}
		}
		ans=0;
		dfs(1,1);
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}


			
			
				
			
	
	
