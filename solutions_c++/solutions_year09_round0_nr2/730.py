#include<iostream>
#include<string>
#include<cstring>
#include<map>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<sstream>
#include<set>
#include<stack>
#define vi vector<int>
#define vvi vector<vector<int> > 
#define vpi vector<pair<int,int> >
#define vvpi vector<vector<pair<int,int> > > 
#define pi pair<int,int> 
#define ll long long
#define boolean bool
using namespace std;
int nums[101][101];
int memo[101][101];
char outs[101][101];
int dx[]={0,-1,1,0};
int dy[]={-1,0,0,1};
main()
{
	int t,tc=1;
	scanf("%d",&t);
	while(t--!=0){
		int h,w;
		scanf("%d%d",&h,&w);
		for(int i=0;i<h;i++) for(int j=0;j<w;j++) scanf("%d",nums[i]+j);
		memset(memo,0,sizeof(memo));
		int cno=1;
		stack<int> qu;
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				if(memo[i][j]>0)continue;
				qu.push(j);
				qu.push(i);
				int alot=0;
				while(true){
					int gi=qu.top();qu.pop();int gj=qu.top();
					int ci=-1,cj=-1;
					for(int t=0;t<4;t++){
						int y=gi+dy[t];
						int x=gj+dx[t];
						if(y<0||y>=h||x<0||x>=w||nums[y][x]>=nums[gi][gj])continue;
						if(ci==-1||nums[y][x]<nums[ci][cj]){
							//if(i==1&&j==1)cout<<nums[y][x]<<endl;
							ci=y;cj=x;
						}
					}
					qu.push(gi);
					if(ci==-1){break;}
					if(memo[ci][cj]>0){
						alot=memo[ci][cj];
						break;
					}
					qu.push(cj);
					qu.push(ci);
				}
				if(alot==0) alot=cno++;
				while(!qu.empty()){
					int gi=qu.top();qu.pop();int gj=qu.top();qu.pop();
					outs[gi][gj]=(alot-1+'a');
					memo[gi][gj]=alot;
				}
			}
		}
		printf("Case #%d:\n",(tc++));
		for(int i=0;i<h;i++){
			printf("%c",outs[i][0]);
			for(int j=1;j<w;j++){
				printf(" %c",outs[i][j]);
			}
			printf("\n");
		}
	}
}