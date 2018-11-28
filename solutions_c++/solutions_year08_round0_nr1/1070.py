#include <stdio.h>
#include <map>
#include <string>
using namespace std;

int main()
{
	int N;
	map<string,int>mymap;
	int i,j,k,t,result;
	int unum,qnum;
	bool flag[300];
	char ch[300];

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&N);
	for(i=1; i<=N; i++){
		scanf("%d",&unum);
		result=0;
		gets(ch);
		for(j=0; j<unum; j++){
			gets(ch);
			mymap[ch]=j;
			flag[j]=false;
		}
		t=0;
		scanf("%d",&qnum);
		gets(ch);
		for(j=0; j<qnum; j++){
			gets(ch);
			if(flag[mymap[ch]]==false){
				flag[mymap[ch]]=true;
				t++;
				if(t==unum){
					result++;
					t=1;
					for(k=0; k<unum; k++)
						flag[k]=false;
					flag[mymap[ch]]=true;
				}
			}
		}
		printf("Case #%d: %d\n",i,result);
	}
	return 0;
}
