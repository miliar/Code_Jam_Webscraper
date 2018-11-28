#include<stdio.h>
int main()
{
	int t,i,j;
	scanf("%d",&t);
	for(j=1;j<=t;j++){
		int n,s,p;
		scanf("%d%d%d",&n,&s,&p);
		printf("Case #%d: ",j);
		int a[n],ans=0;
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(i=0;i<n;i++){
			int score=a[i]/3;
			
			switch(a[i]%3){
				case 0: {if(score>=p){
						
						ans++;
					}
					else if(s>0&&score>0&&score+1>=p){
						ans++;
						s--;
						
					
					}
					break;
					}
				case 1:{if(score>=p||score+1>=p)
					ans++;
					else if(s>0&&score+1>=p){
						ans++;
						s--;
					}
					break;
					}
				case 2:{if(score+1>=p||score>=p)
						ans++;
					else if(s>0&&score+2>=p){
						ans++;
						s--;
					}
					break;
					}
			}}
			printf("%d\n",ans);}
	return 0;
}
