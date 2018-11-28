#include<iostream>
#include<queue>
using namespace std;
int n,k,r,income;
queue<int>line;
queue<int>tmp;
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("b.txt","w",stdout);
	int tc,ns,temp,t,flag;
	cin>>tc;
	for(int z=0;z<tc;z++){
		cin>>r>>k>>n;
		income=0;
		while(!line.empty()) line.pop();
		for(int i=0;i<n;i++){
			cin>>ns;
			line.push(ns);
		}
		
		for(int j=0;j<r;j++){
			temp=k;
			flag=1;
			while(temp>0 && flag==1 && line.size()>0){
				t=line.front();
			//	printf("%d ",t);
				if(temp-t>=0){
					line.pop();
					income+=t;
					temp-=t;
					tmp.push(t);
				}
				else flag=0;
			}

			while(!tmp.empty()){
				line.push(tmp.front());
				tmp.pop();
			}

		}
		
		printf("Case #%d: %d\n",z+1,income);


	}
	return 0;
}