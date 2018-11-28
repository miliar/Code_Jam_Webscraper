#include <cstdio>
#include <vector>
using namespace std;
typedef struct{
	vector<long long> p;
	long long size;
	long long from,to;
}group;
long long v[3000];
vector<group> groups;
long long belongs[3000];
long long R,N,cap;
long long find(){
	groups.clear();
	group temp_group;
	long long i=0,z;
	for (z=0;z<3000;z++)
		belongs[z]=-1;
	long long sum=0;
	long long t=0;
	temp_group.from=0;
	temp_group.to=-1;
	temp_group.size=0;
	temp_group.p.clear();
	while (1){
	//	printf("ask belongs %d = %d\n",temp_group.from,belongs[temp_group.from]);
		if (belongs[temp_group.from]!=-1){
			//cycle_found
			long long cycle_start,cycle_length,cycle_size;
			cycle_start=belongs[temp_group.from];
			cycle_length=groups.size()-belongs[temp_group.from];
			long long j=0;
			cycle_size=0;
			sum=0;
			t=0;
			for (j=0;j<cycle_start;j++)
				sum+=groups[j].size;
			t=cycle_start;
			for (j=cycle_start;j<groups.size();j++){
				cycle_size+=groups[j].size;
			}
		//	printf("%d %d\n",cycle_start,cycle_size,t);
			sum+=((R-t)/(cycle_length))*cycle_size;

			for (j=0;j<((R-t)%cycle_length);j++){
				sum+=groups[cycle_start+j].size;
			}
			return sum;
		}
		if (temp_group.size+v[i]<=cap && temp_group.p.size()!=N){
			temp_group.size+=v[i];
			temp_group.p.push_back(v[i]);
			i++;
			i%=N;
		}else{
			sum+=temp_group.size;
			t++;	
			if (t==R){
				return sum;
			}
			temp_group.to=(i==0)?(N-1):i-1;
			belongs[temp_group.from]=groups.size();
			//printf("belongs %d %d\n",temp_group.from,groups.size());
		
		/*for (vector<long>::iterator x=temp_group.p.begin();x!=temp_group.p.end();x++)
				printf("%d ",*x);
			printf("\n");
			*/
			groups.push_back(temp_group);
			temp_group.to=-1;
			temp_group.from=i;
			temp_group.size=0;
			temp_group.p.clear();
		}
	
	}

}

int main(){
	long long T,i,j;
	scanf("%I64d",&T);
	for (i=0;i<T;i++){
		scanf("%I64d%I64d%I64d",&R,&cap,&N);
		for (j=0;j<N;j++){
			scanf("%I64d",&v[j]);	
		}
		printf("Case #%I64d: %I64d\n",i+1,find());
	}
}
