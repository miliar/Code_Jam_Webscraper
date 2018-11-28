#include<cstdio>
#include<iostream>
#include<cmath>

using namespace std;

int t, n, posb, poso, loko, lokb, jenis, tempat, inso[101],insb[101], waktu, overall;
bool urut[101];
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	
	for (int tc=0;tc<t;tc++){
		posb=1;
		poso=1;
		scanf("%d",&n);
		for (int i=1;i<=n;i++){
			scanf(" %c %d",&jenis,&tempat);
			if (jenis=='O'){
				inso[poso++]=tempat;
				urut[i]=false;
			}else{
				insb[posb++]=tempat;
				urut[i]=true;
			}
		}
		waktu = 0;
		posb=1;
		lokb=1;
		poso=1;
		loko=1;
		overall=1;
		while (overall<=n){
			if (!urut[overall]){
				waktu += abs(inso[poso]-loko)+1;
				if (abs(inso[poso]-loko)>=abs(insb[posb]-lokb)){
//					printf("%d %d mas\n",abs(inso[poso]-loko),abs(insb[posb]-lokb));
					lokb=insb[posb];
				}
				else if (lokb<insb[posb])lokb =lokb+ abs(inso[poso]-loko)+1;
				else if (lokb>insb[posb])lokb =lokb- abs(inso[poso]-loko)-1;
				loko=inso[poso];
				poso++;
				overall++;
			}else{
				waktu += abs(insb[posb]-lokb)+1;
				if (abs(insb[posb]-lokb)>=abs(inso[poso]-loko)){
//					printf("%d %d mas\n",abs(insb[posb]-lokb),abs(inso[poso]-loko));
					loko=inso[poso];
				}
				else if (loko<inso[poso])loko =loko+ abs(insb[posb]-lokb)+1;
				else if (loko>inso[poso])loko =loko- abs(insb[posb]-lokb)-1;
				lokb=insb[posb];
				posb++;
				overall++;
			}
//			printf("o:%d ins-o:%d ins-b:%d lok-o:%d lok-b:%d waktu:%d\n",overall,inso[poso],insb[posb],loko,lokb,waktu);
		}
		printf("Case #%d: %d\n",tc+1,waktu);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
