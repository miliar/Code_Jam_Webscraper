#include <cstdio>
#include <cstdlib>
#include <algorithm>

#define SIZE_L 110

FILE *in , *out ;

int T ;
char str[SIZE_L] ;

char map[30] = "yhesocvxduiglbkrztnwjpfmaq" ;

int main(void)
{
	in = fopen("A-small-attempt0.in" , "r") ;
	out = fopen("A-small-attempt0.out" , "w") ;
	
	fscanf(in , "%d" , &T) ;
	fgets(str , SIZE_L , in) ;
	for(int count = 1 ; count <= T ; ++count)
	{
		fgets(str , SIZE_L , in) ;
		//printf("%d [%s]\n" , count , str) ;
		
		fprintf(out , "Case #%d: " , count) ;
		
		for(int i = 0 ; str[i] != '\0' ; ++i)
		{
			if(str[i] >= 'a' && str[i] <= 'z')
				fprintf(out , "%c" , map[str[i] - 'a']) ;
			else fprintf(out , "%c" , str[i]) ;
		}
	}
	
	fclose(in) , fclose(out) ;
	
	//system("pause") ;
	
	return 0 ;
}

/*
abcdefghijklmnopqrstuvwxyz -- original
ynficwlbkuomxsevzpdrjgthaq -- google

abcdefghijklmnopqrstuvwxyz -- google
yhesocvxduiglbkrztnwjpfmaq -- original
/*


/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand

rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities

de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up
*/
