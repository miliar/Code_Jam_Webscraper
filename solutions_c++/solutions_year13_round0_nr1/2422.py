#include <stdio.h>
#include <string.h>

int main(){

	int test,c=1,i,j,a,flag,fin;
	char pic[5][5],ans[64];
	
	FILE *out = fopen("out.txt","w");
	
	for( scanf("%d",&test) ; test-- ; fprintf(out,"Case #%d: %s\n",c++,ans) ){
		fin=1;
		flag=0;
		ans[0]=0;
		for( i=0 ; i<4 ; i++ ) scanf("%s",pic[i]);
		
		for( i=0 ; !flag && i<4 ; i++ ){
			for( a=j=0 ; j<4 ; j++ ){
				if( pic[i][j]=='.' ){
					fin=a=0;
					break;
				}
				else if( pic[i][j]=='X' ){
					if( a==0 ) a=1;
					else if( a==2 ){
						a=0;
						break;	
					}
				}
				else if( pic[i][j]=='O' ){
					if( a==0 ) a=2;
					else if( a==1 ){
						a=0;
						break;	
					}
				}
			}
			if( a==1 ){
				strcpy(ans,"X won");
				flag=1;	
			}
			else if( a==2 ){
				strcpy(ans,"O won");
				flag=1;	
			}
		}
		for( i=0 ; !flag && i<4 ; i++ ){
			for( a=j=0 ; j<4 ; j++ ){
				if( pic[j][i]=='.' ){
					fin=a=0;
					break;
				}
				else if( pic[j][i]=='X' ){
					if( a==0 ) a=1;
					else if( a==2 ){
						a=0;
						break;	
					}
				}
				else if( pic[j][i]=='O' ){
					if( a==0 ) a=2;
					else if( a==1 ){
						a=0;
						break;	
					}
				}
			}
			if( a==1 ){
				strcpy(ans,"X won");
				flag=1;	
			}
			else if( a==2 ){
				strcpy(ans,"O won");
				flag=1;	
			}
		}
		for( a=i=0 ; !flag && i<4 ; i++ ){
			if( pic[i][i]=='.' ){
				fin=a=0;
				break;
			}
			else if( pic[i][i]=='X' ){
				if( a==0 ) a=1;
				else if( a==2 ){
					a=0;
					break;	
				}
			}
			else if( pic[i][i]=='O' ){
				if( a==0 ) a=2;
				else if( a==1 ){
					a=0;
					break;	
				}
			}
		}
		if( a==1 ){
			strcpy(ans,"X won");
			flag=1;	
		}
		else if( a==2 ){
			strcpy(ans,"O won");
			flag=1;	
		}
		
		for( a=i=0 ; !flag && i<4 ; i++ ){
			if( pic[i][3-i]=='.' ){
				fin=a=0;
				break;
			}
			else if( pic[i][3-i]=='X' ){
				if( a==0 ) a=1;
				else if( a==2 ){
					a=0;
					break;	
				}
			}
			else if( pic[i][3-i]=='O' ){
				if( a==0 ) a=2;
				else if( a==1 ){
					a=0;
					break;	
				}
			}
		}
		if( a==1 ){
			strcpy(ans,"X won");
			flag=1;	
		}
		else if( a==2 ){
			strcpy(ans,"O won");
			flag=1;	
		}
		
		if( !flag ){
			if( fin ) strcpy(ans,"Draw");
			else strcpy(ans,"Game has not completed");	
		}
	}

	return 0;
}

