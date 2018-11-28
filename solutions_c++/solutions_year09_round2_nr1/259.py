#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;



int L,A;

char bf[1000];
char tr[1000000];
int sLen=0;

set<string> a[105];

bool Input(){
	scanf("%d",&L);
	int i,j,k;
	gets(bf);
	tr[0]=0;
	for(i=0;i<L;++i){
		gets(bf);
		strcat(tr," ");
		strcat(tr,bf);
	}
	sLen=strlen(tr);

	scanf("%d",&A);
	for(i=0;i<A;++i){
		a[i].clear();
		int fn;
		scanf("%s%d",&bf,&fn);
		while(fn--){
			scanf("%s",&bf);
			a[i].insert(string(bf));
		}
	}
    return 1;
}

double Proc(int s,int t, set<string>& ft){
	double val;
	sscanf(tr+s+1,"%lf",&val);
	int i,j,k;
	int p1=-1,p2=-1;
	for(k=0,i=s+1;i<=t;++i){
		if(tr[i]=='('){
			++k;
			if(k==1){
				if(p1<0) p1=i;
				else{
					p2=i;
					break;
				}
			}
		}else if(tr[i]==')') --k;
	}
	if(p1<0){
		return val;
	}
	char ts[1000];
	sscanf(tr+s+1,"%lf%s",&val,&ts);
	if(ft.find(string(ts))!=ft.end()){
		s=p1;
		t=p2-1;
		while(t>=s&&tr[t]!=')'){
			--t;
		}
	}else{
		s=p2;
		t=t-1;
		while(t>=s&&tr[t]!=')'){
			--t;
		}
	}
	return val*Proc(s,t,ft);
}


void Solve(int cn){
	printf("Case #%d:\n",cn);
	int i;
	for(i=0;i<A;++i){
		int p1,p2;
		p1=0,p2=sLen-1;
		while(p1<sLen&&tr[p1]!='(') ++p1;
		while(p2>=0&&tr[p2]!=')') --p2;
		printf("%.7lf\n",Proc(p1,p2,a[i]));
	}
    return;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("ans.out","w",stdout);
	int tn;
	int id=0;
	scanf("%d",&tn);
	while(tn--){
		Input();
        Solve(++id);
    }
    return 0;
}
