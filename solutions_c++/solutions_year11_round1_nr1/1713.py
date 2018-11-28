#include<iostream>
#include <fstream>
using namespace std;

ifstream fin("D:\\acm\\pa\\A-small-attempt5.in");
ofstream fout("D:\\acm\\pa\\A-small-attempt5.out");
#define cin fin
#define cout fout

int main()
{
	int t;
	double i , j;
	//double ig , jg;
	double n , pd , pg;
	bool ans;
	int cas = 0;
	cin>>t;
	while( t-- )
	{
		cas++;
		cin>>n>>pd>>pg;
		pd /= 100.0;
		pg /= 100.0;
		ans = false;
		if( ( pg == 0.0 && pd != 0.0 ) || ( pg != 0.0 && pd == 0.0 ) )
		{
			cout<<"Case #"<<cas<<": ";
			cout<<"Broken"<<endl;
			continue;
		}
		if( pd == 0.0 )
		{ 
			cout<<"Case #"<<cas<<": ";
			cout<<"Possible"<<endl;
			continue;
		}
		
		for( i = n ; i > 0.0 ; i -= 1.0 )
		{
			for( j = i ; j > 0.0 ; j -= 1.0 )
			{
				if( j / i == pd )
				{ break; }
				if( j / i < pd )
				{ break; }
			}
			if( j / i == pd )
			{
				
				if( pg == 1.0 && ( i - j > 0.0 || i == 0.0 ) )
				{ continue; }
				ans = true; 
			
			}
			
			if( ans == true )
			{ break; }
		}
	
		cout<<"Case #"<<cas<<": ";
		if( ans == true )
		{ cout<<"Possible"<<endl; }
		else
		{ cout<<"Broken"<<endl; }
	}
	return 0;
}