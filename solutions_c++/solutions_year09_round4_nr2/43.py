
#include <iostream>
#include <cstring>
#include <deque>
#include <queue>
#include <vector>
#include <cstdio>
#include <stack>
#include <cmath>
#include <map>
#include <algorithm>
using namespace std;

const int dy[2]={1,-1};

typedef pair<int,int> pii;
#define f first
#define s second

struct st{
	int x,y;
	int now,next;
};

int main(){
	int nn;scanf("%d",&nn);
	while(nn--){
		int r,c,f;scanf("%d%d%d",&r,&c,&f);

		char buf[r][c+2];
		for(int i=0;i<r;i++)scanf("%s",buf[i]);

		int orig[r];
		for(int i=0;i<r;i++){
			orig[i]=0;
			for(int k=0;k<c;k++)if(buf[i][k]=='#')orig[i]|=(1<<k);
		}

		int ans=-1;

		char seen[r][c][1<<c][1<<c];memset(seen,0,sizeof(seen));
		int step=0;
		queue<st> qnow,qnext;
		qnext.push((st){0,0,orig[0],orig[1]});//seen[0][0][orig[0]][orig[1]]=1;
		while(qnext.size()){
			swap(qnow,qnext);
			while(qnow.size()){
				int x=qnow.front().x;
				int y=qnow.front().y;
				int now=qnow.front().now;
				int next=qnow.front().next;qnow.pop();
				
				char &see=seen[x][y][now][next];
				if(see)continue;
				see=1;

				//cout<<"x"<<x<<" y"<<y<<" now"<<hex<<now<<" next"<<next<<dec<<endl;

				if((next&(1<<y))==0){
					//cout<<"fall"<<endl;

					int cnt=0;
					while((next&(1<<y))==0){
						cnt++;
						if(f<cnt)break;
						if(x+cnt==r-1){ans=step;goto output;}
						now=next;next=orig[x+cnt+1];
					}
					if(cnt<=f){
						if(seen[x+cnt][y][now][next]==0){
							//seen[x+cnt][y][now][next]=1;
							qnow.push((st){x+cnt,y,now,next});
						}
					}

					continue;
				}

				for(int i=0;i<2;i++){
					int yy=y+dy[i];
					if(yy<0 || c<=yy)continue;
					if(now&(1<<yy))continue;
					if(seen[x][yy][now][next]==0){
						//seen[x][yy][now][next]=1;
						qnow.push((st){x,yy,now,next});
					}
				}

				for(int i=0;i<2;i++){
					int yy=y+dy[i];
					if(yy<0 || c<=yy)continue;
					if(now&(1<<yy) || (next&(1<<yy))==0)continue;
					if(seen[x][y][now][next^(1<<yy)]==0){
						qnext.push((st){x,y,now,next^(1<<yy)});
					}
				}

			}
			step++;
		}
output:

		static int npr=1;
		if(ans!=-1){
			printf("Case #%d: Yes %d\n",npr++,ans);
		}else{
			printf("Case #%d: No\n",npr++);
		}
	}

	return 0;
}
