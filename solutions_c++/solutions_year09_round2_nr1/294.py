#include <stdio.h>
#include <string>
#include <string.h> 
#include <ctype.h>
#include <set>
using namespace std;

const int size=10000;
char s[size];

int main(){
	int N,L,A;
	scanf("%d",&N);
	for(int cs=1; cs<=N; cs++){
		printf("Case #%d:\n",cs); 
		scanf("%d",&L);
		char *p=s;
		fgets(s,100,stdin);
		while(L--){
			fgets(p,100,stdin);
			p+=strlen(p);
			*p=' ';
			p++;
		}
		*p=0;
		scanf("%d",&A);
		while(A--){
			int n,c;
			scanf("%*s%d",&n);
			set<string> m;
			char t[100];
			while(n--){
				scanf("%s",t);
				m.insert(string(t));
			}
			double d,r=1.0;
			p=s;
			while(1){
				while((*p)!='(') p++;
				p++;
				sscanf(p,"%lf%n",&d,&c);
				p+=c;
				r*=d;
				while((*p)!=')'&&!isalpha(*p)) p++;
				if((*p)==')') break;
				sscanf(p,"%s%n",t,&c);
				p+=c;
				if(m.find(string(t))!=m.end()) continue; 
				while((*p)!='(') p++;
				p++;
				c=1;
				while(c>0){
					if((*p)=='(') c++;
					if((*p)==')') c--;
					p++;
				}
			}
			printf("%.9lf\n",r);
		}
	}
	return 0;
} 
