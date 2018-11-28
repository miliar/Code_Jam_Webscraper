#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main( int argc, char*argv[])
{
    if( argc != 2 )
    {
        cout<<"Specify input file please.\n";
        return 1;
    }
    ifstream in(argv[1]);
    string sFile = argv[1];
    sFile.replace(sFile.length() - 2, 2, "out");
    ofstream out(sFile.c_str());
    string str;
    getline(in,str);
    int iTasks = atoi(str.c_str());
    for( int iCount = 1; iCount <= iTasks; iCount++ )
    {
        vector<string> vEngines;
        vector<string> vQueries;
        getline(in, str);
        int iNumEng = atoi(str.c_str());
        for( int i = 0; i < iNumEng; i++ )
        {
            getline(in, str);
            vEngines.push_back(str);
        }
        getline(in, str);
        int iNumQueries = atoi(str.c_str());
        for( int i = 0; i < iNumQueries; i++ )
        {
            getline(in, str);
            vQueries.push_back(str);
        }
        int iMin = 0;
//		if( iNumQueries == 0 )
//			iMin = 0;
//		else
		{
			vector<int> vDiff;
			vector<string>::iterator iter1 = vQueries.begin();
			vector<string>::iterator iter = vQueries.begin();
			while( iter != vQueries.end() )
			{
				vDiff.clear();
				for( int i = 0; i < (int)vEngines.size(); i++ )
				{
					if( (iter = find(iter1, vQueries.end(), vEngines[i])) == vQueries.end() )
					{
						vDiff.clear();
						break;
					}
					else
					{
						vDiff.push_back(iter - iter1);
					}
				}
				if( !vDiff.empty() )
				{
					sort(vDiff.begin(),vDiff.end());
					iMin ++;
					iter1 = iter1 + vDiff.back();
				}
			}
		}
        out<<"Case #"<< iCount <<": "<<iMin<<'\n';
    }
}

