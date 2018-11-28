#include<stdio.h>
#include<string>
#include<map>
//#include<Windows.h>
using namespace std;
int main(){
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int n,t=1,surprise,people,min_score;
	scanf("%d",&n);
	for(int q=0;q<n;q++){
		int score;
		int cases=0;
		scanf("%d%d%d",&people,&surprise,&min_score);
		for(int i=0;i<people;i++){
			
			scanf("%d",&score);
			int base = (int)(score / 3);


			  switch (score % 3)
			  {
				case 0:
				{
	
				 
				  if (base >= min_score)
					  {
						
						  cases++;
					  }
				  else
					if (surprise > 0 && base > 0 && base + 1 >= min_score)
					{            
					  cases++;
					  surprise--;
			
					}            
				  
				  break;
				}

				case 1:
				{
				  
		
				  if (base >= min_score || base + 1 >= min_score)
				  {
					  cases++;
				
				  }
				  else
				  {
	
					if (surprise > 0 && base + 1 >= min_score)
					{
					  
					  cases++;
					  surprise--;
					}
				  }

				 
				  break;
				}

				case 2:
				{          
				  

			
				  if (base + 1 >= min_score || base >= min_score)
				  {
					
					cases++;
				  }
				  else
				  {
					if (surprise > 0 && base + 2 >= min_score)
					{
					
					  cases++;
					  surprise--;
					}
				  }

				  break;
				}
			  }
		}
		printf("Case #%d: %d\n",t++,cases);

	}
	//system("pause");
	return 0;
}