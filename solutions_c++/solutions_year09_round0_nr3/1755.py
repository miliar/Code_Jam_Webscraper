#include <cstdio>
#include <vector>
#include <cstring>

const int inf=0x7FFFFFFF;
using namespace std;
typedef vector<int> vi;


int get(int M[][20],int dindex, int pindex, char *data,char *pat)
{
	
	if(pindex==19) return 1;
    if(M[dindex][pindex]!=-1) return M[dindex][pindex];
	
	int res=0;
	for(int i=dindex;i<strlen(data);i++)
	  if(data[i]==pat[pindex])  
	  res=(res + get(M,i+1,pindex+1,data,pat))%10000;
	
	return M[dindex][pindex]=res;	
}



int main()
{

int T;
scanf("%d\n",&T);

char data[502];
char *pat="welcome to code jam";

for(int i=0;i<T;i++)
{
int M[502][20];
gets(data);
memset(M,-1,strlen(data)*20*sizeof(int));
int result=get(M,0,0,data,pat);	
printf("Case #%d: %04d\n",i+1,result);

}

return 0;	
}

	



