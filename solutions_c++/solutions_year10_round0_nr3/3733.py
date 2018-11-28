#include<iostream>
#include <queue>
using namespace std;
int main(){
	int cases;
	cin>>cases;
	int r, k, n,trips,temp;
	int tempCount=0;
	int money[cases];
	while(tempCount<cases){
		trips=0;
		money[tempCount]=0;
		cin>>r>>k>>n;
		queue<int> q;
		queue<int> tempq;
		int g;
		
		for (int i=0;i<n;i++){
			cin>>g;
			q.push(g);
		}
		
		
		while(trips<r){
			trips++;
			temp=0;
			while(!q.empty() && temp<k){
				if(k>=temp+q.front()){					
					temp=temp + q.front();
					tempq.push(q.front());
					q.pop();					
				}
				else
					break;
			}
			while(!tempq.empty() ){
				q.push(tempq.front());
				tempq.pop();
			}
			money[tempCount]=money[tempCount]+temp;
		}		
		tempCount++;
	}
	for(int i=0;i<cases;i++)
		cout<<"Case #"<<(i+1)<<": "<<money[i]<<endl;
	return 0;
}