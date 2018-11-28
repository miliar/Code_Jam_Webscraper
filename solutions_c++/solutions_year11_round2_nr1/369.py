#include<cstdio>
#include<cstring>
using namespace std;

char maze[105][105];
double wp[105];
double owp[105];
double oowp[105];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("Al.out","w",stdout);
	
	int t,cas=0;
	scanf("%d",&t);
	while(t--){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%s",maze[i]);
			int win=0,all=0;
			for(int j=0;j<n;j++){
				if(maze[i][j]!='.') all++;
				if(maze[i][j]=='1') win++;
			}
			wp[i]=(double)win/all;
		}
		
		for(int i=0;i<n;i++){
			double tall=0;
			int tcnt=0;
			for(int j=0;j<n;j++){
				if(maze[j][i]=='.') continue;
				tcnt++;
				int all=0,cnt=0;
				for(int k=0;k<n;k++){
					if(maze[j][k]=='.') continue;
					if(k==i) continue;
					all++;
					if(maze[j][k]=='1') cnt++;
				}
				tall+=(double)cnt/all;
			}
			owp[i]=tall/tcnt;
		}
		
		for(int i=0;i<n;i++){
			double all=0;
			int cnt=0;
			for(int j=0;j<n;j++){
				if(maze[i][j]!='.'){
					all+=owp[j];
					cnt++;
				}
			}
			oowp[i]=all/cnt;
		}
		
		printf("Case #%d:\n",++cas);
		for(int i=0;i<n;i++){
		//	printf("= %lf %lf %lf\n",wp[i],owp[i],oowp[i]);
			printf("%.12lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}
	
	fclose(stdin);
	fclose(stdout);
}