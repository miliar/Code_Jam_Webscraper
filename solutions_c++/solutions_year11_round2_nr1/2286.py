#include<iostream>
using namespace std;
char s[105][105];
double wp1[105],wp2[105],owp[105],oowp[105];
int main(){
	int txt,cas=1,i,j,n,m,cnt,acnt;
	double tmp;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("2.txt","w",stdout);
	cin>>txt;
	while(txt--){
		printf("Case #%d:\n",cas++);
		memset(wp1,0,sizeof(wp1));memset(wp2,0,sizeof(wp2));memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		scanf("%d",&n);
		m=n;
		for(i=0;i<n;++i){
			scanf("%s",s[i]);
			acnt=0;
			cnt=0;
			for(j=0;j<m;++j){
				if(s[i][j]=='1')
					acnt++;
				if(s[i][j]!='.')
					cnt++;
			}
			wp1[i]=acnt*1.0;
			wp2[i]=cnt*1.0;
		}
		int l;
		for(i=0;i<n;++i){
			tmp=0;
			l=0;
			for(j=0;j<m;++j){
				if(s[i][j]!='.')
				{
					acnt=wp1[j];cnt=wp2[j];
					if(s[j][i]=='1')
						acnt--,cnt--;
					else cnt--;
					if(cnt!=0)
					tmp+=acnt*1.0/cnt;
					l++;
				}
			}
			owp[i]=tmp/l;
		}
		for(i=0;i<n;++i){
			cnt=0;
			for(j=0;j<m;++j)
				if(s[i][j]!='.')
					oowp[i]+=owp[j],cnt++;
				oowp[i]/=(cnt*1.0);
		}
		for(i=0;i<n;++i){
			printf("%.12lf\n",0.25 *wp1[i]/wp2[i] + 0.50 * owp[i] + 0.25 *oowp[i]);
		}
	}
	return 0;
}