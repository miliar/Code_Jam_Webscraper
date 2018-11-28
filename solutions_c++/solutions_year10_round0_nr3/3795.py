#include <iostream>
#include <cstdio>

using namespace std;


int main()
{
	int cases,c,n;
	long g[10000],capacity,rides,rideno,x;
	long long income,add,next,total,i;
	FILE*fp;
	
	fp=fopen("nirasmall.txt","a");
	
	cin >> cases;
	for(c=1;c<=cases;c++){
		cin >> rides >> capacity >> n;
		
		for(i=0;i<n;i++) cin >> g[i];
		
		total=0;
		for(i=0;i<n;i++) total+=g[i];
		if(total<=capacity) income=total*rides;
		else{
			next=0;
			rideno=0;
			income=0;
			for(x=0;;x++){
				add=0;
				for(i=next;;i++){
					add+=g[(i%n)];
					if(add>capacity){
						next=i;
						add-=g[(i%n)];
						income+=add;
						rideno++;
						break;
					}
				}
				if(rideno==rides) break;
			} 
		}
			
		fprintf(fp,"Case #%d: %d\n",c,income);
		
	}
	fclose(fp);
	return 0;
		
}


