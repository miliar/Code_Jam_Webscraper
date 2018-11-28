#include <cstdio>
#include<set>

int pow10[8]={1,10,100,1000,10*1000,100*1000,1000*1000,10*1000*1000};

int rotate(int a,int nchars){
return (a/10)+(a%10)*pow10[nchars-1];
}

int main(){
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		int res=0;
		int min, max;
		scanf("%d %d",&min, &max);
		int ndig=0;
		while(pow10[ndig]<max)ndig++;
		for(int j=min;j<=max;j++){
			int l=j;
			std::set<int> s;
			for(int k=1;k<ndig;k++){
				l=rotate(l,ndig);
				if(l>j && l<=max){s.insert(l);}
			}
			res+=s.size();
		}
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}