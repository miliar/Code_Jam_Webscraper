#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>
#include<map>
using namespace std; 

int main(void){
	FILE*in=fopen("D://Downloads/C-large.in","rt");
	FILE*out=fopen("C:/Users/lenovo/Desktop/out.txt","wt");
	int test; fscanf(in,"%d",&test); 
	for(int ti=1;ti<=test;ti++)
	{
		fprintf(out,"Case #%d: ",ti);
		int n; fscanf(in,"%d",&n);
		int orsum=0,sum=0,min=10000000;
		for(int i=0;i<n;i++)
		{
			int t; fscanf(in,"%d",&t);
			orsum=orsum^t;
			sum+=t;
			if(min>t) min=t;
		}
		if(orsum) fprintf(out,"NO\n");
		else fprintf(out,"%d\n",sum-min);
	}
	return 0;
}

