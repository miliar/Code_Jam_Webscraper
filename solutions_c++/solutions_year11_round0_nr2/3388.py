#include <cstdio>
#include <vector>

using namespace std;

int n;
int is[256];
vector<int>with[256];
vector<int>to[256];
vector<int>result;
vector<int>opp[256];


void add(char a)
{
	for(int i=0; i<with[a].size(); i++){
		if(result.size()> 0 && with[a][i] == result[result.size()-1]){
			is[with[a][i]]--;
			result[result.size()-1] = to[a][i];
			is[to[a][i]]++;
			return;
		}
	}
	for(int i=0; i<opp[a].size(); i++){
		if(is[opp[a][i]]>0){
			for(int j=0; j<256; j++)
				is[j]=0;
			result.resize(0);
			return;
		}
	}
	is[a]++;
	result.push_back(a);
}

void test()
{
	for(int i=0; i<256; i++){
		is[i]=0;
		with[i].resize(0);
		to[i].resize(0);
		opp[i].resize(0);
	}
	result.resize(0);
	
	int m;
	char a,b,c;
	scanf("%d ", &m);
	while(m){
		scanf("%c%c%c ", &a, &b, &c);
		with[a].push_back(b);
		with[b].push_back(a);
		to[a].push_back(c);
		to[b].push_back(c);
		m--;
	}
	scanf("%d ", &m);
	while(m){
		scanf("%c%c ", &a, &b);
		opp[a].push_back(b);
		opp[b].push_back(a);
		m--;
	}
	scanf("%d ", &m);
	//printf("A\n");
	while(m){
		scanf("%c", &a);
		//printf("B\n");
		add(a);
		m--;
	}
	

	
}
int main()
{
	scanf("%d", &n);
	for(int i=1; i<=n; i++){
		printf("Case #%d: ", i);
		test();
		printf("[");
		for(int j=0; j<result.size(); j++){
			if(j!=0)
				printf(", ");
			printf("%c", result[j]);
		}
		printf("]\n");
	}
	return 0;
}