#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define MaxN 100
struct BUTTON{
	char robot;
	int btn;
}button[MaxN+5];
struct ROBOT{
	int pos;
	int aim;
	int btn[MaxN+5];
	int size;
	void init(){
		size=0;
		pos=1;
		aim=0;
	}
	void add(int Btn){
		btn[size++]=Btn;
	}
	void makestep(int step){
		if (aim==size) return;
		bool flag;
		if (pos<btn[aim]){
			flag=1;
		}else{
			flag=0;
		}
		while (pos!=btn[aim]){
			if (step==0) break;
			if (flag) pos++;
			else pos--;
			step--;
		}
	}
	void push(){
		aim++;
	}
}blue,orange;
int n;
void init(){
	int i;
	char s[5];
	blue.init();
	orange.init();
	scanf("%d",&n);
	for (i=0;i<n;i++){
		scanf("%s",&s);
		button[i].robot=s[0];
		scanf("%d",&button[i].btn);
		if (button[i].robot=='B'){
			blue.add(button[i].btn);
		}else{
			orange.add(button[i].btn);
		}
	}
}
void solve(){
	int i,tmp;
	int ans=0;
	for (i=0;i<n;i++){
		if (button[i].robot=='B'){
			tmp=button[i].btn-blue.pos;
			if (tmp<0) tmp=-tmp;
			ans+=tmp+1;
			blue.makestep(tmp);
			blue.push();
			orange.makestep(tmp+1);
		}else{
			tmp=button[i].btn-orange.pos;
			if (tmp<0) tmp=-tmp;
			ans+=tmp+1;
			orange.makestep(tmp);
			orange.push();
			blue.makestep(tmp+1);
		}
	}
	printf("%d\n",ans);
}
int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
	int t,i;
	scanf("%d",&t);
    for (i=1;i<=t;i++){
		printf("Case #%d: ",i);
        init();
		solve();
    }
    return 0;
}