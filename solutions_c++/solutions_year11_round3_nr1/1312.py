#include<iostream>
#include<set>
using namespace std;
struct node{
	int r,c;
	
};
bool operator<(const node a,const node b){
		if(a.r<b.r)
			return 1;
		if(a.r==b.r&&a.c<b.c)
			return 1;
		return 0;
	}
const int N = 50;
int main(){
	freopen("out.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	set<node> h;
	int T,r,c;
	int i,j;
	int cas=1;
	int flag;
	char a[N][N];
	cin>>T;
	node tmp;
	node now;
	set<node>::iterator it;
	while(T--){
		flag=0;
		cin>>r>>c;
		h.clear();
		for(i=0;i<r;i++)
			for(j=0;j<c;j++){
				cin>>a[i][j];
				if(a[i][j]=='#'){
					tmp.r=i;
					tmp.c=j;
					h.insert(tmp);
				}
			}
		while(!h.empty()){
			it=h.begin();
			now.r=it->r;
			now.c=it->c;
			h.erase(h.begin());
			a[now.r][now.c]='/';

			tmp.r=now.r;
			tmp.c=now.c+1;
			if(h.count(tmp)==0){
				flag=1;
				break;
			}
			h.erase(h.find(tmp));
			a[tmp.r][tmp.c]='\\';

			tmp.r=now.r+1;
			tmp.c=now.c;
			if(h.count(tmp)==0){
				flag=1;
				break;
			}
			h.erase(h.find(tmp));
			a[tmp.r][tmp.c]='\\';

			tmp.r=now.r+1;
			tmp.c=now.c+1;
			if(h.count(tmp)==0){
				flag=1;
				break;
			}
			h.erase(h.find(tmp));
			a[tmp.r][tmp.c]='/';
		}
		cout<<"Case #"<<cas++<<":"<<endl;
		if(flag==1)
			cout<<"Impossible"<<endl;
		else{
			for(i=0;i<r;i++){
				for(j=0;j<c;j++){
					cout<<a[i][j];
				}
				cout<<endl;
			}
		}
	}
	return 0;
}