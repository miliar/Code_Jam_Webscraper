#include <stdio.h>
#include <string.h>
#include <map>
#include <string>

using namespace std;


int N,S,Q;
map<string, int> ID;

char buf[10001];
bool mark[1010];

int main()
{

   scanf(" %d ",&N);
   for(int t=0; t<N;++t)
   {
	//printf("Teste: %d\n",t);
	int id = 0;
	int cnt = 0;
	int switches = 0;
	ID.clear();
	memset(mark,false,sizeof(mark));
	scanf("%d ",&S);
	for(int i=0; i<S; ++i) {
		gets(buf);
		ID[string(buf)] = id++;
	}
	scanf("%d ",&Q);
	for(int i=0; i<Q; ++i)
	{
	    gets(buf);
	    int query = ID[string(buf)];
	    //printf("query=%d buf=%s\n",query,buf);
	    if(!mark[query])
	    {
		mark[query] = true;
		cnt++;
		if(cnt == S){
			for(int j=0; j<S; ++j) if(j!=query) mark[j] = false;
			switches++;
			cnt = 1;
		} 
		
	    }

	}
	printf("Case #%d: %d\n",t+1,switches);
		

   }

   return 0;
}
