#include<iostream>
#include<cstring>
using namespace std;
int main(){
	int L,D,N;
	scanf("%d%d%d",&L,&D,&N);
	getchar();
	char Language[D][25];
	for(int i=0;i<D;i++)
		gets(Language[i]);
	for(int i=1;i<=N;i++){
		char input[5000];
		gets(input);
		char charlist[L][500];
		int ind1=0,ind2=0,len[L],length,now=0;
		length=strlen(input);
		for(int j=0;j<length;j++){
			if(input[j]=='('){
				j++;
				while(input[j]!=')')
					charlist[ind1][ind2++]=input[j], j++;
			}
			else
				charlist[ind1][ind2++]=input[j];
			len[ind1]=ind2, ind1++, ind2=0;
		}
		for(int j=0;j<D;j++){
			bool exist=true;
			for(int k=0;k<L;k++){
				bool present=false;
				for(int l=0;l<len[k];l++){
					if(Language[j][k]==charlist[k][l]){
						present=true;
						break;
					}
				}
				if(not present){
					exist=false;
					break;
				}
			}
			if(exist)
				now++;
		}
		printf("Case #%d: %d\n",i,now);
	}
	return 0;
}
