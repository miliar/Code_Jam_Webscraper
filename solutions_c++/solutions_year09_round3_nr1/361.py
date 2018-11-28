#include <stdio.h>
#include <string.h>

int main(){
	int Case, Cases;
	char Num[100];
	int act;
	bool is_in[256];
	char Base[100];
	scanf("%d",&Cases);
	for(Case=1;Case<=Cases;Case++){
		scanf(" %s",Num);
		memset(is_in,0,255);
		memset(Base,'!',100);
		act = 0;
		int i;
		for(i=0;Num[i]!='\0';i++){
			if(!is_in[(int)Num[i]]) {
				is_in[(int)Num[i]] = 1;
			//	printf("O char %c e' %d\n",Num[i],act);
				Base[act] = Num[i];
				act++;
			}
		}
		if(act == 1)act++;
		int Tam = act;
		int tmp = Base[1];
		Base[1] = Base[0];
		Base[0] = tmp;
		int v[256];
		for(int j = 0;j<100;j++){
			if(Base[j]!='!'){
				v[(int)Base[j]] = j;
			//	printf("O char %c e' %d com base: %d-> %d\n",Base[j],v[(int)Base[j]],Tam,(int)Base[j]);
				
			}
		}
		unsigned long long resp = 0;
		unsigned long long multi = 1;
		for(i--;i>=0;i--){

			resp+=((unsigned long long)v[(int)Num[i]])*multi;
			multi*=((unsigned long long)Tam);
		}
		printf("Case #%d: %Ld\n",Case,resp);

		
	}
	return 0;
}
