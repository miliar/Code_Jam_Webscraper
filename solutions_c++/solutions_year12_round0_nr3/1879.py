#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <map>
using namespace std;

map <pair<int,int>,int> MAP;

main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T,t,i,j,k,d,A,B,tmp;
	scanf(" %d",&T);
	for(t=0;t<T;t++){
		scanf(" %d %d",&A,&B);
		MAP.clear();
		int ans = 0;
		d = 0;
		i = A;
		while(i>0){
			i /= 10;
			d++;
		}
		
		for(i=A;i<=B;i++){
			int c = 0;
			int num[15];
			tmp = i;
			j = 0;
			while(tmp>0){
				num[j++] = tmp%10;
				tmp /= 10;
			}
			for(k=0;k<d-1;k++){
				num[d] = num[0];
				for(j=1;j<=d;j++)
					num[j-1] = num[j];
				int nn = 0;
				for(j=d-1;j>=0;j--)
					nn = nn*10+num[j];
				//printf("%d==%d\n",i,nn);
				if(nn>i && nn<=B){
					if(MAP.find(make_pair(i,nn))==MAP.end()){
						c++;
						MAP[make_pair(i,nn)] = c;
					}
				}
			}
			ans += c;
		}
		
		printf("Case #%d: %d\n",t+1,ans);
	}
}