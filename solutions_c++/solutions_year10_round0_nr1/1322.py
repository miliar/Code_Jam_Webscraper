#include <ios>
#define IFILE "input.txt"
#define OFILE "output.txt"
bool ar[12];
int main(){
	int T,N,K,t;
	freopen(IFILE,"r",stdin);
	freopen(OFILE,"w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d%d",&N,&K);
		printf("Case #%d: %s\n",t,(K&((1<<N)-1))==((1<<N)-1)?"ON":"OFF");
	}
	return 0;
}


