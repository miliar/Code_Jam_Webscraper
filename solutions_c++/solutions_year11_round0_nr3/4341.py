#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
//typedef long long i64;
typedef __int64 i64;
/**/
const int nt= 3;
int testing[nt]={3,5,6};
/**/
//
//  #define DBG_CODE
//
//
int label[1024]={0};
int comb[1024]={0}; 
i64 val[1024]={0};

/**/
i64 add(i64 x1, i64 x2)
{
	return (x1^x2);
}
/**//*
//#include <stdio.h>
void printc(int comb[], int k) {
	printf("{");
	int i;
	for (i = 0; i < k; ++i)
		printf("%d, ", comb[i]);
	printf("\b\b}\n");
}
/**/
void setLabel(int comb[], int k,int* label) {
	
#ifdef DBG_CODE
	printf("{");
#endif
	int i;
	for (i = 0; i < k; ++i)
	{

#ifdef DBG_CODE
		printf("[%d] %d, ", 
			comb[i], val[comb[i]]);
#endif
		label[comb[i]]= 1;
	}
	
#ifdef DBG_CODE
	printf("\b\b}\n");
#endif
}

int next_comb(int comb[], int k, int n) {
	int i = k - 1;
	++comb[i];
	while( 
		(i >= 0) && 
		(comb[i] >= n - k + 1 + i)
		) 
	{
		--i;
		++comb[i];
	}
	if (*comb > n - k)
		return 0; 
	for (i = i + 1; i < k; ++i)
		comb[i] = comb[i - 1] + 1;
	return 1;
}
/**//*
int main(int argc, char *argv[]) {
	int n = 3;
	int k = 2; 
	int comb[16]; 
	int i;
	for (i = 0; i < k; ++i)
		comb[i] = i;
	printc(comb, k);
	while (next_comb(comb, k, n))
		printc(comb, k);

	return 0;
}
/**/

void sum_comp(i64* p1,i64* p2,
			  i64* val, int n,
			  int* label)
{
	i64 x1=0;
	i64 x2=0;
	int i=0; // * ptr= label+n-1;
	for(;i<n;i++)
	{
		(label[i]?x1:x2)^= val[i];
	}
	*p1= x1;
	*p2= x2;
	/**/
#ifdef DBG_CODE
int j=0;
for(i=0;i<n;i++)
{
	if(label[i])
		j++;
}
printf("bipartite: (%d, %d)\n",j,n-j);
#endif
	/**/
	return;
/*		if(label[i]?x1:x2)
			x1^= val[i];
		else
			x2^= 
		if(ptr==label)
			break;
	}
/**/	

}
//
#ifndef MAX
#define MAX(a,b) (a>b?a:b)
#endif
//
int i64_cmp(const void *a, const void *b) 
{ 
    const i64 *ia = (const i64 *)a; 
	const i64 *ib = (const i64 *)b;
    return *ia  - *ib; 
} 
i64 sum_real(i64* val,int n,int* label)
{
	i64 sum=0;
	int i=0;
	for(;i<n;i++)
	{
		if(!label[i])
		{
			sum+= val[i];
		}
	}
	return sum;
}

int main() 
{
	int T= 1; 
#ifndef DBG_CODE
  scanf("%d", &T);
#endif
  for (int Ti = 1; Ti <= T; ++Ti) 
  {
//  fprintf(stderr, "Case #%d of %d...\n", Ti, T);
    int n= nt; 
#ifndef DBG_CODE
		scanf("%d",&n);
#endif
//	vector<i64> C; 
/**/
//	scanf("%d", &n);
	int i,k;
	for(i=0;i<n;i++)
	{
		i64 x= testing[i];
#ifndef DBG_CODE
		scanf("%lld",&x);
#endif
		val[i]= x;
//		C.push_back(k);
	}
	/**/
	/**/
    qsort(val,n, sizeof(i64), i64_cmp);
//	std::sort(C.begin(),C.end());
	/**/
#ifdef DBG_CODE
	for(i=0;i<n;i++)
	{
		printf("(%d)= %lld\n",i,val[i]);
	}
	printf("\n");
#endif
	/**/
	/**/
	int maxima=-1;
	/**/
	for(k=1;k<n;k++)
	{
		memset(label,0x0,sizeof(int)*1024);
		for (i = 0; i < k; ++i)
		{
			comb[i] = i;
		//	comb[i] = C[i];
		}
		/**/
		do
		{
			//printc(comb, k);
			setLabel(comb,k,label);
			i64 x1=0,x2=0;
			sum_comp(&x1,&x2,val,n,label);			
			
#ifdef DBG_CODE
	printf("x1= %lld\n",x1);
	printf("x2= %lld\n",x2);
#endif
			if(x1==x2)
			{
				maxima= // MAX(x1,x2);
				sum_real(val,n,label);
//				maxima= MAX(x1,x2);
				break;
			}
		}
		while (next_comb(comb, k, n));		
		if(maxima>0)
		{
#ifdef DBG_CODE
	printf("ans.= ");
	printf("%lld \n",maxima);
#endif
			break;
		}
	}
	/**/
    printf("Case #%d: ",Ti);
	if(maxima>0)
		printf("%lld",maxima);
	else
		printf("NO");
	printf("\n");
	/**/
	/**//*
	printf("1: %d\n",add(5,4));
	printf("2: %d\n",add(7,9));
	printf("3: %d\n",add(50,10));
	/**/
#ifdef DBG_CODE
	for(i=0;i<n;i++)
	{
		printf("(%d)= %lld\n",i,val[i]);
	}
	printf("\n");
	/**/
//	scanf("%d %lld", &n, &k);
/*  if ((k + 1) % (1 << n) == 0) 
	{
		printf("Case #%d: %s\n", Ti, "ON");
	}
    else 
	{
		printf("Case #%d: %s\n", Ti, "OFF");
	}
	/**/
	getchar();
#endif
  }
  return 0;
}
