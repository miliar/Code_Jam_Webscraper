#include<stdio.h>
#include<string.h>


struct combine{char el[3];};
struct destr{char el[2];};

bool cek(char a,char b,char aa,char bb){
	if((a==aa&&b==bb) || (a==bb&&b==aa))
		return true;
	return false;
}

int main(){
	int cs;
	scanf("%d",&cs);
	for(int ct=1;ct<=cs;ct++){
		int c;
		scanf("%d",&c);getchar();
		combine comb[c];
		for(int i=0;i<c;i++){
			scanf("%c%c%c",&comb[i].el[0],&comb[i].el[1],&comb[i].el[2]); getchar();
		}
		int d;
		scanf("%d",&d);getchar();
		destr dest[d];
		for(int i=0;i<d;i++){
			scanf("%c%c",&dest[i].el[0],&dest[i].el[1]); getchar();
		}

		int s;
		scanf("%d",&s);getchar();
		char list[s];
		memset(list,0,sizeof(list));
		int nlist=0;
		for(int i=0;i<s;i++){
			scanf("%c",&list[nlist++]);
			if(nlist>=2){
				bool flag=0;
				for(int j=0;j<c;j++){ //cek combined
					if(cek(list[nlist-1], list[nlist-2], comb[j].el[0], comb[j].el[1])){
						nlist--;
						list[nlist-1]=comb[j].el[2];

						flag=1;
					}
				}
				if(!flag){
					flag=0;
					for(int j=0;j<d&&!flag;j++){
						for(int k=0;k<nlist-1&&!flag;k++){
							if(cek(list[nlist-1],list[k],dest[j].el[0],dest[j].el[1])){
								nlist=0;
								flag=1;
							}
						}
					}
				}
			}

		}

		printf("Case #%d: [",ct);
		for(int i=0;i<nlist-1;i++){
			printf("%c, ",list[i]);
		}
		if(nlist)
		printf("%c]\n",list[nlist-1]);
		else
		printf("]\n");
	}
	return 0;
}
