#include<deque>
#include<cstdio>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

int main(){
	int T0; scanf("%d",&T0);
	for(int T=1;T<=T0;T++){
		int nc; scanf("%d",&nc);
		char com[128][128]={};
		rep(i,nc){
			char s[4]; scanf("%s",s);
			com[s[0]][s[1]]=s[2];
			com[s[1]][s[0]]=s[2];
		}

		int no; scanf("%d",&no);
		bool opp[128][128]={};
		rep(i,no){
			char s[4]; scanf("%s",s);
			opp[s[0]][s[1]]=true;
			opp[s[1]][s[0]]=true;
		}

		int n; scanf("%d ",&n);
		int cnt[128]={};
		deque<char> dq;
		rep(i,n){
			char c=getchar();
			if(!dq.empty() && com[dq.back()][c]){
				c=com[dq.back()][c];
				cnt[dq.back()]--;
				dq.pop_back();
			}
			dq.push_back(c);
			cnt[c]++;
			for(int a='A';a<='Z';a++) if(opp[c][a] && cnt[a]>0) {
				while(!dq.empty()) dq.pop_back();
				fill(cnt+'A',cnt+'Z'+1,0);
				break;
			}
		}

		printf("Case #%d: [",T);
		rep(i,dq.size()){
			printf("%c",dq[i]);
			if(i<dq.size()-1) printf(", ");
		}
		puts("]");
	}

	return 0;
}
