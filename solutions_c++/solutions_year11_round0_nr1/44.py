#include<iostream>
#include<queue>

using namespace std;

int main(){
	int a,b, oa, ob;
	int cs, ans, ns;
	queue<int> qa,qb, oq;
	cin>>cs;
	freopen("A.out","w",stdout);
	for(int css=1;css<=cs;css++){
		cin>>ns;
		while(!qa.empty())qa.pop();
		while(!qb.empty())qb.pop();
		while(!oq.empty())oq.pop();
		for(int j=0;j<ns;j++){
			char c;
			int p;
			cin>>c; cin>>p;
			if(c=='O') {qa.push(p);oq.push(0);}
			else if(c=='B') {qb.push(p);oq.push(1);}
		}
		qa.push(100000);
		qb.push(100000);
		a = 1; b = 1;
		ans = 0;
		while(!oq.empty()){
			int curo = oq.front();
			oa = qa.front(); ob = qb.front();
			if(oa>a){
				a++;
			}else if(oa<a){
				a--;
			}else if(oa==a){
				if(curo==0){
					oq.pop();
					qa.pop();
				}
			}
			if(ob>b){
				b++;
			}else if(ob<b){
				b--;
			}else if(ob==b){
				if(curo==1){
					oq.pop();
					qb.pop();
				}
			}
				ans++;
		}
		printf("Case #%d: %d\n", css, ans);
	}
	return 0;
}