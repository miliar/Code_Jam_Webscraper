
#include <fstream>
#include <string>
using namespace std;

int main()
{
	char g_map[26]={'y','h','e','s','o','c','v','x','d','u','i','g',
			'l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int T;
	string str;
	ifstream fin("A-small-attempt2.in");
	ofstream fout("A-samll-attempt.out");
	fin>>T;
	fin.get(); 
	for(int j=0;j<T;j++)
	{
		getline(fin,str);
		//getchar();
		fout<<"Case "<<"#"<<j+1<<": ";
		for(int i=0;i<str.length();i++)
		{	
			
			if(32==str[i])fout<<" ";
			else 
			{
				fout<<g_map[str[i]-'a'];
			}
		}
		if(j<T-1)fout<<endl;

	}
	return 0;
}