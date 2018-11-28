#include<iostream>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<map>
#include<set>
#include<vector>

using namespace std;

int comp(const void *a,const void *b){
	int *x,*y;
	x=(int*)a;y=(int*)b;
	if(*x > *y)
		return -1;
	return 1;
}

int main(){
	int tc,ntc,p,k,l,i;
	int let[1001];
	scanf("%d",&ntc);

	for(tc=0;tc<ntc;tc++){
		scanf("%d %d %d",&p,&k,&l);
		for(i=0;i<l;i++)
			scanf("%d",let+i);
		qsort(let,l,sizeof(int),comp);
		long long int total=0;
		int tecla=0;
		int pos = 1;

		for(i=0;i<l;i++){
			total += let[i]*pos;
			tecla++;
			if(tecla == k){
				tecla = 0;
				pos++;
			}
		}
		cout <<"Case #"<<tc+1<<": "<<total<<endl;

	}

}
