#include <iostream>
#include <vector>

using namespace std ;

struct ttime 
{
	int min1 , min2;	
} ;

void sortaccTime (vector <ttime> &x) ;

int main ()
{
	int n ;
	int i , j;
	cin >> n ;
	for (i = 0 ; i < n ; i++)
	{
		int turn ;
		cin >> turn ;
		int nA , nB	;
		cin >> nA >> nB ;
		vector <ttime> A2B , B2A;
		for (j = 0 ; j < nA ; j++)
		{
			int h1 , m1 , h2 , m2;
			scanf ("%d:%d %d:%d" , &h1 , &m1 , &h2 , &m2) ;
			ttime temp ;
			temp.min1 = m1 + h1 * 60;
			temp.min2 = m2 + h2 * 60;
			A2B.push_back(temp)	;
		}
		for (j = 0 ; j < nB ; j++)
		{
			int h1 , m1 , h2 , m2;
			scanf ("%d:%d %d:%d" , &h1 , &m1 , &h2 , &m2) ;
			ttime temp ;
			temp.min1 = m1 + h1 * 60;
			temp.min2 = m2 + h2 * 60;
			B2A.push_back(temp)	;
		}
		if (nA == 0 || nB == 0)
		{
			cout << "Case #" << (i + 1) << ": " << nA << " " << nB << endl ;
			continue ;
		}
		sortaccTime (A2B) ;
		sortaccTime (B2A) ;
		int nt1 = 0 , nt2 = 0;
		ttime temp ;
		while (true)
		{
			
			if (A2B.size() > 0 && B2A.size() > 0)
			{
				if (A2B[0].min1 < B2A[0].min1)
				{
					nt1 ++ ;
					temp = A2B[0] ;
					A2B.erase(A2B.begin());
					int m ;
					m = temp.min2 + turn ;
					
					while (true)
					{
						bool noA = true , noB = true ;
						for (j = 0 ; j < B2A.size() ; j++)
						{
							if (B2A[j].min1 >= m)
							{
								noB = false ;
								m = B2A[j].min2 + turn ;
								B2A.erase (B2A.begin() + j) ;
								break ;	
							}	
						}
						if (noB)
						{
							break ;
						}
						for (j = 0 ; j < A2B.size() ; j++)
						{
							if (A2B[j].min1 >= m)
							{
								noA = false ;
								m = A2B[j].min2 + turn ;
								A2B.erase (A2B.begin() + j)	 ;
								break ;
							}
						}
						if (noA)
							break ;	
					}
				}
				else
				{
					nt2 ++ ;
					temp = B2A[0] ;
					B2A.erase(B2A.begin());
					int m ;
					m = temp.min2 + turn ;
										
					while (true)
					{
						bool noA = true , noB = true ;
					
						for (j = 0 ; j < A2B.size() ; j++)
						{
							if (A2B[j].min1 >= m)
							{
								noA = false ;
								m = A2B[j].min2 + turn ;
								A2B.erase (A2B.begin() + j)	 ;
								break ;
							}
						}
						if (noA)
							break ;	
						for (j = 0 ; j < B2A.size() ; j++)
						{
							if (B2A[j].min1 >= m)
							{
								noB = false ;
								m = B2A[j].min2 + turn ;
								B2A.erase (B2A.begin() + j) ;
								break ;	
							}	
						}
						if (noB)
						{
							break ;
						}
					}
				}
			}
			else if (A2B.size() == 0 && B2A.size() == 0)
				break ;
			else if (A2B.size() == 0)
			{
				nt2 += B2A.size();
				break ;
					
			}
			else if (B2A.size() == 0)
			{
				nt1 += A2B.size();
				break ;
			}
		}
		cout << "Case #" << (i + 1) << ": " << nt1 << " " << nt2 << endl ;
	}
	return 0 ;	
}

void sortaccTime (vector <ttime> &x)
{
	int i , j ;
	int N = x.size() ;
	for (i = 0 ; i < N ; i++)	
	{
		for (j = N - 1 ; j >= i + 1 ; j--)
		{
			if (x[j - 1].min1 > x[j].min1)
				swap (x[j - 1] , x[j]) ;
		}	
	}
}
