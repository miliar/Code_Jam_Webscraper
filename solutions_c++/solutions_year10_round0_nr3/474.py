#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <string.h>
using namespace std;
const int max_size=1003;

struct group{
	int id,size;
};


struct ride{
	long long cost;
	int next;
};

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,R,k,N;
	long long sum;
	ride weigth[max_size];
	queue <group> Ocher;
	bool B[max_size];
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		sum=0;
		memset(B,0,max_size);
		scanf("%d %d %d",&R,&k,&N);
		for(int j=0;j<N;j++){
			group tmp;
			tmp.id=j;
			scanf("%d",&tmp.size);
			Ocher.push(tmp);
		}
		int l=0,now=0;
		for(;l<R && !B[now];l++){
			int size=k;
			long long temp_sum=0;
			if(Ocher.front().size<=size){
				temp_sum=Ocher.front().size;
				size-=Ocher.front().size;
				Ocher.push(Ocher.front());
				Ocher.pop();
				while(size>=Ocher.front().size && now!=Ocher.front().id){
					temp_sum+=Ocher.front().size;
					size-=Ocher.front().size;
					Ocher.push(Ocher.front());
					Ocher.pop();
				}
				B[now]=true;
				weigth[now].cost=temp_sum;
				weigth[now].next=Ocher.front().id;
				now=Ocher.front().id;			
				sum+=temp_sum;
			}
		}
		if(l<R){
			long long cycle_size=0,cycle_sum=0;
			int tmp=now;
			cycle_size++;
			cycle_sum+=weigth[tmp].cost;
			tmp=weigth[tmp].next;
			while(tmp!=now){
				cycle_size++;
				cycle_sum+=weigth[tmp].cost;
				tmp=weigth[tmp].next;
			}
			R-=l;
			sum+=(R/cycle_size)*cycle_sum;
			if(R%cycle_size){
				long long g=R%cycle_size;
				for(l=0;l<g;l++){
					sum+=weigth[now].cost;
					now=weigth[now].next;
				}
			}
		}
		printf("Case #%d: %lld\n",i+1,sum);
		while(!Ocher.empty())
			Ocher.pop();
	}

	return 0;
}