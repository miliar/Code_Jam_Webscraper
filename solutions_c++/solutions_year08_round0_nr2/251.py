#include <stdio.h>
#include <stdlib.h>


int N, T, NA, NB ;

class c_heap{
public :
	int entry[256], count ;
	
	void reset(int count){
		int i ;
		this->count = count ;
		entry[1] = 0x7FFFFFFF ;
		for( i=1 ; i<=count ; i++)
			entry[i] = 0 ;
	}
	
	void add(int min){
		int now ;
		int par ;
		
		entry[++count] = min ;
		now = count ;
		
		while( now > 1 ){
			par = now >> 1 ;
			if( entry[now] < entry[par] ){
				min = entry[now] ;
				entry[now] = entry[par] ;
				entry[par] = min ;
				
				now = par ;
			}				
			else
				break ;
		}
	}
	
	void extra_min(){
		int now, L, R ;
		
		entry[1] = entry[count--] ;
		now = 1 ;
		
		while( (L=(now<<1)) <= count ){
			R = L+1 ;
			if( R<=count && entry[R]<entry[L] )
				L = R ;
				
			if( entry[L] < entry[now] ){
				R = entry[now] ;
				entry[now] = entry[L] ;
				entry[L] = R ;

				now = L ;
			}
			else
				break ;
		}

		if( count == 0 )
			entry[1] = 0x7FFFFFFF ;
	}	
} ;


int ListA[128][2], ListB[128][2] ;


char str[16] ;
int get_minute(void){
	int hour, min ;
	
	scanf("%s", str) ;
	sscanf(str, "%d", &hour) ;
	sscanf(str+3, "%d", &min) ;
	
	return hour*60 + min ;
}

c_heap ableA, ableB ;

bool test1(int sa, int sb){

	int indA = 0 ;
	int indB = 0 ;
	
	ableA.reset(sa) ;
	ableB.reset(sb) ;

	while( indA <NA || indB<NB ){
		if( ableA.entry[1] > ListA[indA][0] && ableB.entry[1] > ListB[indB][0] )
			return false ;
			
		while( ableA.entry[1] <= ListA[indA][0] ){
			ableA.extra_min() ;
			ableB.add( ListA[indA][1] ) ;
			indA ++ ;
		}
		while( ableB.entry[1] <= ListB[indB][0] ){
			ableB.extra_min() ;
			ableA.add( ListB[indB][1] ) ;
			indB ++ ;
		}
	}		
	return true ;
}


bool test( int sum, int*ans){
	int a ;
	for( a=0 ; a<=sum ; a++){
		if( test1(a,sum-a) ){
			ans[0] = a ;
			ans[1] = sum-a ;
			return true ;
		}
	}
	return false ;
}


int cmp(const void*a, const void*b){
	return *((int*)a) - *((int*)b) ;
}

int main(void){

	int cases ;
	int i ;
	
	int ans[2] ;
	int max, min, sum ;
	
	
	scanf("%d", &N) ;
	for( cases=1 ; cases<=N ; cases++){
		scanf("%d%d%d", &T, &NA, &NB) ;
		
		for( i=0 ; i<NA ; i++ ){
			ListA[i][0] = get_minute() ;
			ListA[i][1] = get_minute() + T ;
		}
		ListA[i][0] = -1 ;
		qsort( ListA, NA, sizeof(ListA[0]), cmp ) ;

		for( i=0 ; i<NB ; i++ ){
			ListB[i][0] = get_minute() ;
			ListB[i][1] = get_minute() + T ;
		}
		ListB[i][0] = -1 ;
		qsort( ListB, NB, sizeof(ListB[0]), cmp ) ;

		min = 0 ;
		max = NA + NB ;
		while( min < max ){
			sum = (min+max)>>1 ;
			
			if( test(sum,ans) ){
				max = sum ;
			}
			else{
				min = sum + 1 ;				
			}
		}
		
		test(min, ans) ;
		printf("Case #%d: %d %d\n", cases, ans[0], ans[1]) ; 		
	}

	return 0 ;
}
