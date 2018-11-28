#include <iostream>
using namespace std;
int form[32][32];
bool clear[32][32];
int i,j,k,l,m,n,xys,ysc;
char st[128],ans[128];
int anslen,len;
void work1()
{
	if (anslen==1)return;
	if (form[ans[anslen-1]][ans[anslen-2]]!=0)
	{
		ans[anslen-2]=form[ans[anslen-1]][ans[anslen-2]]-1;
		anslen--;
	}
}
void work2()
{
	for (int i=anslen-2;i>=0;--i){
		if(clear[ans[i]][ans[anslen-1]]){
			anslen=0;
			return;
		}
	}
}
void getans()
{
     anslen=0;
	 for (int i=0;i<len;i++){
		 ans[anslen++]=st[i]-'A';
		 work1();
		 work2();
     }
	 return;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&ysc);
	for (xys=1;xys<=ysc;++xys){
        memset(form,0,sizeof(form));
		memset(clear,false,sizeof(clear));
		char stt[8];
	    scanf("%d",&m);
	    for (i=1;i<=m;++i){
		    scanf("%s",stt);
		    form[stt[0]-'A'][stt[1]-'A']=stt[2]-'A'+1;
		    form[stt[1]-'A'][stt[0]-'A']=stt[2]-'A'+1;
        }
	    scanf("%d",&m);
	    for (i=1;i<=m;++i){
		    scanf("%s",&stt);
		    clear[stt[0]-'A'][stt[1]-'A']=1;
		    clear[stt[1]-'A'][stt[0]-'A']=1;
        }
	    scanf("%d",&len);	
	    scanf("%s",&st);
		getans();
		printf("Case #%d: ",xys);
		printf("[");
	    if (anslen!=0){
           for (i=0;i<anslen-1;++i) printf("%c, ",ans[i]+'A');
           printf("%c",ans[i]+'A');
        }
        printf("]\n");
	}
	return 0;
}
