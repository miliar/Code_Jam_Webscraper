#include "cstdio"
#include "vector"
#include "algorithm"
using namespace std;

#define pb push_back

FILE *in=fopen("B-large.in","r");
FILE *out=fopen("large","w");


int a[2000];



int main(){
	int t;
	int licz,L,N,C,iter;
	vector<int> x;
	vector<int> :: iterator it;
	long long time, spent;

	fscanf(in,"%d",&t);

	for(int k=1;k<=t;k++){

		x.clear();
		spent=0;
		iter=0;
		licz=0;
		fscanf(in,"%d%lld%d%d",&L,&time,&N,&C);

		for(int i=0;i<C;i++)
			fscanf(in,"%d",&(a[i]));
		
		while(spent<time && licz<N){
			licz++;
			spent+=2*a[iter++];
			iter%=C;
			if(spent>time){
				x.pb((spent-time)/2);
				spent=time;
			}
		}
		
		while(licz<N){
			x.pb(a[iter++]);
			iter%=C;
			licz++;
		}

		sort(x.begin(),x.end());

		it=x.end();
		while(it!=x.begin()){	
			it--;
			if(L>0){ 
				spent+=*it;
				L--;
			}
			else spent+=2*(*it);
		}
		fprintf(out,"Case #%d: %lld\n",k,spent);
	}



return 0;
}

