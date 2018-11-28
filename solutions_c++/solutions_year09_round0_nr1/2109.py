#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstring>
#include <fstream>
#define M 5001
using namespace std;


int main()
{
	fstream f1("A-small-attempt1.in");
	ofstream f2("xue1.txt");
	int L, D, N;
	f1>>L>>D>>N;

	int i,j,k,sz = 0;
	vector<string> dic;
	vector<int> sck, ck;

	string tmpdic, pat;
	for( i = 0; i < D; i++)
	{
		f1>>tmpdic;
		dic.push_back(tmpdic);
		sck.push_back( i );
//		sz++;
	}
	int l = 0;

	vector<int> res;
	for( i = 0; i < N; i++)
	{
		f1>> pat;
		ck = sck;
		for( l = 0; l < L; l++ )
		{
			vector<int> tck(ck);
			ck.clear();
//			sz = 0;

			if( pat[0] != '(' )
			{
				for( j = 0; j < tck.size(); j++ )
				{
					if( dic[tck[j]][l] == pat[0] )
					{
						ck.push_back( tck[j] );
//						sz++;
					}
				}
				pat = pat.substr( 1 );
			}
			else
			{
				int pos1 = pat.find('(');
				int pos2 = pat.find(')');
				for( j = 0; j < tck.size(); j++ )
				{
					for( int k = pos1+1; k < pos2; k++)
					{
						if( dic[tck[j]][l] == pat[k] )
						{
							ck.push_back( tck[j] );
	//						cout<<"r: "<<tck[j]<<endl;
	//						sz++;
							break;
						}
					}
				}
				pat = pat.substr( pos2 + 1 );
			}
		}
//		cout<<"Case #"<<i+1<<":"<<" "<<ck.size()<<endl;
		res.push_back( ck.size() );

	}

	for( i = 0 ; i < N; i++ )
	{
		f2<<"Case #"<<i+1<<":"<<" "<<res[i]<<endl;
	}
}

