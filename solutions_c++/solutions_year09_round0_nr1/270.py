#define MD(x) if (0) {x;}
#include <iostream>
#include <cstring>
#include <algorithm>
void MyAssert(int p){ if (!p) while (true) printf("error\n");}
using namespace std;

const int maxL = 20;
const int maxD = 5010;
const int maxM = 30;  // letters

char name[maxD][maxL];
bool p[maxL][maxM];
char s[1<<12];

int main(){
	int L,D,N;
	scanf("%d%d%d\n",&L,&D,&N);
	for (int i=0; i<D; i++)
		scanf("%s",name[i]);
	for (int i=0; i<N; i++){
		scanf("%s",s);
		MD(printf("%s:%d\n",s,strlen(s));)
		memset(p,false,sizeof(p));
		bool in=false;
		int k=0;

		for (int j=0; s[j]; j++){
			if (s[j]=='('){
				in = true;
			}
			else if (s[j]==')'){
				in = false;
				k++;
			}
			else if (s[j]>='a' && s[j]<='z'){
			     p[k][ s[j]-'a' ] = true;
				 if (!in) k++;			
			}
		}
	//	MyAssert(k==L);
		MD(printf("k:%d\n",k);)

		int ret = 0;
		for (int j=0; j<D; j++){
			int k=0;
			while (k<L && p[k][ name[j][k]-'a']) k++;
			if (k==L) {
				ret++;
				MD(cout<<name[j]<<endl;)
			}
		}
		printf("Case #%d: %d\n",i+1,ret);
	}
	return 0;
}
