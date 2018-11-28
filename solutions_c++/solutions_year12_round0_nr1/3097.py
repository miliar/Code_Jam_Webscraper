#include <fstream>

using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("A-small-attempt0.out");

	int NUM_OF_CASES;
	char var;

	//read in;
	in >> NUM_OF_CASES;
	in.get();

	//init
	char* tran = "yhesocvxduiglbkrztnwjpfmaq";
	for( int i = 0; i < NUM_OF_CASES; i ++ )
	{
		out << "Case #" << i + 1 << ": " ;
		
		var = in.get();
		while( (var >= 97 && var <= 122 ) || ( var == ' ' ) )
		{
			
			if( var != ' ' )
			{
				out << tran[ var - 97 ];
			}else 
			{
				out << ' ';
			}
			var = in.get();
		}
		out << endl;
	}

	out.close();
	in.close();
	return 0;
}