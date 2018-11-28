//Jakub Sygnowski
#include <cstdio>
#include <string>
#define REP(I,N) for(int I=0;I<(N);I++)
using namespace std;
int n,d,l,res,it;
bool dost[30][50];
string tab[5007];
char tem[10000];
string ciag;
bool erro;
int main(){
	scanf("%d%d%d",&l,&d,&n);
	REP(i,d){
		scanf("%s",tem);
		tab[i]=tem;
	}
	REP(nr,n){
		res=0;
		scanf("%s",tem);
		ciag=tem;
		REP(i,l) REP(lit,'z'-'a'+1) dost[i][lit]=false;
		it=0;
		REP(i,ciag.size()){
			if (ciag[i]=='('){
				while(ciag[i]!=')'){
					i++;
					if (ciag[i]==')') break;
					dost[it][ciag[i]-'a']=true;
				}	
			}
			else {
				dost[it][ciag[i]-'a']=true;
			}
			it++;
		}
	/*	REP(i,l){
			REP(lit,'z'-'a'+1) if (dost[i][lit]) printf("%c ",lit+'a');
			printf("\n");
		}*/
		//if (nr==4) return 0;

		REP(i,d){
			erro=false;
		//	printf("%s\n",tab[i].c_str());
			REP(s,tab[i].size()){
		//		printf("%d %d\n",s,tab[i][s]-'a');
				if (!dost[s][tab[i][s]-'a']){
					erro=true;
					break;
				}
			}
			if (!erro) res++;
		}
		printf("Case #%d: %d\n",nr+1,res);
	}
}
