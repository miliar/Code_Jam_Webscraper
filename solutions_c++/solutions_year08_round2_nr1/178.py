#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream> 
#include <cmath>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair
#define PII pair<int,int> 
#define A first
#define B second
#define PIII pair<int,PII> 

#define I(x,y) x <y> :: iterator 
#define set(a,c) memset(a,c,sizeof(a))

#define REP(i,n) for(int i=0;i<n;i++)

typedef unsigned long long LLU;
typedef long long LL;
typedef long double LD;
int n;
LLU r[3][3];
LLU A,B,C,D,x,y,M,i1,i2,j2,i3,j3;
LLU answer;
int main()
{
	int j1;
	int KASES;
	scanf("%d",&KASES);
	for(int kases=0;kases<KASES;kases++)
	{
		printf("Case #%d: ",kases+1);
		cin>>n>>A>>B>>C>>D>>x>>y>>M;
//		scanf("%d %d %d %d %d %d %d %d",&n,&A,&B,&C,&D,&x,&y,&M);
		for(int i=0;i<3;i++) for(int j=0;j<3;j++) r[i][j]=0;
		answer = 0;
		r[x%3][y%3]++;
		for(int i=1;i<n;i++){
			x = (A*x + B )%M;
			y = (C*y+D)%M;//printf("\n %d %d",x,y);
			r[x%3][y%3]++;
		}
	//	printf("\n");
	
	/*	for(int i1=0;i1<3;i1++)
			for(int j1=0;j1<3;j1++)
				for(int i2=0;i2<3;i2++)
					for(int j2=0;j2<3;j2++)
					{
						if(i1==i2 && j1==j2)
							continue;
						i3 = (3-(i1+i2)%3)%3;
						j3 = (3-(j1+j2)%3)%3;
						if(i1*3+j1 > i2 *3 + j2)
							continue;
						if(i1*3+j1 > i3 * 3 +j3)
							continue;
						if(i2*3+j2 > i3*3 + j3)
							continue;
	//					if(r[i1][j1]*r[i2][j2]*r[i3][j3])printf("%d %d %d %d %d %d \n",i1,j1,i2,j2,i3,j3);
						
						answer += r[i1][j1]*r[i2][j2]*r[i3][j3];
					}
				*/
	for(int f1=0;f1<7;f1++)
		for(int s=f1+1;s<8;s++)
		{
			i1 = f1/3;
			j1 = f1%3;
			i2 = s/3;
			j2 = s%3;
			i3 = (3-(i1+i2)%3)%3;
			j3 =(3 -(j1+j2)%3)%3;
						//if(r[i1][j1]*r[i2][j2]*r[i3][j3])printf("%d %d %d %d %d %d \n",i1,j1,i2,j2,i3,j3);
						
			if(i3*3+j3>s){
	//		printf("%d %d %d %d %d %d \n",i1,j1,i2,j2,i3,j3);
				answer+=(r[i1][j1]*r[i2][j2]*r[i3][j3]);
		}
		}
		for(int i=0;i<3;i++)
			for(int j=0;j<3;j++)
			
				answer += r[i][j]*(r[i][j]-1)*(r[i][j]-2)/6;
		//printf("%d\n",answer);
		cout<<answer<<endl;
	}
}

