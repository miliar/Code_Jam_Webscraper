#include<cstdio>
#include<stack>
#define MN 102
#define MC 'Z'+1
using namespace std;
const char b[]="QWERASDF";
int test,ntest;
int n,i,j,a,t[MC];
char co[MC][MC],op[MC][MC],s[MN],c;
stack<char> l,ll;

int main()
{
	scanf("%d",&ntest);
	for(test=1; test<=ntest; ++test)
	{
		for(i=0; i<MC; ++i)
			for(j=0; j<MC; ++j)
				co[i][j]=op[i][j]=0;
		for(i=0; i<MC; ++i) t[i]=0;
		scanf("%d",&n);        // Combiny
		for(i=0; i<n; ++i)
		{
			scanf("%s",s);
			co[s[0]][s[1]]=co[s[1]][s[0]]=s[2];
		}
		scanf("%d",&n);        // Opposy
		for(i=0; i<n; ++i)
		{
			scanf("%s",s);
			op[s[0]][s[1]]=op[s[1]][s[0]]=1;
		}
		scanf("%d%s",&n,s);        // Invoki
		for(i=0; i<n; ++i)
		{
			if(!l.empty() && co[l.top()][s[i]]) { // kombinujemy
				--t[l.top()];
				l.top()=co[l.top()][s[i]];
				++t[l.top()];
				continue;
			} 
			for(j=0; j<8; ++j) // oposujemy
				if(t[b[j]] && op[s[i]][b[j]])
				{
					while(!l.empty()) l.pop();
					for(c='A'; c<='Z'; ++c) t[c]=0;
					j=-5;
					break;
				}
			if(j<0) continue;
			// dodajemy
			l.push(s[i]);
			++t[s[i]];
		}
		while(!l.empty()) 
		{
			ll.push(l.top());
			l.pop();
		}
		printf("Case #%d: [",test);
		if(!ll.empty()) { 
			printf("%c",ll.top());
			ll.pop();
		}
		while(!ll.empty()) {
			printf(", %c",ll.top());
			ll.pop();
		}
		printf("]\n");
	}
}

