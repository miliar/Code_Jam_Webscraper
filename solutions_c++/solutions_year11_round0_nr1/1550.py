# include <stdio.h>
# include <vector>


using namespace std ;


typedef struct {
	char id ;
	int begin, end ;
	int t ;
} NODE;


int MAX(int a, int b){return a > b ? a : b ;}
int ABS(int a, int b){ return (a > b) ? (a-b) : (b-a) ;}
int positive (int a, int b){ return (a > b) ? (a - b) : 0 ;}


int calc (vector <NODE> vec)
{
	int pos1 = 1, pos2 = 1, t = 0, i ;
	int last1 = 0, last2 = 0 ;


	for (i = 0 ; i < vec.size() ; i++)
	{
		if (vec[i].id == 'O')
		{
			last1 = positive (ABS(pos1, vec[i].begin), last2) + vec[i].t ;
			t += last1 ;
			pos1 = vec[i].end ;
		}
		if (vec[i].id == 'B')
		{
			last2 = positive (ABS(pos2, vec[i].begin), last1) + vec[i].t;
			t += last2  ;
			pos2 = vec[i].end ;
		}
	}
	return t ;
}
int main ()
{
	int T, n, Case = 1, num, i ;
	char c ;
	NODE node ;
	vector <NODE> vec ;

	freopen("ain.txt", "r", stdin) ;
	freopen ("aout.txt", "w", stdout) ;
	scanf ("%d", &T) ;
	getchar () ;
	while (T--)
	{
		vec.clear() ;
		scanf ("%d", &n) ;
		scanf (" %c %d", &c, &num) ;
		node.begin = node.end = num ;
		node.t = 1 ;
		node.id = c ;
		vec.push_back(node) ;

		for (i = 1 ; i < n ; i++)
		{
			scanf (" %c %d", &c, &num) ;
			if (c == node.id)
			{
				node.t += ABS(node.end, num) + 1 ;
				node.end = num ;
				vec.pop_back() ;
				vec.push_back(node) ;
			}
			else
			{
				node.t = 1 ;
				node.begin = node.end = num ;
				node.id = c ;
				vec.push_back(node) ;
			}
		}
		printf ("Case #%d: %d\n", Case++, calc (vec)) ;
	}
	fclose (stdin) ;
	fclose (stdout) ;
	return 0 ;
}
