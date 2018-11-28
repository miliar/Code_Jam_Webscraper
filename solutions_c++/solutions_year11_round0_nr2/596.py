#include<cstdio>
#include<string>
#include<cstring>
using namespace std;
struct ponto{
	char a,b,c;
	};

int main(){
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++){
		printf("Case #%d: [",caso);
		ponto junc[40],rep[40];
		int m,n;
		scanf("%d",&m);
		for(int i=0;i<m;i++)
			scanf(" %c %c %c",&junc[i].a,&junc[i].b,&junc[i].c);
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf(" %c %c",&rep[i].a,&rep[i].b);
		string s="";
		int q;
		scanf("%d",&q);
		int v[26];
		memset(v,0,sizeof(v));
		while(q--){
			char c;
			scanf(" %c",&c);
		   int juntou=0;
		   for(int i=0;s.size() && i<m;i++){
		   	if( (s[s.size()-1]==junc[i].a && c==junc[i].b) ||
		   	    (s[s.size()-1]==junc[i].b && c==junc[i].a)){
		   		v[s[s.size()-1]-'A']--;
		   		s[s.size()-1]=junc[i].c;
		   		juntou=1;
		   		break;
		   	}
		   }
		   if(juntou)continue;
		   for(int i=0;i<n;i++){
		   	if( (v[rep[i].a-'A'] && c==rep[i].b) ||
		   	    (v[rep[i].b-'A'] && c==rep[i].a)){
		   		memset(v,0,sizeof(v));
		   		s="";
		   		juntou=1;
		   		break;		
		   	}
		   }
		   if(juntou)continue;
			s+=c;
			v[c-'A']++;		   
		}
		if(s.size())printf("%c",s[0]);
		for(int i=1;i<(int)s.size();i++)		
			printf(", %c",s[i]);
		printf("]\n");

	}
	return 0;
}
