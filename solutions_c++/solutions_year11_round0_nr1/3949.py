#include<set>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<map>
#include<cstring>
using namespace std;
int eip[200];
int curpos[200];

int main(void){
    int tcnum;
    scanf("%d ", &tcnum);
    for (int z=1; z<=tcnum; z++){
	int mnum;
	scanf("%d", &mnum);
	memset(eip, 0, 200*sizeof(int));
	memset(curpos, 0, 200*sizeof(int));
	curpos['O']=curpos['B']=1;
	int tot=0;
	for (int k=0; k<mnum; k++){
	    char cr;
	    int d;
	    scanf(" %c %d ", &cr, &d);
	    int cost=1+max(0, abs(d-curpos[cr])-eip[cr]);
	    tot+=cost;
	    if (cr=='B'){
		eip['B']=0;
		eip['O']+=cost;
	    }
	    else{
		eip['O']=0;
		eip['B']+=cost;
	    }
	    curpos[cr]=d;
	}
	printf("Case #%d: %d\n", z, tot);
    }
    return 0;
}
