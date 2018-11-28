#include <iostream>
#include <cmath>
#include <ctime>

using namespace std;

bool comparetime(tm A, tm B, int turntime)
{
    if(A.tm_hour*60 + A.tm_min + turntime <= B.tm_hour*60 + B.tm_min )
	return true;
    else
	return false;
}

int main()
{
    int inputs;
    cin >> inputs;
    
    for( int i = 0; i < inputs; i++ )
    {
	int turntime;
	cin >> turntime;
	int train_a, train_b;
	cin >> train_a >> train_b;
	tm *arrival_a, *departure_a, *arrival_b, *departure_b;

	arrival_a = new tm[train_a];
	departure_a = new tm[train_a];
	
	arrival_b = new tm[train_b];
	departure_b = new tm[train_b];
	
	char tmp;
	for( int j = 0; j < train_a; j++ )
	{
	    cin >> departure_a[j].tm_hour;
	    cin >> tmp; 
	    cin >> departure_a[j].tm_min;
	    cin >> arrival_a[j].tm_hour;
	    cin >> tmp; 
	    cin >> arrival_a[j].tm_min;
	}
	
	for( int j = 0; j < train_b; j++ )
	{
	    cin >> departure_b[j].tm_hour;
	    cin >> tmp; 
	    cin >> departure_b[j].tm_min;
	    cin >> arrival_b[j].tm_hour;
	    cin >> tmp; 
	    cin >> arrival_b[j].tm_min;
	}

	for( int j = 0; j < (train_a - 1); j++ )
	{
	    int minimum = 100 * arrival_a[j].tm_hour + arrival_a[j].tm_min ;
	    int marker = j;
	    for( int k = j + 1; k < train_a; k++ )
	    {
		int current = 100 * arrival_a[k].tm_hour + arrival_a[k].tm_min ;
		if( minimum > current )
		{
		    minimum = current;
		    marker = k;
		}
	    }
	    if( marker != j )
	    {
		tm temptime = arrival_a[j];
		arrival_a[j] = arrival_a[marker];
		arrival_a[marker] = temptime;
	    }
	}

	for( int j = 0; j < (train_a - 1); j++ )
	{
	    int minimum = 100 * departure_a[j].tm_hour + departure_a[j].tm_min ;
	    int marker = j;
	    for( int k = j + 1; k < train_a; k++ )
	    {
		int current = 100 * departure_a[k].tm_hour + departure_a[k].tm_min ;
		if( minimum > current )
		{
		    minimum = current;
		    marker = k;
		}
	    }
	    if( marker != j )
	    {
		tm temptime = departure_a[j];
		departure_a[j] = departure_a[marker];
		departure_a[marker] = temptime;
	    }
	}


	
	for( int j = 0; j < (train_b - 1); j++ )
	{
	    int minimum = 100 * arrival_b[j].tm_hour + arrival_b[j].tm_min ;
	    int marker = j;
	    for( int k = j + 1; k < train_b; k++ )
	    {
		int current = 100 * arrival_b[k].tm_hour + arrival_b[k].tm_min ;
		if( minimum > current )
		{
		    minimum = current;
		    marker = k;
		}
	    }
	    if( marker != j )
	    {
		tm temptime = arrival_b[j];
		arrival_b[j] = arrival_b[marker];
		arrival_b[marker] = temptime;
	    }
	}

	
	for( int j = 0; j < (train_b - 1); j++ )
	{
	    int minimum = 100 * departure_b[j].tm_hour + departure_b[j].tm_min ;
	    int marker = j;
	    for( int k = j + 1; k < train_b; k++ )
	    {
		int current = 100 * departure_b[k].tm_hour + departure_b[k].tm_min ;
		if( minimum > current )
		{
		    minimum = current;
		    marker = k;
		}
	    }
	    if( marker != j )
	    {
		tm temptime = departure_b[j];
		departure_b[j] = departure_b[marker];
		departure_b[marker] = temptime;
	    }
	
	}
	int limit = 0;
	int count_a = train_a, count_b = train_b;

	for(int j = 0 ; j < train_a ; j++)
	{
	    for(int k = limit ; k < train_b ; k++)
	    {
		if (comparetime( arrival_a[j], departure_b[k], turntime)== true)
		{
		    count_b--;
		    limit = k+1;
		    break;
		} 

	    }
	}
	limit = 0;	
	for(int j = 0 ; j < train_b ; j++)
	{
	    for(int k = limit ; k < train_a ; k++)
	    {
		if (comparetime( arrival_b[j], departure_a[k], turntime)== true)
		{
		    count_a--;
		    limit = k+1;
		    break;
		} 

	    }
	}

	cout << "Case #" << ( i + 1 ) << ": " << count_a << " " << count_b << endl;
    }

    return 0;
}





