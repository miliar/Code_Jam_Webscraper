#include <stdio.h>
#include <conio.h>
#include <string.h>

long n,i,j,k,l,q,se,tab[10],sw=0,sum=0,mark;
char s[10][102]={'\0'},qu[102]={'\0'};

int main(void){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
    scanf("%ld",&n);
    for(i=0;i<n;i++,sw=0,mark=11){
        for(j=0;j<10;j++) tab[j]=0;
        scanf("%ld",&se);
        gets(qu);//bug
        for(j=0;j<se;j++){
            gets(s[j]);
		}
        scanf("\n%ld\n",&q);
        for(j=0;j<q;j++){
            gets(qu);
			
			//search
			for(k=0;k<se;k++){
				if(!strcmp(s[k],qu))
					break;
			}
			
			//From last loop
			if(sum==1 && mark==k){
				sw++;
				for(l=0;l<se;l++){
					if(l!=mark)
						tab[l]=0;
				}
			}
			
			tab[k]++;
			
			//search for 0
			for(l=0,sum=0;l<se;l++){
				if(tab[l]==0)
					sum++;
			}
			
			if(sum==1){
				for(l=0;l<se;l++){
					if(tab[l]==0){
						mark=l;
						break;
					}
				}
			}
		}
		
		//Conclusion
		printf("Case #%ld: %ld\n",i+1,sw);
    }
    return 0;
}
