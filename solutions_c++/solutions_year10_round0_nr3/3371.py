#include <iostream>
#include <cstdio>
#include <queue>;
using namespace std;

int R,K,N;
int g[1001];
int top[1001];
int sum[1001];
int T;
long long max_sum;
int main(void){
    //freopen("small.in","r",stdin);
   //freopen("small.out","w",stdout);
	freopen("large.in","r",stdin);
   freopen("large.out","w",stdout);
	cin>>T;
	int b=1;
	while(T--){
        
		cin>>R>>K>>N;
		queue<int> q;
		long long dollar=0;
		long long part=0;
		long long he=0;
		max_sum=0;
		int i,j,t;
		bool flag=false;
		for(i=1;i<=N;i++){
			cin>>g[i];
			he+=g[i];
			q.push(i);
		}
		cout<<"Case #"<<b++<<": ";
		if(he<=K){
            max_sum=he*R;
            cout<<max_sum<<endl;
            continue;      
        }
		int total=0;
		int head;
		for(i=1;flag==0;i++){
			total=0;
			top[i]=q.front();
			head=q.front();
			for(j=1;j<i;j++){
				if(head==top[j]) {
					flag=true;
					break;
				}
			}
			if(flag==1){
				break;
			}else{
				while((total+g[head])<=K){
					total=total+g[head];
					q.pop();
					q.push(head);
					head=q.front();
				}
				sum[i]=total;
			}	
		}
		int x,y;
		if(R<j){
			for(t=1;t<=R;t++){
            max_sum+=sum[t];
			}
			cout<<max_sum<<endl;
		}else{
         for(t=1;t<j;t++){
            max_sum+=sum[t];
			}
			R=R-(j-1);
			x=R/(i-j);
			y=R%(i-j);
			int c=0;
			for(t=j;t<i;t++){
            dollar+=sum[t];
            c++;
            if(c==y) part=dollar;
         }
         max_sum+=dollar*x+part;
         cout<<max_sum<<endl;
      }
		
	}
	//system("pause");
	return 0;
}
