#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

char L[27];

struct Node{
	int idx;
	string org;
	string cur;
	int msk,step;
	friend bool operator < (const Node& p1,const Node& p2){
		return p1.cur < p2.cur;
	}
};

const int maxn = 10000 + 10;
int n,m;
Node D[maxn];

void work(){
	for(int i = 0 ;i<n;i++){
		D[i].step = 0;
		D[i].cur = string(D[i].org.size(),'#');
	}

	for(int cur = 0;cur < 26;cur++){
		int ch = L[cur];
		int mask = 1<<(ch - 'a');

		sort(D,D + n);
		/*for(int i = 0;i<n;i++)
			cout<<D[i].cur<<';';
		cout<<endl;
		for(int i = 0;i<n;i++)
			cout<<D[i].step<<' ';
		cout<<endl;*/
		for(int i = 0 ;i<n;){
			int j;
			for(j = i;j<n;j++)
				if(D[j].cur!=D[i].cur)break;
			bool has = false;
			for(int k = i;k<j;k++)
				if((D[k].msk & mask)>0){
					has = true;
					break;
				}
			if(has){
				for(int k = i;k<j;k++)
					if((D[k].msk & mask)==0)
						D[k].step++;
			}
			i = j;
		}
		for(int i = 0;i<n;i++)
			if((D[i].msk & mask)>0){
				int len = D[i].org.size();
				for(int j = 0;j<len;j++)
					if(D[i].org[j]==ch)
						D[i].cur[j]=ch;
			}
	}
	int best = 0,bestone = 0;
	for(int i = 0;i<n;i++)
		if(D[i].step>best){
			best = D[i].step;
			bestone = i;
		}else if(D[i].step==best && D[i].idx < D[bestone].idx){
			bestone = i;
		}
	printf(" %s",D[bestone].org.c_str());
}

int main(){
	int T;
	cin>>T;
	for(int tc =1 ;tc<=T;tc++){
		cin>>n>>m;
		for(int i=0;i<n;i++){
			cin>>D[i].org;
			int len = D[i].org.size();
			D[i].msk = 0;
			D[i].idx = i;
			for(int j=0;j<26;j++){
				for(int k = 0;k<len;k++){
					if(D[i].org[k]=='a' + j){
						D[i].msk |= 1<<j;
						break;
					}
				}
			}
		}
		printf("Case #%d:",tc);
		for(int i = 0;i<m;i++){
			cin>>L;
			work();
		}
			
		puts("");

	}

	return 0;
}
