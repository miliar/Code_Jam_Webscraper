#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;
int O[101],oi,ois;
int B[101],bi,bis;
queue <int > which;
int main()
{
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		ois=1;bis=1;
		oi=0;bi=0;
		int N,z;
		char w=' ';
		scanf("%d",&N); 
		for(int i=0;i<N;i++)
		{scanf(" %c %d",&w,&z);
		if(w=='O'){O[oi++]=z;which.push(0);}
		if(w=='B'){B[bi++]=z;which.push(1);}
		}
		int i=0,j=0;
		int t=0;
		while(i<oi && j<bi)
		{
			if(!which.front()){
				which.pop();
				int ile = abs(O[i]-ois)+1;
				if(B[j]==bis);
				else if(B[j]>bis)bis=min(B[j],bis+ile);
				else bis=max(B[j],bis-ile);
				t+=ile;
				ois=O[i];i++;
			}
			else if(which.front()){
				which.pop();
				int ile = abs(B[j]-bis)+1;
				if(O[i]==ois);
				else if(O[i]>ois)ois=min(O[i],ois+ile);
				else ois=max(O[i],ois-ile);
				t+=ile;
				bis=B[j];j++;
			}
		}
		while(i<oi)
		{
			t+=abs(O[i]-ois)+1;
		ois=O[i];i++;
	}
		while(j<bi)
		{
			t+=abs(B[j]-bis)+1;
			bis=B[j];j++;
}
		printf("Case #%d: %d\n",cas,t);
		while(!which.empty())which.pop();
	}
}

