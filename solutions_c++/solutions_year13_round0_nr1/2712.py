#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
	int t,it=1,i,j,sum;
	char ch[6];
	int a[4][4];
	int b[10][5];
	scanf("%d",&t);
	while(t--){
		getchar();
		for(i=0;i<4;i++){
			scanf("%s",ch);
			for(j=0;j<4;j++){
				
				if(ch[j]=='X') a[i][j]=1;
				else if(ch[j]=='O') a[i][j]=2;
				else if(ch[j]=='T') a[i][j]=3;
				else a[i][j]=0;
				
			}
		}
		
		
		/*for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cout<<a[i][j]<<"  ";
				
			}
			cout<<endl;
		}
		cout<<endl;
		*/
		
		for(i=0;i<10;i++){
			for(j=0;j<5;j++){
				b[i][j]=0;
			}
		}
		int ctr=0;
		for(i=0;i<4;i++,ctr++){
			for(j=0;j<4;j++){
				b[ctr][a[i][j]]++;
			}
		}
		for(i=0;i<4;i++,ctr++){
			for(j=0;j<4;j++){
				b[ctr][a[j][i]]++;
			}
		}
				
		for(i=0;i<4;i++){
			b[ctr][a[i][i]]++;
		}	
		ctr++;	
		for(i=0;i<4;i++){
			b[ctr][a[i][3-i]]++;
		}
		
		for(i=0;i<10;i++){
			for(j=1;j<4;j++){
				b[i][4]+=b[i][j];
			}
		}
		
		
		/*for(i=0;i<10;i++){
			for(j=0;j<5;j++){
				cout<<b[i][j]<<" ";
			}
			cout<<endl;
		}
		cout<<endl;
		*/
		int flag=0;
		for(i=0;i<10;i++){
			if(b[i][4]==4){
				
				if(b[i][1]==4 ||( b[i][1]==3 && b[i][3]==1)){
					flag=1;
					printf("Case #%d: X won\n",it++);
					break;
				}	
				else if(b[i][2]==4||( b[i][2]==3 && b[i][3]==1)){
					flag=1;
					printf("Case #%d: O won\n",it++);
					break;
				}	
					
				}
		}		
		if(flag==0){
			sum=0;
			for(i=0;i<10;i++){
				
				sum=sum+b[i][4];
				
			}
			
			if(sum==40){
				printf("Case #%d: Draw\n",it++);
				
				
			}
			else{
				
				printf("Case #%d: Game has not completed\n",it++);
			}
		}		
			
			
		
		
		
	}
	
	return 0;
}
