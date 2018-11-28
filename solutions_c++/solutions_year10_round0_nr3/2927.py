#include <limits.h>
#include <iostream>
#include <stdio.h>
#include <bitset>
#include <string>
#include <vector>
using namespace std;
int main()
{


	freopen("B-small.in","r",stdin);
	freopen("A-small.out","w",stdout);

	int cases,r,k,n;
	scanf("%d\n",&cases);
	int res=0;
	for(int i=0;i<cases;i++){
		res=0;
		scanf(" %d %d %d\n",&r,&k,&n);
		
			vector<int> g(n);
			for(int j=0;j<n;j++){

					scanf(" %d",&g[j]);


			}

			scanf("\n");
			int rides=0;
			int accum=0;
			int cont=0;
			int aux=0;
			while(rides<r){
					accum=0;
					aux=cont;
					while(accum+g[cont]<=k){

						accum+=g[cont];
						cont++;
												
						if(cont>=g.size())cont=0;
						if(cont==aux)break;
					}
					res+=accum;
					rides++;
			}
			

		


		printf("Case #%d: %d\n",i+1,res);
	}
	

}
