#include <cstdio>
#include <iostream>
#include <cstdlib>

using namespace std;

char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main(){
	//printf("%c",a[('a'+7)%26]);
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	
	int T;
	cin>>T;
	char c;
	scanf("%c",&c);
	for(int I=1;I<=T;++I){
		
		
		printf("Case #%d: ",I);
		while(scanf("%c",&c),c!='\n'){
			if(c==' '){
				printf(" ");
				continue;
			}else{
				printf("%c",a[(c+7)%26]);
			}
			
		}
		printf("\n");
		
	}

}
