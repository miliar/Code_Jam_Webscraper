//Fruit of Light
//FoL CC
//pineapple strawberry
#include <cstdio>
#include <stack>
#include <vector>
using namespace std;

char C[30][30];
bool T[30][30];
bool B[30];

void over(vector<char> A)
{
	for(int i=0; i<29; i++) B[i]=false;
	for(int i=0; i<A.size(); i++) B[A[i]-'A']=true;
}

int main()
{
	int t1;
	scanf("%d ",&t1);
	for(int i1=0; i1<t1; i1++)
	{
		for(int i=0; i<29; i++)
			for(int j=0; j<29; j++) C[i][j]='!';
		for(int i=0; i<29; i++)
			for(int j=0; j<29; j++) T[i][j]=false;
		int n;
		scanf("%d ",&n);
		for(int i=0; i<n; i++){
		char c1=getchar(),c2=getchar(),c3=getchar(); getchar();
		C[c1-'A'][c2-'A']=c3; C[c2-'A'][c1-'A']=c3;}
		scanf("%d ",&n);
		for(int i=0; i<n; i++){
		char c1=getchar(),c2=getchar(); getchar(); T[c1-'A'][c2-'A']=true; T[c2-'A'][c1-'A']=true;}
		for(int i=0; i<29; i++) B[i]=false;
		scanf("%d ",&n);
		vector<char> S;
		for(int i=0; i<n; i++)
		{
			char c=getchar();
			bool t=false;
			for(int i=0; i<26; i++) if(T[c-'A'][i] && B[i]) t=true;
			if(S.empty()) {S.push_back(c); B[c-'A']=true;}
			else if(C[S[S.size()-1]-'A'][c-'A']!='!') {char p=C[S[S.size()-1]-'A'][c-'A']; S.pop_back(); S.push_back(p); over(S);}
			else if(t) {while(!S.empty()) S.pop_back(); over(S);}
			else {S.push_back(c); B[c-'A']=true;}
			//printf("%d\n",S.size());
		}
		printf("Case #%d: [",i1+1);
		for(int i=0; i<S.size(); i++)
		{
			printf("%c",S[i]);
			if(i!=S.size()-1) printf(", ");
		}
		printf("]\n");
	}
return 0;
}