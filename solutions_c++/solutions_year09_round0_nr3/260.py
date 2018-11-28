#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)

char texto[550];
char busca[]="welcome to code jam";
int cant[550][20];

int main(){
	int casos,c;
	
	fgets(texto, 550, stdin);
	sscanf(texto,"%d",&casos);
	for (c=0;c<casos;c++){
		cout<<"Case #"<<c+1<<": ";
		
		fgets(texto,550,stdin);
		int i,j,largo=strlen(texto)-1;
		
		memset(cant,0,sizeof(cant));
		
		for (i=0;i<largo;i++) for (j=0;j<19;j++){
			if (busca[j]==texto[i]){
				if (j==0){
					cant[i][j]=1;
					continue;
				}
				int k;
				
				for (k=0;k<i;k++) cant[i][j]+=cant[k][j-1];
				cant[i][j]%=10000; 
			}
		}
		int rta=0;
		
		for (i=0;i<largo;i++) rta=(rta+cant[i][18])%10000;
		int pot=1000;
		
		while (rta<pot){ cout<<"0"; pot/=10; }
		if (rta) cout<<rta;
		cout<<endl;
	}
	
	return 0;
}
