#include <cstdio>
#include <iostream>
#include <cstring>
#include <stack>
using namespace std;
int way[444][444];
int ada[444];
int mati[444][444];
int T,N;
int tc=1;
char a[9999];

int main() {
	freopen("B.txt","w",stdout);
	freopen("Bin.txt","r",stdin);
	
scanf("%d",&T);
while (T--){
	memset(ada,0,sizeof(ada));
	memset(way,0,sizeof(way));
	memset(mati,0,sizeof(mati));
	scanf("%d",&N);
	for (int i=0;i<N;i++){
		scanf("%s",a);
		way[(int)a[0]][(int)a[1]] = (int)a[2];
		way[(int)a[1]][(int)a[0]] = (int)a[2];
		}
	scanf("%d",&N);
	for (int i=0;i<N;i++){
		scanf("%s",a);
		mati[a[0]][a[1]]=1;
		mati[a[1]][a[0]]=1;
		}
	scanf("%d",&N);
	scanf("%s",a);
	stack<int> kul ;
	while (kul.size()) kul.pop();
	
	for (int i=0;i<N;i++){
			kul.push(a[i]);
			ada[a[i]]++;
			bool gerak = 1;
			while (gerak && kul.size()>1) {
				gerak = 0;
				char A = kul.top();
				kul.pop();
				char B = kul.top();
				if (way[A][B]!=0) {
					gerak =1;
					kul.pop();
					kul.push(way[A][B]);
					ada[A]--; ada[B]--; ada[way[A][B]]++;
					}
				else kul.push(A);
				}
		char A = a[i];
		for (int j='A';j<'Z';j++){
				if (mati[A][j] && ada[j] && ada[A]) {
					while (kul.size()) {ada[kul.top()]--; kul.pop();}
					break;
					}
			}
		
		}
		stack<int> kul2;
		while (kul.size()) {kul2.push(kul.top()); kul.pop();}
	printf("Case #%d: [",tc++);
	if (kul2.size()) printf("%c",kul2.top());
	if (kul2.size())	kul2.pop();
	while (kul2.size()) {
		printf(", %c",kul2.top());
		kul2.pop();
		}
	printf("]\n");
}
}
