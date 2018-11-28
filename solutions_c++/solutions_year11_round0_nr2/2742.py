#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
using namespace std;
#define C 38
#define D 30
char c[C][5], d[D][3];
char in[105], out[105];
int l, n, cc, dd;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T, cs, i, j, k;
	bool op;
	scanf("%d", &T);
	for(cs=1; cs<=T; cs++){
		scanf("%d", &cc);
		for(i=0; i<cc; i++)scanf("%s", c[i]);
		scanf("%d", &dd);
		for(i=0; i<dd; i++)scanf("%s", d[i]);
		scanf("%d%s", &n, in);
		memset(out, 0, sizeof(out));
		l=0;
		for(i=0; i<n; i++){
			if(l==0){out[l++]=in[i]; continue;}
			op=0;
			if(cc){
				for(j=0; j<cc; j++)
					if((in[i]==c[j][1] && out[l-1]==c[j][0]) || (in[i]==c[j][0] && out[l-1]==c[j][1])){
						out[l-1]=c[j][2];
						op=1;
						break;
					}
			}
			if(op)continue;
			if(dd){
				for(k=0; k<dd; k++){
					if(in[i]==d[k][0]){
						for(j=0; j<l; j++)
							if(out[j]==d[k][1])break;
						if(j!=l){
							memset(out, 0, sizeof(out));
							l=0;
							op=1;
							break;
						}
					}
					else if(in[i]==d[k][1]){
						for(j=0; j<l; j++)
							if(out[j]==d[k][0])break;
						if(j!=l){
							memset(out, 0, sizeof(out));
							l=0;
							op=1;
							break;
						}
					}
				}
			}
			if(!op){
				out[l++]=in[i];
			}
		}
		printf("Case #%d: [", cs);
		if(l!=0)printf("%c", out[0]);
		for(i=1; i<l; i++)printf(", %c", out[i]);
		puts("]");
	}

	return 0;
}