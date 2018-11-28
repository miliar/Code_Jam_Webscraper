
#include<stdio.h> 
#include<math.h> 
#include<string.h> 
#include<stdlib.h> 
#include<iostream>
#include<vector>
#include<list>
#include<algorithm>

using namespace std;

struct Node{
	int b,e,f;
};

bool cmp(Node a,Node b)
{
	return a.b<b.b;
}

int main() 
{ 
	vector<Node> train;
	int n,t,na,nb,s,h,m,i;

	scanf("%d",&n);
	for (int ri=1;ri<=n;++ri)
	{
		train.clear();
		scanf("%d%d%d",&t,&na,&nb);
		s=na+nb;
		for ( i=0;i<na;i++){
			Node plat;
			scanf("%d:%d",&h,&m);
			plat.b=h*60+m;
			scanf("%d:%d",&h,&m);
			plat.e=h*60+m;
			plat.f=0;
			train.push_back(plat);
		}
		for ( i=na;i<s;i++){
				
			Node plat;
			scanf("%d:%d",&h,&m);
			plat.b=h*60+m;
			scanf("%d:%d",&h,&m);
			plat.e=h*60+m;
			plat.f=1;
			train.push_back(plat);
		}
		sort(train.begin(),train.end(),cmp);
		int m[2],num[2];
		m[0]=m[1]=0;
		num[0]=num[1]=0;
		list<int> l[2];
		
		for ( i=0;i<s;++i){
			
			int now=train[i].f;
		//	l[now].sort();
			for (list<int>::iterator t1=l[now].begin();t1!=l[now].end();++t1)
				if ((*t1)<=train[i].b)
				{
					++num[now];
					*t1=2000;
				}
			
			if (num[now]==0)
				m[now]++;
			else num[now]--;
			int next=(now+1)%2;
			l[next].push_back(train[i].e+t);
		}
		printf("Case #%d: %d %d\n",ri,m[0],m[1]);
			
	}
	
	
			
			

//	system("PAUSE");
	return 0;
	
} 


