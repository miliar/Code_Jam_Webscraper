#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<algorithm>
#include<functional>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<complex>
#define EPS (1e-10)
#define PI (3.141592653589793238)
#define MP make_pair
typedef long long ll;
using namespace std;

char com[256][256];
bool des[256][256];

int main(void){
	int T;
	scanf("%d",&T);
	for(int casenum=1;casenum<=T;casenum++){
		int i,j;
		int c,d,n;
		string invoke;
		for(i=0;i<256;i++)for(j=0;j<256;j++){com[i][j]=0;des[i][j]=false;}
		scanf("%d",&c);
		for(i=0;i<c;i++){
			string st;
			cin >> st;
			com[st[0]][st[1]]=st[2];
			com[st[1]][st[0]]=st[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++){
			string st;
			cin >> st;
			des[st[0]][st[1]]=true;
			des[st[1]][st[0]]=true;
		}
		scanf("%d",&n);
		cin >> invoke;
		vector<char> ans;
		for(i=0;i<n;i++){
			ans.push_back(invoke[i]);
			bool comb=false;
			if(ans.size()>=2){
				char ch=com[ans[ans.size()-1]][ans[ans.size()-2]];
				if(ch!=0){
					ans.erase(ans.end()-2,ans.end());
					ans.push_back(ch);
					comb=true;
				}
			}
			if(!comb){
				for(j=0;j<(int)ans.size()-1;j++){
					if(des[ans[j]][invoke[i]]){
						ans.clear();
						break;
					}
				}
			}
		}
		printf("Case #%d: [",casenum);
		for(i=0;i<ans.size();i++){
			printf("%c",ans[i]);
			if(i<(int)ans.size()-1)printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
