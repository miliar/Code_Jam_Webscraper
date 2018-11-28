# include <cstdio>
# include <iostream>
# include <algorithm>
# include <vector>
# include <cstring>
# include <cctype>
# include <set>
# include <map>
# include <cmath>
# include <queue>
# include <string>

using namespace std;

char conv[128]="";

char inp[1001];
set<int> vatt;

int in[128],out[128],twice[128];
char good[4000][2];

int main()
{
	conv['o']='0';
	conv['i']='1';
	conv['e']='3';
	conv['a']='4';
	conv['s']='5';
	conv['t']='7';
	conv['b']='8';
	conv['g']='9';
	
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d:",t);
		
		int N;
		scanf("%d",&N);
		
		scanf("%s",inp);
		int L=strlen(inp);
		
		vatt.clear();
		for(int i=0;i<L-1;i++)
		{
			vatt.insert(inp[i]*128+inp[i+1]);
			if(conv[inp[i]])vatt.insert(conv[inp[i]]*128+inp[i+1]);
			if(conv[inp[i+1]])vatt.insert(inp[i]*128+conv[inp[i+1]]);
			if(conv[inp[i+1]]&&conv[inp[i]])vatt.insert(conv[inp[i]]*128+conv[inp[i+1]]);
		}
		
		for(int i=0;i<128;i++)
			in[i]=out[i]=twice[i]=0;
		
		set<int>::iterator sit;int cnt=0;
		for(sit=vatt.begin();sit!=vatt.end();sit++)
		{
			int i=*sit;
			char a=i/128,b=i%128;
			good[cnt][0]=a;good[cnt++][1]=b;
			in[a]++,out[b]++;
			if(a==b)twice[a]=1;
		}
		
		int ret=cnt<<1;bool flag=true;
		for(int i=0;i<128;i++)
		{
			if(in[i]!=1||out[i]==1||twice[i]!=1)ret-=min(in[i],out[i]);
			if(in[i]!=out[i]||(in[i]==0&&out[i]==0&&twice[i]==1))flag=false;
		}
		if(flag)ret++;
		printf(" %d\n",ret);
	}
	return 0;
}
