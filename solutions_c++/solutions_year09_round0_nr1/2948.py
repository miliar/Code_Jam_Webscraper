#include "stdafx.h"
int l,d,n;

map<char,void*>dict;
char tmpstr[2048];
map<char,void*>::iterator pit;
void init(){
	map<char,void*>*pdict;
	map<char,void*>*pdict2;
	
	int pos;
	scanf("%d%d%d",&l,&d,&n);
	gets(tmpstr);
	for(int i=0;i<d;i++){
		pdict=&dict;
		gets(tmpstr);
		pos=0;
		for(int x=0;x<l;x++){
			if((pit=(pdict->find(tmpstr[pos])))==pdict->end()){
				pdict2=new map<char,void*>;
				pdict->insert(pair<char,void*>(tmpstr[pos],pdict2));
				pdict=pdict2;
			}else{
				pdict=(map<char,void*>*)pit->second;
			}
			pos++;
		}
	}
}

int recursesolve(char* pstr,map<char,void*>*pdict,char* curchar){
	char* pstr2;
	char* pend;
	int ret=0;
	
	if(curchar){
		if(*curchar==0)
			return 1;
		if((pit=(pdict->find(*curchar)))!=pdict->end()){
			if(curchar==pstr)//bugfix
				pstr++;
			if(*pstr=='(')
				return recursesolve(pstr,(map<char,void*>*)pit->second,NULL);
			else{
				return recursesolve(pstr,(map<char,void*>*)pit->second,pstr);
			}
		}
		return 0;
	}else if(*pstr=='('){
		pend=strchr(++pstr,')');
		while(pstr<pend){
			ret+=recursesolve(pend+1,pdict,pstr);
			pstr++;
			
		}
		return ret;
	}else if(*pstr==0)
		return 1;
}
/*int solve(char* pstr){
	for(int x=0;x<l;x++){
		if(*pstr=='('){
			recursesolve(pstr,&dict,NULL);
		}
	}
}*/


int main(){
int ret;
	//	freopen("..\\A-small-practice.in","r",stdin);
//	freopen("..\\A-small-practice.out","w",stdout);
	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A-large.out","w",stdout);
	init();	
	for (int caseId=1;caseId<=n;caseId++){
		printf("Case #%d: ",caseId);
		gets(tmpstr);
		
		if(tmpstr[0]=='(')
			ret=recursesolve(tmpstr,&dict,NULL);
		else
			ret=recursesolve(tmpstr,&dict,tmpstr);
		printf("%d\n",ret);
		fflush(stdout);
	}
	return 0;
}

