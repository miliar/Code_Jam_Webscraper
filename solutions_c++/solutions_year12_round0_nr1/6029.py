#include <stdio.h>
#include <string>

using namespace std;

void main(){
	char clave[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	//char clave[27]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
	//char clave[27]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char G[102];
	char S[102];
	int T=0;
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("salida.out","w",stdout);
	scanf("%d\n",&T);
	for(int j=1;j<=T;++j){
		gets(G);
		string s=G;
		for(int i=0;i<s.size();++i){
			if(G[i]==' ')S[i]=G[i];
			else
				S[i]=clave[G[i]-'a'];
		}
		S[s.size()]='\0';
		printf("Case #%d: %s\n",j,S);
	}
}