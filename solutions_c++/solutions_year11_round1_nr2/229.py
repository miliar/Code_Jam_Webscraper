#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
bool mat[110][110][30];
bool aru[110][30];
string st[110];int len[110];
int main()
{
	int i,j,k,l,m,n,o,p,t;string s;cin>>t;
	for(i=0;i<t;i++){
		//memset(mat,false,sizeof(mat));
		memset(aru,false,sizeof(aru));
		cin>>n>>m;
		for(j=0;j<n;j++){
			cin>>st[j];len[j]=st[j].size();
			for(k=0;k<len[j];k++){
				aru[j][(st[j][k]-'a')]=true;
			}
		}
		printf("Case #%d: ",i+1);
		for(o=0;o<m;o++){
			cin>>s;memset(mat,false,sizeof(mat));
			for(j=0;j<n;j++) for(k=0;k<n;k++){
				if(len[j]==len[k]) mat[j][k][0]=true;
				for(l=0;l<26;l++){
					if(!mat[j][k][l]) continue;
					int f=1;
					for(p=0;p<len[j];p++){
						if((st[j][p]==s[l] && st[k][p]!=s[l]) || (st[j][p]!=s[l] && st[k][p]==s[l])) f=0;
					}
					if(f>0) mat[j][k][l+1]=true;
				}
			}
			int ma=-1;string ret="";
			for(j=0;j<n;j++){
				int kei=0;
				for(k=0;k<26;k++){
					int f=0;
					for(l=0;l<n;l++){
						if(mat[j][l][k] && aru[l][(s[k]-'a')]) f=1;
					}
					if(f>0 && !aru[j][(s[k]-'a')]) kei++;
				}
//				cout<<kei<<endl;
				if(ma<kei){ma=kei;ret=st[j];}
			}
			cout<<ret;if(o<m-1) cout<<" ";else cout<<endl;
		}
	}
	return 0;
}
