#include<string>
#include<map>
#include<vector>
#include<iostream>
#include<queue>
using namespace std;
	int mp[101][101];
	int shed[101][101];
	int t,r,c;
	int dr[]={-1,0,0,1};
	int dc[]={0,-1,1,0};
	struct point
	{
		point(int mr,int mc){pr=mr;pc=mc;}
		int pr;
		int pc;
	};
bool checkmin(int mr,int mc,int cr,int cc){
	int minone=100000;
	int tr=-1,tc=-1;
	bool tag=true;
	for(int i=0;i<4;i++)
	{
			 int tmpr=cr+dr[i];int tmpc=cc+dc[i];
			 if(tmpr>=0&&tmpr<r&&tmpc>=0&&tmpc<c&&mp[tmpr][tmpc]<minone){
				tr=tmpr;tc=tmpc;minone=mp[tmpr][tmpc];
			 }
	}
	if(tr==mr&&tc==mc)return true;
	return false;
}
void floodfill(int mr,int mc,int number){
	queue<point> q;
	q.push(point(mr,mc));
	while(!q.empty()){
		point pt=q.front();
		q.pop();
		for(int i=0;i<4;i++){
			int tmpr=pt.pr+dr[i];int tmpc=pt.pc+dc[i];
			if(tmpr>=0&&tmpr<r&&tmpc>=0&&tmpc<c&&shed[tmpr][tmpc]==0&&mp[tmpr][tmpc]>mp[pt.pr][pt.pc]&&checkmin(pt.pr,pt.pc,tmpr,tmpc)) 
			{
				shed[tmpr][tmpc]=number;
				q.push(point(tmpr,tmpc));
			}
		}
	}
}
int main()
{

	
	int i,j,k;
    int mr,mc;
	int minone;
	int number;
	freopen("c:\\B-small-attempt1.in","r",stdin);
	freopen("c:\\output.txt","w",stdout);
	cin>>t;
	for(int testcase=0;testcase<t;testcase++){
		cin>>r>>c;
		printf("Case #%d:\n",testcase+1);
		number=1;
		memset(shed,0,sizeof(shed));
		for(i=0;i<r;i++)
			for(j=0;j<c;j++)
				cin>>mp[i][j];
		while(true){
			minone=100000;
			for(i=0;i<r;i++)
				for(j=0;j<c;j++){
					if(shed[i][j]==0&&mp[i][j]<minone){
						minone=mp[i][j];mr=i;mc=j;
					}
				}
			if(minone==100000)break;
			shed[mr][mc]=number;
			floodfill(mr,mc,number);
			number++;
		}
		map<int,char> comp; 
		number=0;
		for(i=0;i<r;i++)
			for(j=0;j<c;j++)
			{
				if(comp.find(shed[i][j])==comp.end()){
					comp[shed[i][j]]='a'+number;
					number++;
				}
				cout<<comp[shed[i][j]];
				if(j==c-1)printf("\n");
				else printf(" ");
			}
		
	}
	return 0;
}