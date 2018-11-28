
#include <cstdio>
#include <fstream>

#define D 5005
#define ALPH 30
#define L 20

using namespace std;

char ptrn[D][L],data[500];
int chr[ALPH],can[D],cnt,cnt2,tc=1;
int l,d,n;

FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");


int main(){
	int i,j,k,pnt;
	fscanf(in,"%d %d %d",&l,&d,&n);
	for (i=0;i<d;i++){
		fscanf(in,"%s",&ptrn[i]);
	}
	for (i=0;i<n;i++){
		fscanf(in,"%s",&data);
		for(j=0;j<d;j++){
			can[j]=j;
		}
		cnt=d;
		pnt=0;
		for(j=0;j<l;j++){
			memset(chr,0,sizeof(chr));
			if (data[pnt]!='('){
				chr[data[pnt]-'a']=1;
			}else{
				while(data[++pnt]!=')'){
					chr[data[pnt]-'a']=1;	
				}
			}
			pnt++;
			cnt2=0;
			for(k=0;k<cnt;k++){
				if (chr[ptrn[can[k]][j]-'a']){
					can[cnt2++]=can[k];
				}
			}
			cnt=cnt2;
		}
		fprintf(out,"Case #%d: %d\n",tc++,cnt);
	}
	return 0;
}