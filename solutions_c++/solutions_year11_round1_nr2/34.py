#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
char alls[10100][12];
int tmt;
struct XD{
    char wo[12];
    int id;
    int len;
    int pos[30];
    void input(int ii){
	id=ii;
	scanf("%s",wo);
	strcpy(alls[ii],wo);
	int i;
	for(i=0;i<26;i++)pos[i]=0;
	for(i=0;wo[i];i++){
	    pos[wo[i]-'a']|=(1<<i);
	}
	len=i;
    }
    bool operator<(const XD& b)const{
	return pos[tmt]<b.pos[tmt];
    }
};
vector<XD> in[12];
int n;
char alp[30];
struct XDD{
    int po,id;
    XDD(int pp=-1,int ii=-1):po(pp),id(ii){}
    bool operator>(const XDD& b)const{
	return (po>b.po)||(po==b.po&&id<b.id);
    }
};
XDD trys(vector<XD> wos,int np){
    if(wos.size()==0)return XDD(-1,-1);
    if(wos.size()==1)return XDD(0,wos[0].id);
    int i,j;
    int nc=alp[np]-'a';
    for(i=0;i<wos.size();i++){
	if(wos[i].pos[nc])break;
    }
    if(i==wos.size())return trys(wos,np+1);
    tmt=nc;
    sort(wos.begin(),wos.end());
    XDD ans(-1,-1);
    for(i=0;i<wos.size();i=j){
	vector<XD> tmp;
	for(j=i;j<wos.size();j++){
	    if(wos[j].pos[nc]!=wos[i].pos[nc])break;
	    tmp.push_back(wos[j]);
	}
	XDD ret=trys(tmp,np+1);
	if(wos[i].pos[nc]==0)ret.po++;
	if(ret>ans)ans=ret;
    }
    return ans;
}
inline void solve(){
    int i;
    scanf("%s",alp);
    XDD ans(-1,-1);
    for(i=1;i<=10;i++){
	fprintf(stderr,"<%d>",i);
	XDD ret=trys(in[i],0);
	if(ret>ans)ans=ret;
    }
    printf(" %s",alls[ans.id]);
}
int main(){
    int t,i,cas=1;
    scanf("%d",&t);
    while(t--){
	int m;
	scanf("%d%d",&n,&m);
	for(i=0;i<12;i++)in[i].clear();
	for(i=0;i<n;i++){
	    XD tmp;
	    tmp.input(i);
	    in[tmp.len].push_back(tmp);
	}
	fprintf(stderr,"%d\t",cas);
	printf("Case #%d:",cas++);
	while(m--)solve();
	puts("");
    }
}
