# include <Stdio.h>
# include <string>
# include <vector>
//# include <map>


using namespace std ;


# define CTI(x) ((x) - 'A')


char combine[30][30] ;
char opposed[30][30] ;
char table[30] ;


int IsOpposed (char c)
{
	char i ;
	for (i = 'A' ; i <= 'Z' ; i++)
	{
		if (table[CTI(i)] && opposed[CTI(i)][CTI(c)] == 1)
			return 1 ;
	}

	return 0 ;
}

string work(string str, int n)
{
	string rtn = "" ;
	char ch ;

	char stack[110] ;
	int i, cnt = 0 ;

	
	stack[cnt++] = str[0] ;
	table[CTI(str[0])] = 1 ;
	for (i = 1 ; i < n ; i++)
	{
		//combine
		if (cnt != 0 && combine[CTI(str[i])][CTI(stack[cnt-1])] != 0)
		{
			ch = combine[CTI(str[i])][CTI(stack[cnt-1])] ;
			table[CTI(stack[cnt-1])] -- ;
			cnt-- ;
			stack[cnt++] = ch ;
			table[CTI(ch)]++ ;
		}
		else if (IsOpposed(str[i])) //opposed
		{
			memset (table, 0, sizeof (table)) ;
			cnt = 0 ;
		}
		else
		{
			stack[cnt++] = str[i] ;
			table[CTI(str[i])] ++ ;
		}
	}
	for (i = 0 ; i < cnt ; i++)
		rtn += stack [i] ;
	return rtn ;
//	return vec ;
}



int main ()
{
	int i, T, Case ;
	int C, D, N ;
	char str[1000] ;
	string buff ;
	string result ;
	freopen ("B.in", "r", stdin) ;
	freopen ("b.txt", "w", stdout) ;
	
	
	scanf ("%d", &T) ;
	for (Case = 1 ;  Case <= T ; Case ++)
	{
		memset (table, 0, sizeof (table)) ;
		memset (opposed, 0, sizeof (opposed)) ;
		memset (combine, 0, sizeof (combine)) ;
		scanf ("%d", &C) ;
		for (i = 0 ; i < C ; i++)
		{
			scanf ("%s", str) ;
			combine[CTI(str[0])][CTI(str[1])] = combine[CTI(str[1])][CTI(str[0])] = str[2] ; 
		}
		scanf ("%d", &D) ;
		for (i = 0 ; i < D ; i++)
		{
			scanf ("%s", str) ;
			opposed[CTI(str[0])][CTI(str[1])] = opposed[CTI(str[1])][CTI(str[0])] = 1 ;
		}

		scanf ("%d", &N) ;
		scanf ("%s", str) ;
		result = work (str, N) ;
		

		printf ("Case #%d: [", Case) ;
		for (i = 0 ; i < result.length() ; i++)
		{
			if (i != 0) printf (", ") ;
			printf ("%c", result[i]) ;
		}
		printf ("]\n") ;
	}
	
	return 0 ;
}