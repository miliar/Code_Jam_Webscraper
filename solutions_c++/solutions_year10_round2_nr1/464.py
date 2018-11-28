#include <cstdio>
#include <cstring>
#include <cstdlib>

const int N=101;

char already[300*N][N];
char need[N][N];

int main(){
	int ic,cas,n,m;
	scanf("%d",&cas);
	for(ic=1;ic<=cas;ic++){
		scanf("%d%d",&n,&m);
		int i;
		for(i=0;i<n;i++) scanf("%s",already[i]);
		for(i=0;i<m;i++) scanf("%s",need[i]);
		int ans=0;
		for(i=0;i<m;i++){
			int j,k;
			int maxc=1;
			int li,lj;
			li=strlen(need[i]);
			int cc;
			for(j=0;j<n;j++){
				lj=strlen(already[j]);
				cc=0;
				for(k=0;k<li&&k<lj;k++){
					if(already[j][k]!=need[i][k]) break;
					if(already[j][k]=='/') cc++;
				}
				if((already[j][k]==0&&need[i][k]==0)||(already[j][k]==0&&need[i][k]=='/')||(already[j][k]=='/'&&need[i][k]==0)) cc++;
				if(cc>maxc) maxc=cc;
			}
			int cs=0;
			for(k=0;k<li;k++){
				if(need[i][k]=='/') cs++;
			}
			ans+=cs-maxc+1;
			//printf("ans=%d,cs=%d,maxc=%d\n",ans,cs,maxc);
			if(cs-maxc+1>0) strcpy(already[n++],need[i]);
			cc=0;
			for(k=0;k<li;k++){
				if(need[i][k]=='/'){
					cc++;
					if(cc>maxc){
						char tmp[N];
						for(j=0;j<k;j++) tmp[j]=need[i][j];
						tmp[j]=0;
						strcpy(already[n++],tmp);
					}
				}
			}
			//for(j=0;j<n;j++) printf("%s\n",already[j]);
		}
		printf("Case #%d: %d\n",ic,ans);
	}
	return 0;
}
