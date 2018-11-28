#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>

using namespace std;

int Plus(int a, int b)
{
 	int sum = 0, i = 0, m, n;
    while(a&&b)
    {
	    m = (a&1) ;
	    n = (b&1) ;
	    //printf("m = %d n = %d\n", m, n);
	    sum += (m^n) * (1<<i);
		a >>= 1 ;
		b >>= 1 ;  		  
		i ++ ; 
    }
    while(a)
    {
        sum += (a&1) * (1<<i) ;
        a >>= 1 ;
        i ++ ;
    }
    while(b)
    {
        sum += (b&1) * (1<<i) ;
        b >>= 1 ;
        i ++ ;
    }
    return sum ;
}

int sum1, sum2, num[20], N, sum, rsum1, rsum2;
bool res ;

void dfs(int d)
{
    if(d >= N)
	{
	    if(sum1 == sum2 && sum2 != 0) {res = 1 ; sum = max(sum, max(rsum1, rsum2));/* printf("rsum1 = %d rsum2 = %d\n", rsum1, rsum2);*/}
		return ; 	 
    } 	 
    int i, t ;
    for(i = 0; i < 2; i ++)
    {
	    
	    if(i)
		{
	        t = sum1 ;
		    sum1 = Plus(sum1, num[d]);
		    rsum1 += num[d]; 
			dfs(d + 1) ;
			sum1 = t ; 
			rsum1 -= num[d];
        } 	
		else 
		{
		    t = sum2 ;
			sum2 = Plus(sum2, num[d]) ;
			rsum2 += num[d];
			dfs(d + 1) ;
			sum2 = t ;  	
			rsum2 -= num[d] ; 
        }	
    }
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int T, i, j, no = 1 ;
    
    scanf("%d", &T);
    while(T --)
    {
	    scanf("%d", &N);
		for(i = 0; i < N; i ++) scanf("%d", &num[i]);
		sum2 = res = sum = rsum2 = 0 ;
		sum1 = rsum1 = num[0] ;
		dfs(1);
		printf("Case #%d: ", no ++); 	
		if(!res) printf("NO\n");
		else printf("%d\n", sum);	
    }
    
    
    //system("pause");
    return 0 ;
}
