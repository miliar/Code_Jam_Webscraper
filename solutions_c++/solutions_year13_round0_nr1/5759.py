#include <stdio.h>
#include <string.h>
char str[10][10];
int main()
{
	freopen("E:/A-small-attempt4.in","r",stdin);
    freopen("E:/a.out","w+",stdout);
	int t,i,j,a,b,flag,s,cas=1;
	char tmp;
	scanf("%d",&t);
	while(t--)
	{
		s=0;
		for(i=0;i<4;i++){
			scanf("%s",str[i]);
			for(j=0;j<4;j++){
				if(str[i][j]=='.')
					s++;
			}
		}
		a=b=0;
		for(i=0;i<4;i++)
		{
			j=0;flag=0;tmp = str[i][0];
			while(j<4 && (str[i][j]==tmp || (str[i][j]=='T' && flag==0) || tmp=='T')){
				if(str[i][j]=='T'){
					flag=1;
				}
				if(tmp=='T')
					tmp = str[i][j];
				j++;
			}
			if(j>=4){
				if(tmp=='O')
					a=1;
				else if(tmp=='X')
					b=1;
			}
		}
		
		for(i=0;i<4;i++)
		{
			j=0;flag=0;tmp = str[0][i];
			while(j<4 && (str[j][i]==tmp || (str[j][i]=='T' && flag==0) || tmp=='T')){
				if(str[j][i]=='T'){
					flag=1;
				}
				if(tmp=='T')
					tmp = str[j][i];
				j++;
			}
			if(j>=4){
				if(tmp=='O')
					a=1;
				else if(tmp=='X')
					b=1;
			}
		}
		
		i=0;flag=0;tmp = str[i][i];
		while(i<4 && (str[i][i]==tmp || (str[i][i]=='T' && flag==0) || tmp=='T')){	
			if(str[i][i]=='T'){
				flag=1;
			}
			if(tmp=='T')
				tmp = str[i][i];
			i++;
		}
		if(i>=4){
			if(tmp=='O')
				a=1;
			else if(tmp=='X')
				b=1;
		}
		

		i=0;j=3;flag=0;tmp = str[i][j];
		while(i<4 && (str[i][j]==tmp || (str[i][j]=='T' && flag==0) || tmp=='T')){
			if(str[i][j]=='T'){
				flag=1;
			}
			if(tmp=='T')
				tmp = str[i][j];
			i++;j--;
		}
		if(i>=4){
			if(tmp=='O')
				a=1;
			else if(tmp=='X')
				b=1;
		}

		if(a==0 && b==1)
			printf("Case #%d: X won\n",cas++);
		else if(a==1 && b==0){
			printf("Case #%d: O won\n",cas++);
		}else if(s!=0){
			printf("Case #%d: Game has not completed\n",cas++);
		}else{
			printf("Case #%d: Draw\n",cas++);
		}
		
	}
	return 0;
}
