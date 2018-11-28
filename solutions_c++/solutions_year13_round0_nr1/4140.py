#include<cstdio>
using namespace std;

int main(){
	int k;
	scanf(" %d", &k);
	for(int T=1;T<=k;T++){
		char a[4][4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf(" %c",&a[i][j]);
			}
		}
		bool flag1 = false;
		bool flag2 = false;
		bool flag3 = false;
		for(int i=0;i<4;i++){
			int count1=0,count2=0;
		  for(int j=0;j<4;j++){
				if (a[i][j]=='X')
					count1++;
				if (a[i][j]=='O')
					count2++;
				if (a[i][j]=='.')
					flag3=true;
				if (a[i][j]=='T'){
					count1++;count2++;
				}					
		  }
			if (count1==4) flag1 = true;
			if (count2==4) flag2 = true;
		}
		if (flag1==true){ printf("Case #%d: X won\n",T); continue;}
		else if(flag2==true){ printf("Case #%d: O won\n",T); continue;}
		for(int i=0;i<4;i++){
			int count1=0,count2=0;
		  for(int j=0;j<4;j++){
		    if (a[j][i]=='X')
			    count1++;
			  if (a[j][i]=='O')
			    count2++;
	      if (a[j][i]=='T'){
	        count1++;count2++;
        } 
		  }
			if (count1==4) flag1=true;
			if (count2==4) flag2=true;
		}
		if (flag1==true){ printf("Case #%d: X won\n",T); continue;}
    else if(flag2==true){ printf("Case #%d: O won\n",T); continue;}
		int count1=0,count2=0;
		for(int i=0;i<4;i++){
			if (a[i][i]=='X')
         count1++;
      if (a[i][i]=='O')
         count2++;
      if (a[i][i]=='T'){
         count1++;count2++;
      } 
		}
		if (count1==4) flag1=true;
		if (count2==4) flag2=true;
		count1=0;count2=0;
		for(int i=0;i<4;i++){
			if (a[i][3-i]=='X')
			  count1++;
			if (a[i][3-i]=='O')
			  count2++;
      if (a[i][3-i]=='T'){
        count1++;count2++;
      } 
		}
		if (count1==4) flag1=true;
		if (count2==4) flag2=true;
		if (flag1==true){ printf("Case #%d: X won\n",T); continue;}
    else if(flag2==true){ printf("Case #%d: O won\n",T); continue;}
		else if(flag3==true) printf("Case #%d: Game has not completed\n",T);
		else printf("Case #%d: Draw\n",T);
	}
}
