               
#include<iostream>
#include<iomanip>
#include<list>

using namespace std;

int main()
{
	list<long> a1,a2,b1,b2 ;
	list<long>::iterator ita , itb ; 
	long N, A, B, turna , i,j ,hr , min ,a , b;
	char colon;
	
	
	cin >> N;
	
	for(i =0 ;i< N ;i++)
	{
		cin >> turna;
		cin >> A>>B ;

		
		a1.clear();a2.clear();b1.clear();b2.clear();

		
		for ( j = 0 ;j< A ;j++)
		{
			cin >> setw(2) >> hr >> setw(1) >> colon >> setw(2) >> min ;
			a1.insert (a1.begin() ,hr*60 + min);
			cin >> setw(2) >> hr >> setw(1) >> colon >> setw(2) >> min ;
			a2.insert (a2.begin() ,hr*60 + min + turna);
		}
		
		for ( j = 0 ;j< B ;j++)
		{
			cin >> setw(2) >> hr >> setw(1) >> colon >> setw(2) >> min ;
			b1.insert (b1.begin() ,hr*60 + min);
			cin >> setw(2) >> hr >> setw(1) >> colon >> setw(2) >> min ;
			b2.insert (b2.begin() ,hr*60 + min+ turna);
		}

		a1.sort();
		a2.sort();
		b1.sort();
		b2.sort();

		a = a1.size() ;

		ita = a1.begin();
		itb = b2.begin(); 
		
		
		while ( ita != a1.end())
		{
			if (itb != b2.end() &&  *itb <= *ita ) {
				--a;
				itb++;
			}
			ita++;
		}

		b = b1.size() ;

		ita = a2.begin() ; 
		itb = b1.begin() ; 
		
		while ( itb != b1.end())
		{
			if ( ita != a2.end() &&  *ita <= *itb ) {
				--b;
				ita++;
			}
			itb++;
		}

		cout << "Case #" << i+1 << ": " << a << " " << b << endl;
	}

	return 0;
}