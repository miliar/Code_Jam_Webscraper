#include <cstdio>
#include <cstring>
#include <cstdlib>
#define rep(i,n) for(int i=0,_n=(n);i<_n;i++)
using namespace std;
int combined[200][200],opp[200][200];
char stSoal[200], arc[200][20],ard[200][20];

int main () {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int nCase, c,d;
	char st[200];   
	scanf("%d",&nCase);
	for(int iCase=0;iCase<nCase;iCase++){
		int len =0;
		scanf("%d",&c);
		memset(combined,0,sizeof(combined));
		memset(opp,0,sizeof(opp));
		rep(i,c){
			scanf("%s",arc[i]);
			combined[arc[i][0]][arc[i][1]]=arc[i][2];
			combined[arc[i][1]][arc[i][0]]=arc[i][2];
		}
		scanf("%d",&d);
		rep(i,d){
			scanf("%s",ard[i]);
			opp[ard[i][0]][ard[i][1]]=1;
			opp[ard[i][1]][ard[i][0]]=1;
		}
		int lenSoal;
		scanf("%d",&lenSoal);
		scanf("%s",stSoal);

		rep(i,strlen(stSoal)){
			st[len++]=stSoal[i];
			while(len>=2){
				if(combined[st[len-1]][st[len-2]]!=0){
					st[len-2]=combined[st[len-1]][st[len-2]];
					len--;
				}else{
					break;
				}
			}
									   rep(j,len-1){
									   if(opp[st[len-1]][st[j]]){
											  len=0;
									   }
									   }
		}
											  printf("Case #%d: [",iCase+1);
											  rep(k,len){
											  if(k>0)printf(", ");
											  printf("%c",st[k]);
											  }
											  printf("]\n");
	}
    return 0;
}
