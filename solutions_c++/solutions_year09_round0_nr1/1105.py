/*Problema A - Google Code  Jam*/
#include <iostream>
#include <vector>

using namespace std;

int k,sz;
string str,ret;

void siguiente(){
	if(str[k]=='('){
		k++;
		ret="";
		while(str[k]!=')'){
			ret+=str[k];
			k++;
		}
		k++;
	}else{
		ret="A";
		ret[0]=str[k];
		k++;
	}
}
int main(){
	int len,nro_p,nro_q,longitud,indice;


	scanf("%d %d %d",&len,&nro_p,&nro_q);
	string vc[nro_p];

	for(int i=0;i<nro_p;i++)
		cin>>vc[i];
	for(int i=1;i<=nro_q;i++){
		cin>>str;
		sz=str.length();
		k=0;
		indice=0;
		vector<bool> valido(nro_p,true);

		while(k<sz){
			siguiente();
			//ret es mi siguiente token
			longitud=ret.length();
			vector<bool> esta_letra('z'+1,false);
			for(int j=0;j<longitud;j++)
					esta_letra[(int)ret[j]]=true;
			for(int j=0;j<nro_p;j++)
				if(!esta_letra[vc[j][indice]])
					valido[j]=false;
			indice++;
		}
		int res=0;
		if(indice==len)
			for(int j=0;j<nro_p;j++)
				res+=valido[j];
		printf("Case #%d: %d\n",i,res);
	}
}
/*
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zxy)bc




3 5 5
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zxy)bc
(abcd)(abcd)

*/
