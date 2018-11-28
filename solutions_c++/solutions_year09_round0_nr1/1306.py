#include <stdio.h>
#include <algorithm>
using namespace std;

int l,d,n,pos1,pos2,res;
char kamus[5010][20],buff[1000];
bool ada[20][30],ok,buka;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d %d %d",&l,&d,&n);
	for (int i=0;i<d;i++)
		scanf("%s",kamus[i]);
	for (int i=0;i<n;i++){
		res=0;
		scanf("%s",buff);
		pos1=0,pos2=0;
		memset(ada,false,sizeof(ada));
		buka=false;
		while (buff[pos1]){
			if (buff[pos1]=='('){
				//new token
				buka=true;
			}
			else if (buff[pos1]==')'){
				//increase the token
				pos2++;
				buka=false;
			}
			else{
				//add the current token
				if (buka) ada[pos2][(buff[pos1]-'a')]=true;
				else ada[pos2++][(buff[pos1]-'a')]=true;
			}
			pos1++;
		}
		for (int j=0;j<d;j++){
			ok=true;
			for (int k=0;k<l;k++)
				if (!ada[k][(kamus[j][k]-'a')]){
					ok=false;
					break;
				}
			if (ok) res++;
		}
		printf("Case #%d: %d\n",(i+1),res);
	}
	return 0;
}