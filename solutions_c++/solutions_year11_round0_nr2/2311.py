#include<stdio.h>
#include<vector>
#include<memory.h>
#include<string>
using namespace std;
int t,c,d,n;
char str[105];
int count[255];
int main(){
	scanf("%d\n",&t);
	for(int I=1; I<=t; ++I){
		string o;
		memset(count,0,sizeof(count));
		vector<string> C,D;
	
		scanf("%d ",&c);
		for(int i=0;i<c;++i){
			scanf("%s ", str);
			C.push_back(str);
		}
		
		scanf("%d ",&d);
		for(int i=0;i<d;++i){
			scanf("%s ", str);
			D.push_back(str);
		}
		
		scanf("%d ",&n);
		scanf("%s",str);
		
		for(int i=0;i<n;++i){
			
			if(o.size()>=1){
				bool cont = 0;
				for(int j=0;j<c;++j)
					if((str[i]==C[j][0] && o[o.size()-1] == C[j][1]) ||
						(str[i]==C[j][1] && o[o.size()-1] == C[j][0]))
						{
							--count[(int)o[o.size()-1]];
							o[o.size()-1] = C[j][2];
							++count[(int)C[j][2]];
							cont = 1;
						}
				if(cont) continue;
			}
			if(o.size()>=1){
				bool cont = 0;
				for(int j=0;j<d;++j)
					if((str[i]==D[j][0] && count[(int)D[j][1]]) ||
						(str[i]==D[j][1] && count[(int)D[j][0]]))
						{
							o.resize(0);
							memset(count,0,sizeof(count));
							cont = 1;
						}
				if(cont) continue;
			}
			
			o+=str[i];
			++count[(int)str[i]];
			
			//printf(" %s\n",o.c_str());
		}
		printf("Case #%d: [",I);
		for(int i=0;i<(int)o.size();++i){
			if(i) printf(", ");
			printf("%c",o[i]);
		}
		printf("]\n");
	}
	return 0;
}
