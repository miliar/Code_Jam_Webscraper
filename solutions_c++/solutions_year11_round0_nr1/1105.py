#include<cstdio>
#include<vector>
using namespace std;

int t, n, x;
char c;

int o, b;
vector<int> oseq, bseq;
int owsk, bwsk;
vector<char> seq;
int wsk=0;

void fajt(int przyp){
	int timer=0;
	while(wsk<seq.size()){
		timer++;
		bool clicked=0;
		// orange
		if(owsk<oseq.size()){
			if(oseq[owsk]>o) o++;
			else if(oseq[owsk]<o) o--;
			else if(seq[wsk]=='O'){
				clicked=1;
				wsk++;
				owsk++;
			}
		}
		// blue
		if(bwsk<bseq.size()){
			if(bseq[bwsk]>b) b++;
			else if(bseq[bwsk]<b) b--;
			else if(!clicked && seq[wsk]=='B'){
				wsk++;
				bwsk++;
			}
		}
	}
	printf("Case #%d: %d\n",przyp,timer);
}

int main(){
	scanf("%d",&t);
	for(int y=1; y<=t; y++){
		scanf("%d ",&n);
		o=1;
		b=1;
		owsk=0;
		bwsk=0;
		oseq.clear();
		bseq.clear();
		seq.clear();
		wsk=0;
		for(int i=0; i<n; i++){
			scanf("%c %d ",&c,&x);
			if(c=='O'){
				oseq.push_back(x);
				seq.push_back(c);
			}
			else{
				bseq.push_back(x);
				seq.push_back(c);
			}
		}
		fajt(y);
	}
}

