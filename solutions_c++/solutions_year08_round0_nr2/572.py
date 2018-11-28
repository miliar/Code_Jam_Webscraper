#include<iostream>
#include<algorithm>

using namespace std ;

struct train
{
	int dep ;
	int arr ;
} ja[200] , jb[200] ;

int comp1(const void *a , const void *b)
{
	if(((train*)a)->arr < ((train*)b)->arr)
		return -1 ;
	if(((train*)a)->arr == ((train*)b)->arr)
		return 0 ;
	return 1 ;
}

int comp0(const void *a , const void *b)
{
	if(((train*)a)->dep < ((train*)b)->dep)
		return -1 ;
	if(((train*)a)->dep == ((train*)b)->dep)
		return 0 ;
	return 1 ;
}

int main()
{
	int tcase , c , i , j , na , nb , a , b , x , y , t ;
	char ch ;

	freopen("1.txt" , "r" , stdin) ;
	freopen("2.txt" , "w" , stdout) ;

	cin >> tcase ;
	for(c = 1 ; c <= tcase ; c++)
	{
		cin >> t >> na >> nb ;

		for(i = 0 ; i < na ; i++)
		{
			cin >> x >> ch >> y ;
			ja[i].dep = x * 60 + y ;
			cin >> x >> ch >> y ;
			ja[i].arr = x * 60 + y ;
		}

		for(i = 0 ; i < nb ; i++)
		{
			cin >> x >> ch >> y ;
			jb[i].dep = x * 60 + y ;
			cin >> x >> ch >> y ;
			jb[i].arr = x * 60 + y ;
		}

		qsort(jb , nb , sizeof(train) , comp1) ;
		qsort(ja , na , sizeof(train) , comp0) ;
		a = na ;
		for(i = 0 , j = 0 ; i < na && j < nb ; i++)
		{
			if(jb[j].arr + t <= ja[i].dep)
			{
				a-- ;
				j++ ;
			}
		}

		qsort(ja , na , sizeof(train) , comp1) ;
		qsort(jb , nb , sizeof(train) , comp0) ;
		b = nb ;
		for(i = 0 , j = 0 ; i < nb && j < na ; i++)
		{
			if(ja[j].arr + t <= jb[i].dep)
			{
				b-- ;
				j++ ;
			}
		}

		cout << "Case #" << c << ": " << a << " " << b << "\n" ;
	}
}