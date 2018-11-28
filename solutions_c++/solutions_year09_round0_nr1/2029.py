#include <cstdio>
using namespace std;

int main(){
  int L,D,N;
  scanf("%d%d%d",&L,&D,&N);
  char words[D][L+1];
  for(int i=0; i<D; i++)
    scanf("%s",words[i]);
  bool patternArray[L][128];
  char pattern[100000];
  for(int i=1; i<=N; i++){
    for(int j=0; j<L; j++)
	for(int k='a'; k<='z'; k++)	
	    patternArray[j][k]=false;    
    scanf("%s",pattern);
    int k=-1;
    for(int j=0; j<L; j++){
	if(pattern[++k]=='('){
	    while(pattern[++k]!=')')
		patternArray[j][pattern[k]]=true;
	}else patternArray[j][pattern[k]]=true;
    }
    int result=0;
    for(int j=0; j<D; j++){
	int k;
	for(k=0; k<L; k++)
	   if(!patternArray[k][words[j][k]])
		break;
	if(k==L)
	   result++;	
    }
    printf("Case #%d: %d\n",i,result);
  }
}
