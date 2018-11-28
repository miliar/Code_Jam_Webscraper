#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
int main(){
	int T,N;
	long long int R,k,g;
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("C-small2.out", "w", stdout);
    scanf("%d",&T);
    vector<long long int> groups;
	long long int summ=0;
	long long int rev=0;
	long long int once=0;
	for(int i=0;i<T;i++){
		summ=rev=once=0;
		groups.clear();
		scanf("%lld%lld%d",&R,&k,&N);
		for(int m=0;m<N;m++){
			scanf("%lld",&g);
			groups.push_back(g);
		}
			
		for(vector<long long int>:: iterator iter=groups.begin();iter!=groups.end();iter++)
			summ+=*iter;
		if(summ<=k){
			rev=R*summ;
		}
		else{
			vector<long long int>:: iterator iter1=groups.begin();
			for(int j=0; j<R; j++){
				once=0;
				while(once<k){
					once+=*iter1;
					if(once>k){
						once-=*iter1;
						break;
					}
					else {
						iter1++;
						if(iter1==groups.end()){
							iter1=groups.begin();
						}
					}
				}
				rev+=once;
			}
		}
		cout<<"Case #"<<i+1<<": "<< rev<<endl;
	}
	return 0;
}
			
				
				
    
