#include <iostream>
#include <vector>

using namespace std ;

int main ()
{
	int N ;
	cin >> N ;
	int i , j , k , l;
	vector <int> ans ;
	for (i = 0 ; i < N ; i++)
	{
		int nSE ; 
		cin >> nSE ;
		vector <string> SE ;
		char buffer[102];
		cin.clear();
		cin.ignore();
		for (j = 0 ; j < nSE ; j++)
		{
			
			cin.getline(buffer , 101);
			SE.push_back (buffer);
		}
		int nQ ; 
		cin >> nQ ;
		cin.clear();
		cin.ignore();
		vector <string> Q ;
		for (j = 0 ; j < nQ ; j++)
		{
			cin.getline(buffer , 101);
			Q.push_back (buffer);
		}
		
		vector <int> poss (nSE , -1) ;
		for (j = 0 ; j < nSE ; j++)
		{
			for (k = 0 ; k < nQ ; k++)
			{
				if (Q[k] == SE[j])	
				{
					poss[j] = k ;
					break ;
				}
			}
		}
		
		bool goOut = false ;
		int max = -1 ;
		for (j = 0; j < nSE ; j++)
		{
			if(poss[j] == -1)
			{	
				//cout << "D" ;
				ans.push_back (0);
				goOut = true ;
				break ;
			}
			else if (poss[j] > max)
				max = poss[j];
		}
		if (goOut)
			continue ;
		int flips = 0 ;	
		string curr = Q[max];
		for (j = 0 ; j < nQ ; j++)
		{
			if (Q[j] != curr)
				continue ;
			//cout << "Changing at " << j << " " << Q[j] <<endl ;
			flips++ ;
			for (k = 0 ; k < nSE ; k++)
			{
				poss[k] = -1 ;	
			}
			for (k = 0 ; k < nSE ; k++)
			{
				for (l = j; l < nQ ; l++)
				{
					if (Q[l] == SE[k])	
					{
						poss[k] = l ;
						break ;
					}
				}
			}
			max = -1 ;
			for (k = 0; k < nSE ; k++)
			{
				if(poss[k] == -1)
				{	
					goOut = true ;
					break ;
				}
				else if (poss[k] > max)
					max = poss[k];
			}
			if (goOut)
				break ;
			curr = Q[max];
		}
		ans.push_back (flips);
	}
	
	for (i = 0 ; i < N ; i++)
	{
		cout << "Case #" << (i + 1) << ": " << ans[i] << endl ;
	}
	return 0 ;	
}
