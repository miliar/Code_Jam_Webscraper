# include <stdio.h>
# include <string.h>
# include <string>
# include <iostream>
# include <vector>

using namespace std;

int l, d, n, i, j, k, t;
char pal[64];
int mrc[5024];
vector<string> vet, vet2;
string pch;

int main (void){
	scanf("%d%d%d", &l, &d, &n);
	vet.clear();
	for(i=0;i<d;i++){
		scanf(" %s", pal);
		vet.push_back(pal);
	}
	for(i=1;i<=n;i++){
		vet2.clear();
		//printf("%d!!(((\n",  vet2.size());
		scanf(" %s", pal);
		pch = "";
		int mesma = 0;
		for(j=0;pal[j]!='\0';j++){
			if(pal[j]=='('){
				mesma = 1;
				continue;
			}
			else if(pal[j] == ')'){
				vet2.push_back(pch);
				pch = "";
				mesma = 0;
			}
			else{
				if(mesma == 1)
					pch+=pal[j];
				else{
					pch+=pal[j];
					vet2.push_back(pch);
					pch = "";
				}
			}
		}
		/*pch = strtok(pal, "() ");
		while(pch != NULL){
			puts(pch);
			vet2.push_back(pch);
			pch = strtok(NULL, "() ");
		}*/
		memset(mrc, 0, sizeof(mrc));
		for(j=0;j<l;j++){
			int tam = vet2[j].length();
			//cout << "Vendo " << vet2[j] << endl;
			for(k=0;k<tam;k++){
				//printf("agora no ind %d\n", k);
				for(t=0;t<d;t++){
					//cout << vet[t][j] << " " << vet2[j][k] <<endl;
					if(vet[t][j] == vet2[j][k]) {
						if(mrc[t] == j) mrc[t]++;
					}
				}
			}
		}
		int cnt = 0;
		for(j=0;j<d;j++) if(mrc[j] == l){
		//	printf("!!!!!!!!!! %d !!!!!!!\n", j);
			cnt++;
		}
		printf("Case #%d: %d\n", i, cnt);
	}
}