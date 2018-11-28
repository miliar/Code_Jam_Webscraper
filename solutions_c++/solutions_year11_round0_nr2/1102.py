#include<cstdio>
#include<vector>
using namespace std;

int t;

void fajt(int przyp){
	char map[30][30];
	vector<int> opp[30];
	int c,d,n;

	vector<char> wyn;
	int isinwyn[30];

	for(int i=0; i<30; i++){
		isinwyn[i]=0;
		for(int j=0; j<30; j++) map[i][j]=0;
	}

	scanf("%d ",&c);
	for(int i=0; i<c; i++){
		char x,y,z;
		scanf("%c%c%c ",&x,&y,&z);
		map[x-'A'][y-'A']=z;
		map[y-'A'][x-'A']=z;
	}

	scanf("%d ",&d);
	for(int i=0; i<d; i++){
		char x,y;
		scanf("%c%c ",&x,&y);
		opp[x-'A'].push_back(y);
		opp[y-'A'].push_back(x);
	}

	scanf("%d ",&n);
	while(n--){
		c=getchar();
		if(!wyn.size()){
			isinwyn[c-'A']++;
			wyn.push_back(c);
			continue;
		}
		
#define wynlast wyn[wyn.size()-1]
		else if(map[wynlast-'A'][c-'A']){
			char tmp=map[wynlast-'A'][c-'A'];
			isinwyn[wynlast-'A']--;
			wyn.pop_back();
			isinwyn[tmp-'A']++;
			wyn.push_back(tmp);
			continue;
		}

		bool dupa=0;
		for(int i=0; i<opp[c-'A'].size(); i++){
			if(isinwyn[opp[c-'A'][i]-'A']){
				wyn.clear();
				for(int j=0; j<30; j++) isinwyn[j]=0;
				dupa=1;
				break;
			}
		}
		
		if(!dupa){
			wyn.push_back(c);
			isinwyn[c-'A']++;
		}
		
	}

	printf("Case #%d: [",przyp);
	for(int i=0; i<wyn.size(); i++){
		if(i+1<wyn.size()) printf("%c, ",wyn[i]);
		else printf("%c",wyn[i]);
	}
	printf("]\n");
}

int main(){
	scanf("%d ",&t);
	for(int y=1; y<=t; y++){
		fajt(y);
	}
}
