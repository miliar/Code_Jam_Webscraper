#include<stdio.h>
#include<stdlib.h>

const int MAX = 2000;

int cmp(const void* p1, const void* p2){
	long pp1= *((long *)p1);
	long pp2= *((long *)p2);
	return pp2-pp1;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int n,p,k,L;
	long str[MAX];
	scanf("%d",&n);
	for(int caseID=1;caseID<=n;caseID++){
		scanf("%d%d%d",&p,&k,&L);
		for(int i=0;i<L;i++){
			scanf("%ld",&str[i]);
		}
		qsort(str,L,sizeof(long),cmp);
		__int64 sum=0;
		int ptr=0;
		bool flag=false;
		for(int i=1;i<=p;i++){
			for(int j=1;j<=k;j++){
				sum+=str[ptr]*i;
				ptr++;
				if(ptr>=L){
					flag=true;
					break;
				}
			}
			if(flag==true)	break;
		}
		printf("Case #%d: %I64d\n",caseID,sum);
	}

	return 0;
}
