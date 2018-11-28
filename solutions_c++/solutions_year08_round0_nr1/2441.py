#include <iostream>
#include <string>
using namespace std;

// sets 0 (resets) array
void clearTab( int* tab, int size )
{
	for( int p=0; p<size; p++) tab[p] = 0;
}

int main()
{
	int n;
	cin >> n;
//cout << n << endl;
std::cin.ignore( std::numeric_limits<std::streamsize>::max(), '\n' );

	for( int q=0; q<n; q++ )
	{
		int num_se;
		cin >> num_se;

//cout << num_se << endl;
std::cin.ignore( std::numeric_limits<std::streamsize>::max(), '\n' );

		int required_switches = 0;

		//char **se = new char*[num_se];
		string *se = new string[num_se];
		int *se_usage = new int[num_se];
		
		// get search engines
		for( int z = 0; z<num_se; z++ )
		{
			string se_name;
			//char se_name[101];
			//cin >> se_name;
			
			std::getline( cin, se_name, '\n' );

		
			se[z] = se_name;
			//se[z] = new char[ strlen(se_name) ];
			//strcpy( se[z], se_name );
			//cout << se[z] << endl;
		} 
			
		// clear table (initial)
		clearTab( se_usage, num_se );

		//cout << se_usage[0] << endl;
 
		int num_w;
		cin >> num_w;
std::cin.ignore( std::numeric_limits<std::streamsize>::max(), '\n' );


		// get words
		//cout << "W: " << num_w << endl;
		//if( num_w > 0)
		for( int j=0; j<num_w; j++)
		{
			//if( num_w == 0 ) break; 

			//char word[101];
			string keyword;
			getline( cin, keyword );
//cout << keyword << endl;
			//char *keyword = new char[ strlen(word) ];
			//strcpy( keyword, word );

			int last_u = -1;

			// check browser names
			for( int u=0; u<num_se; u++ )
			{	
				// compare names
				if( se[u] == keyword ) {se_usage[u]++; last_u = u; }
			}
	
			bool all_used = true;			
//cout << "s #" << j << " -> ";

			// all se were used?
			for( int u=0; u<num_se; u++ )
			{ //cout << se_usage[u] << " ";
				if( se_usage[u] == 0 )
				{
					all_used = false;
					//break;
				}
			}

//	if( q == 19 && j == 53 ) { cout << (se_usage[0] == 0) ;cout << endl << se[0] << endl; }

			if( (all_used == true) /*&& (q < n-1)*/ )
			{
				required_switches++;
				
				//cout << " ! SW ! ";
				
				clearTab(se_usage, num_se);
				se_usage[last_u]++;
			} 
//cout << endl;
		}

		cout << "Case #" << q+1 << ": " << required_switches << endl;
	}
 
	return 0;
}
