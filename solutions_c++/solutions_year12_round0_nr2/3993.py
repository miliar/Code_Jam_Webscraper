#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main( )
{
	int t,n,s,p;
	int total[110];
	int res;
	
	scanf("%d",&t);
	
	for(int cs=1;cs<=t;cs++){
		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;i++){
			scanf("%d",&total[i]);
		}
		
		if(p==0){
			res = n;
		}else{
			res = 0;
			
			for(int i=0;i<n;i++){
				if(total[i]==0){
					continue;
				}
				if(((total[i]+2)/3)>=p){
					res = res +1;
					continue;
				}
				
				if(s){
					if(((total[i]+4)/3)>=p){
						res = res + 1;
						s = s-1;
					}
				}
			}
		}
		
		cout<<"Case #"<<cs<<": "<<res<<endl;
	}
	
	return 0;
}

