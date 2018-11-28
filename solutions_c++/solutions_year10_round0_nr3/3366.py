#include <iostream>
#include <queue>

using namespace std;

int main(){
	int xx,r,k,n;
	scanf("%d",&xx);
	
	for(int i=1;i<=xx;i++){
		queue<int> q,qt;
		scanf("%d %d %d",&r,&k,&n);
		while(n--){
			int tmp;
			scanf("%d",&tmp);
			q.push(tmp);
		}
		int alles=0;
		int tmp;
   
		while(r--){
			tmp=0;
			while(!q.empty() && tmp+q.front()<=k){
				tmp+=q.front();
				qt.push(q.front());
				q.pop();
			}
			alles+=tmp;
			while(!qt.empty()){
				q.push(qt.front());
				
				qt.pop();
			}
		}
		cout<<"Case #"<<i<<": "<<alles<<endl;
	}
	
}

