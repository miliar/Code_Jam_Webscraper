#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int getalval(char ch, char * lang);
	const char INFILE_NAME[]        = "in.in";
	const char OUTFILE_NAME[]       = "gcj.Out";

	ifstream fin;						// Input file
    ofstream fout;						// Output file

int main()
{
	fout.open(OUTFILE_NAME, ios::out);

	if (fout)
	{
		fin.open(INFILE_NAME, ios::in);
	}
	int x;
	fin >> x;
	int cases = x;
	//cout << "num cases is " << cases << endl;

	// process each case
	for( int i = 0; i < cases; i++ )
	{
		int switches = 0;
		fin >> x;
		int senum = x;
		fin.ignore(100,'\n');
		//cout << "num search engines is " << senum << endl;

		string senames[100];
		for( int j = 0; j < senum; j++ )
		{
			string name;
			getline (fin,name);
			senames[j] = name;
			//cout << "\tse named " << senames[j] << endl;
		}

		fin >> x;
		int qnum = x;
		//cout << "num queries is " << qnum << endl;
		fin.ignore(100,'\n');

		int found[100];
		for( int j = 0; j < senum; j++ )
		{
			found[j] = 0;
		}

		// process queries
		for( int j = 0; j < qnum; j++ )
		{
			int current;
			string query;
			getline (fin,query);
			//cout << "query is " << query << endl;
			for( int k = 0; k < senum; k++ )
			{
				if ( query == senames[k] )
				{
					found[k] = 1;
					current = k;
				}
			}

			int sum = 0;
			for( int k = 0; k < senum; k++ )
			{
				sum += found[k];
			}

			// need to switch
			if( sum == senum )
			{
				switches++;	
				for( int k = 0; k < senum; k++ )
				{
					found[k] = 0;
				}
				//cout << "switched!" << endl;
				found[current] = 1;
			}
		}
		cout << "Case #" << i+1 << ": " << switches << endl;
		fout << "Case #" << i+1 << ": " << switches << endl;
	}


	//char aliennum[5];
	//char sourcelang[11];
	//char targetlang[11];
	//char bwans[25];
	//char ans[25];
	//for( int i = 0; i < num; i++ )
	//{
	//	//cout << "Case #" << i+1 << ": ";
	//	fout << "Case #" << i+1 << ": ";
	//	fin >> aliennum;
	//	int numlen = strlen(aliennum);
	//	cout << aliennum << endl;

	//	fin >> sourcelang;
	//	int sourcelen = strlen(sourcelang);
	//	cout << sourcelang << endl;

	//	fin >> targetlang;
	//	int targetlen = strlen(targetlang);
	//	cout << targetlang << endl;

	//	int dec = 0;
	//	for( int c = 0; c < numlen; c++ )
	//	{
	//		dec *= sourcelen;
	//	//	cout << "1 " << dec << endl;
	//		dec += getalval(aliennum[c],sourcelang);
	//	//	cout << "2 " << dec << endl;
	//	}
	//	//cout << "dec is " << dec << endl;
	//	int l = 0;
	//	while( dec != 0 )
	//	{
	//		int rem = dec%targetlen;
	//		dec = dec/targetlen;
	//		bwans[l++] = targetlang[rem];
	//	}
	//	bwans[l] = '\0';
	//	
	//	int anslen = strlen(bwans);
	//	for( int d = 0; d < anslen; d++ )
	//	{
	//		ans[d] = bwans[anslen-1-d];
	//	}
	//	ans[anslen] = '\0';
	//	//cout << ans << endl;
	//	fout << ans << endl;
	//}


	if (fin)
	{
		fin.close();
	}
	fout.close();

}

int getalval(char ch, char * lang)
{
	int x;
	for( x = 0; x < strlen(lang); x++ )
	{
		if( ch == lang[x] )
			return x;
	}
	return 0;
}