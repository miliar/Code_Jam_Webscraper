#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<limits>
#include<set>

using namespace std;

int main()
{
	int N,s,A[100],d;
	int t=1;
	scanf("%d",&t);
	for(int k=0;k<t;++k)
	{
		scanf("%d%d%d",&N,&s,&d);
		for(int i=0;i<N;++i)
			scanf("%d",&A[i]);
		int l_score=0,u_score=0;
		for(int i=0;i<N;++i)
		{
			int a,b,c=A[i]/3;
			if(A[i]%3==0){a=c;b=c+1;}
			else if(A[i]%3==1){a=c+1;b=c+1;}
			else {a=c+1;b=c+2;}
			if(A[i]==0){a=0;b=0;}
			if(a>10)a=10;
			if(b>10)b=10;
			if(a>=d) l_score++;
			else if(b>=d) u_score++;
//			cout<<a<<"  "<<b<<endl;
		}
		if(u_score>s)u_score=s;
		printf("Case #%d: %d\n",k+1,l_score+u_score);

	}
	return 0;
}

