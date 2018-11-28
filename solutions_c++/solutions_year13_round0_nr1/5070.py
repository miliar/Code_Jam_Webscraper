#include <stdio.h>
int T , cnt , C = 1;
bool xwin , ywin;
char G[6][6];
bool check_vertical( char key , int pos ){
	bool extra = 0;
	for ( int i = 0 ; i <= 3 ; i++ ){
		if ( G[i][pos] == 'T' ){
			if ( extra ) return false;
			extra = true;
				
		}
		else if ( G[i][pos] == key )
			continue;
		else
			return false;
		
	}	
	return true;
}
bool check_horizontal( char key , int pos ){
	bool extra = 0;
	for ( int i = 0 ; i <= 3 ; i++ ){
		if ( G[pos][i] == 'T' ){
			if ( extra ) return false;
			extra = true;		
		}
		else if ( G[pos][i] == key )
			continue;
		else
			return false;
		
	}	
	return true;
}
bool check_lutord( char key ){
	bool extra = false;
	for ( int i = 0 , j = 0 ; i <= 3 ; i++ , j++ ){
		if ( G[i][j] == 'T' ){
			if ( extra ) return false;
			extra = true;
		}	
		else if ( G[i][j] == key )
			continue;
		else
			return false;
		
	
	}	
	return true;
	

}
bool check_rutold( char key ){
	bool extra = false;
	for ( int i = 0 , j = 3 ; i <= 3 ; i++ , j-- ){
		if ( G[i][j] == 'T' ){
			if ( extra ) return false;
			extra = true;
		}	
		else if ( G[i][j] == key )
			continue;
		else
			return false;
		
	
	}	
	return true;
	

}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while ( T-- ){
		cnt = 0;
		xwin = ywin = false;
		for ( int i = 0 ; i <= 3 ; i++ ){
			scanf("%s",G[i]);
			for ( int j = 0 ; j <= 3 ; j++ )
				if ( G[i][j] == '.' )
					cnt++;
				
			
		}
		for ( int i = 0 ; i <= 3 ; i++ ){
			if ( check_vertical( 'X' , i ) )
				xwin = true;
			if ( check_horizontal( 'X' , i ) )
				xwin = true;	
			
		}
		if ( check_lutord( 'X' )  )	xwin = true;
		if ( check_rutold( 'X' )  ) xwin = true;
		for ( int i = 0 ; i <= 3 ; i++ ){
			if ( check_vertical( 'O' , i ) )
				ywin = true;
			if ( check_horizontal( 'O' , i ) )
				ywin = true;	
			
		}
		if ( check_lutord( 'O' )  )	ywin = true;
		if ( check_rutold( 'O' )  ) ywin = true;
		
		if ( xwin )
			printf("Case #%d: X won\n",C++);
		else if ( ywin )
			printf("Case #%d: O won\n",C++);
		else if ( cnt == 0 )
			printf("Case #%d: Draw\n",C++);
		else
			printf("Case #%d: Game has not completed\n",C++);
		
		
	}
	
	return 0;
} 
