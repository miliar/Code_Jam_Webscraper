#include <iostream>

using namespace std;
//roller coaster can hold k people at once
//The roller coaster will run R times in a day.
int main()
{	
	int test;
	scanf("%d",&test);
	int *pass= new int[10];
	for(int kk = 1 ; kk<=test;kk++)
	{
		int r , k ,n;
		scanf("%d%d%d",&r,&k,&n);
		
		int i =0;
		while(i < n ){
			scanf("%d",&pass[i++]);
		}
		int count =0 , ind =0 ,m=0;
		while(r--){
				int pep =0 ;
				for(int i = ind;i<n ; i=(i+1)%n){
					if(count+pass[i]<=k  ){
						count+=pass[i];m+=pass[i];
						if((i+1)%n == ind){
							count =0;ind = i;break;
						}
					}else {count =0;ind = i;break;}				
				}
			}
				printf("Case #%d: %d\n",kk,m);
		}
	
		delete[] pass;
	return 0;
}
