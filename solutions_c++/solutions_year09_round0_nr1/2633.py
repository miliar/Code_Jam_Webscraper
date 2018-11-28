#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>

FILE * fin = fopen("e:/cj/A-small-practice.in","r");
FILE * fout = fopen("e:/cj/A-small-practice0.out","w");

int  readLine( char *strline ) {
	char dilim = '\n' ;
	char ch ;
	int offset = 0 ;

	while( fread(&ch,1,1,fin) == 1 ) {
		if( ch == '\n' ) {
			strline[offset] = '\0' ;
			offset ++ ;
			break;
		} else {
			strline[offset] = ch ;
			offset ++ ;
		}
	}
	return offset ;
}


int splitLine( char *strline, char ** arrstr  ) {
	char dilim = ' ' ;
	char ch ;
	int offset = 0 ;
	char *strelement = new char [9999] ;
	int off1 = 0 ;

	int retInt = 0 ;
	while(  true ) {
		ch = strline[offset] ;

		if( ch == '\0'  ) {
			strelement[off1] = '\0' ;
			arrstr[retInt] = strelement ;
			retInt ++ ;
			break ;
		} else if( ch == dilim  ) {
			
			strelement[off1] = '\0' ;
			off1 = 0 ;
			arrstr[retInt] = strelement ;
			strelement = new char [9999] ;
			retInt ++ ;
		} else {
			strelement[off1] = ch ;
			off1++;
			
		}
		offset ++ ;
	}
	return retInt ;
}

void deleteArrStr( char ** arrstr,int size ) {
	for( int i = 0 ; i < size ; i ++ ) {
		delete arrstr[i] ;
	}
}

int javab = 0 ;

int rec( char **dic,char ** arr,int L,int D,int N , int dicid , int cln, int cp) {
	
	

	int i = 0 ;
	for( i = dicid ; i < D ; i ++ ) {
		if( dic[i][cln] == arr[cln][cp] ) {
			break;
		}
		for( int l = 0 ; l < cln && i +1 < D ; l++ ) {
			if( dic[i+1][l] != dic[i][l] ) {
				i = D-1;
				break ;
			}
		}
	}
	if( i != D ) {

		if( cln == L-1 ) {
			javab++; 
			return 1 ;
		}else {
			cln++;
			cp = 0 ;
			int t1= cp ;
			while( arr[cln][t1] != NULL ) {
				rec(dic, arr,L,D,N,i,cln,t1);
				t1++;
			}
		}

	}else {
		return 0 ;
		
	}
	
}



int main () {

			
	char *sline = new char [99999] ;
	char **arrstr = new char * [99999] ;

	char **dic = new char* [99999] ;

	readLine( sline ) ;
	
	int no = splitLine(sline,arrstr);
	int L,D,N ;
	L = atoi(arrstr[0]);
	D = atoi(arrstr[1]);
	N = atoi(arrstr[2]);

	int dc = 0 ;
	while( dc < D ) {
		char *sline = new char [20] ;
		readLine( sline ) ;
		dic[dc] = sline ;

		dc++ ;
	}
	
	for( int ii = 0 ; ii < D-1 ; ii ++ ) {
		for( int jj = ii+1 ; jj < D ; jj ++ ) {
			if( strcmp(dic[ii],dic[jj]) > 0 ) {
				char t[9999] ;
				strcpy( t,dic[ii]);
				strcpy( dic[ii],dic[jj]);
				strcpy( dic[jj], t );
			}
		}
	}

	int nc = 0 ;
	sline = new char [1000] ;
	char **arr = new char *[20] ;
	for( int k = 0 ; k < 20 ; k ++ ) {
		arr[k] = new char[20] ;
	}

	while( readLine(sline ) != 0 && nc < N ) {
		nc++ ;
		int tt = 0 ;

		
		int noc = 0;
		int nol = 0;
		int fl = 0 ;

		while( sline[tt] != NULL ) {
			if( sline[tt] == ')' ) {
				arr[nol][noc] = '\0' ;
				for( int ii = 0 ; ii < noc-1 ; ii ++ ) {
					for( int jj = ii+1 ; jj < noc ; jj ++ ) {
						if( arr[nol][ii] > arr[nol][jj] ) {
							char t =  arr[nol][ii];
							arr[nol][ii] = arr[nol][jj] ;
							arr[nol][jj] = t ;
						}
					}
				}
				nol ++ ;
				noc = 0 ;
				fl = 0 ;
			} else if( sline[tt] == '(' ) {
				noc = 0 ;
				fl = 1 ;
			}else{
				if( fl == 1 ) {
					arr[nol][noc] = sline[tt] ;
					noc++;
				}else{
					arr[nol][noc] = sline[tt] ;
					arr[nol][noc+1] = '\0' ;
					for( int ii = 0 ; ii < noc ; ii ++ ) {
						for( int jj = ii+1 ; jj < noc+1 ; jj ++ ) {
							if( arr[nol][ii] > arr[nol][jj] ) {
								char t =  arr[nol][ii];
								arr[nol][ii] = arr[nol][jj] ;
								arr[nol][jj] = t ;
							}
						}
					}
					noc = 0 ;
					nol++;
				}
			}
			tt++;
		}
		
		javab = 0 ;
		int t1= 0 ;
		while( arr[0][t1] != NULL ) {
			rec( dic,(char **)arr,L,D,N,0,0,t1) ;
			t1++;
		}
		fprintf(fout,"Case #%d: %d\n",nc,(int)javab);
		fflush(fout);
		
	}

}


