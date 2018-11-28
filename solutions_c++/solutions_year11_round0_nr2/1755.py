#include<cstdio>
#include<cstring>
using namespace std;
const int N=1000;
char com[100][100];
int  flag[100];
int opp[100][100];
bool oppp[100][100];
int stalk[N];
int n,d,c,i,j,t,l,tot,x;
char ch[10];
char ele[N];
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&t);
	for(l=1;l<=t;l++){
		printf("Case #%d: ",l);
		memset(com,0,sizeof(com));
		memset(opp,0,sizeof(opp));
		memset(flag,0,sizeof(flag));
		memset(oppp,0,sizeof(oppp));
	    scanf("%d",&c);
	    for(i=0;i<c;i++){
    		scanf("%s",&ch);
    		com[ch[0]][ch[1]]=ch[2];
    		com[ch[1]][ch[0]]=ch[2];
    	}
    	scanf("%d",&d);
    	for(i=0;i<d;i++){
	    	scanf("%s",&ch);
	    	opp[ch[0]][++opp[ch[0]][0]]=ch[1];
	    	opp[ch[1]][++opp[ch[1]][0]]=ch[0];
	    	oppp[ch[0]][ch[1]]=1;
    		oppp[ch[1]][ch[0]]=1;
	    }
	    scanf("%d",&n);
	    tot=-1;
	    scanf("%s",&ele);
	    for(i=0;i<n;i++){
    		flag[stalk[++tot]=ele[i]]++;
    		if(tot==0)continue;
    		if(com[stalk[tot]][stalk[tot-1]]){
  			  flag[stalk[tot]]--;flag[stalk[tot-1]]--;
    		  stalk[tot-1]=com[stalk[tot]][stalk[tot-1]];
    		  tot--;
    		  continue;
            }
            for(j=1;j<=opp[stalk[tot]][0];j++)
               if(flag[opp[stalk[tot]][j]]){
               	 memset(flag,0,sizeof(flag));
               	 tot=-1;
               	 break;
               }
    	}
    	printf("[");
    	if(tot>=0)printf("%c",stalk[0]);
    	for(i=1;i<=tot;i++)
    	 printf(", %c",stalk[i]);
   	    printf("]\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
