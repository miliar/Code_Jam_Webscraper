#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int main(){
	int n;
	scanf("%d\n",&n);
	char buffer[10000];
	for(int l=0;l<n;l++){
		fgets(buffer,10000,stdin);
		//printf("#%s#\n",buffer);
		string text = string(buffer);
		//printf("#%s#\n",(char*)text.c_str());
		string searchString = "welcome to code jam";
		vector< pair<int,int> > pares[19];


	
		for(int i=0;i<text.size();i++){
			if(text[i]=='m'){
				pares[18].push_back( pair<int, int> (i,1));
			}
		}
		int mod = 10000;
		for(int i=searchString.size()-2;i>=0;i--){
			for(int j=0;j<text.size();j++){
				if(text[j]==searchString[i]){
					int num = 0;
					for(int k=0;k<pares[i+1].size();k++){
						int posProxPar = (pares[i+1][k]).first;
						if(posProxPar > j)
							num = ((num % mod) + (pares[i+1][k].second % mod))%mod;
					}
					if(num!=0){
						pares[i].push_back( pair<int,int> (j,num) );
			//			printf("pushing i:%d j:%d num:%d\n",i,j,num);
					}
				}
			}
		}
		int ans = 0;
		for(int i=0;i<pares[0].size();i++){
			ans= ((ans%mod)+ (pares[0][i].second ) % mod)%mod;
		}
		printf("Case #%d: %04d\n",l+1,ans);
	}
}
