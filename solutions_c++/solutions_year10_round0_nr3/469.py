#include <cstdlib>
#include <cstdio>
#include <cstring>

//#define DEBUG 1

int T,k,R,N;
int group[1000];
int last[1000];
long long lasteuro[1000];

int main(){
	scanf("%d\n",&T);
	for(int i=1;i<=T;++i){
		scanf("%d %d %d\n",&R,&k,&N);
		for(int j=0;j<N;++j)
			scanf("%d",group+j);
		
		//reset
		memset(last,0,sizeof(last));
		memset(last,0,sizeof(lasteuro));
		int pos, iter, p;
		long long euro, size;
		euro = 0;
		pos=0;
		iter = 1;
		
		// calc
		for(;iter<=R;){
		
			// check for periodicity
			if(last[pos] != 0) {
				int period = iter - last[pos];

				int repeat = (R - iter) / period;
				long long diffeuro = euro - lasteuro[pos];
				if(repeat > 0){
				
					euro += repeat * diffeuro;
					iter += period * repeat;
				}
				
				// simulate rest
				while(iter<=R){
					size = 0;
					do{
						if(size + group[p] > k)
							break;
						size += group[p];
						p = (p+1) % N;
					} while(p!=pos);
		
					pos = p;
					euro += size;
					++iter;
				}
				break;
			} // end periodicity
			
			last[pos] = iter;
			lasteuro[pos] = euro;
			++iter;
			
			size = 0;
			p = pos;
			do{
				if(size + group[p] > k)
					break;
				size += group[p];
				p = (p+1) % N;
			} while(p!=pos);
		
			pos = p;
			euro += size;
		}
		
		printf("Case #%d: %lld\n",i,euro);


	}
}
