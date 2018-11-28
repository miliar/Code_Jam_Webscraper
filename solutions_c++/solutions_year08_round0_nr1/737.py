#include<stdio.h>;
#include<string.h>;
#include<stdlib.h>



char myName[102][110];
bool  is[102];

int cmp(const void* a,const void* b)
{
	return strcmp( (const char*)a, (const char*)b);
}

int Query(int up,int down,char *s){
	if(down>up)printf("Error!\n");
	int mid = (up + down)/2;
	int t = strcmp(myName[mid],s);
	if(t==0)return mid;
	else if(t<0)Query(up,mid+1,s);
	else Query(mid-1,down,s);
}

int main()
{
	freopen("A-large.in","r",stdin);

	freopen("A-large.out","w",stdout);

	int N,S,Q;
	int i,j,k;
	char tmp[110];
	int count1,count2;

	scanf("%d",&N);
	
	for(i=0;i<N;i++){
		scanf("%d",&S);
		fgets(tmp,105,stdin);
		for(j=0;j<S;j++){
			fgets(myName[j],105,stdin);
		}
		qsort(myName,S,sizeof(myName[0]),cmp);

		count2 = 0;
		count1 = S;
		memset(is,0,sizeof(is));
		scanf("%d",&Q);
		fgets(tmp,105,stdin);
		for(j=0;j<Q;j++){
			fgets(tmp,105,stdin);
			k = Query(S-1,0,tmp);
			if(is[k]==false){
				is[k]=true;
				count1--;
			}
			if(count1==0){
				count2++;
				count1 = S-1;
				memset(is,0,sizeof(is));
				is[k]=true;
			}
		}
		printf("Case #%d: %d\n",i+1,count2);
	}
	
	return 0;
}
