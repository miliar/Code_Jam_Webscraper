#include<stdio.h>
#include<math.h>

_int64 cor[100010][2];

_int64 main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	_int64 N,n,a,b,c,d,x,y,m;
	_int64 i,j,k,kk;
	_int64 sum;
	scanf("%I64d",&N);

	for(i=0;i<N;i++){
		scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d",&n,&a,&b,&c,&d,&x,&y,&m);
		
		sum = 0;

		cor[0][0] = x;
		cor[0][1] = y;
		for(j = 1;j<n;j++){
			x= (a * x + b) % m;
			y = (c * y + d) % m;
			cor[j][0] = x;
			cor[j][1] = y;
		}
		
		for(j = 0;j<n;j++){
			for(k=j+1;k<n;k++){
				for(kk=k+1;kk<n;kk++){
					if(cor[j][0]==cor[k][0] && cor[j][1]==cor[k][1] ||
						cor[j][0]==cor[kk][0] && cor[j][1]==cor[kk][1]
						||cor[k][0]==cor[kk][0] && cor[k][1]==cor[kk][1]
						)continue;
					if( (cor[j][0]+cor[k][0]+cor[kk][0])%3==0 &&(cor[j][1]+cor[k][1]+cor[kk][1])%3==0)sum++;
				}
			}
		}
		printf("Case #%I64d: %I64d\n",i+1,sum);
	}

	return 0;
}