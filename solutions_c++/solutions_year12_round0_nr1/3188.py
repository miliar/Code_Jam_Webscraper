#include <fstream>

using namespace std;

int main()
{
	int n;
	char txt[102],txtmap[101];
	ifstream ifile("small.in");
	ifstream ifilemap("map");
	ofstream ofile("output");
	ifile.seekg(0,ios::beg);
	ofile.seekp(0,ios::beg);
	ifilemap.seekg(0,ios::beg);
	char map[26];
	ifile>>n;
	ifile.getline(txt,100*sizeof(char));
	for(int j = 0; j < 26; j++)
	{
		ifilemap>>map[j];
	}
	 
	for(int i = 1; i <= n; i++)
	{
		
		ifile.getline(txt,101*sizeof(char));
		int k = ifile.gcount();
		for(int j = 0; j < k; j++)
		{
			if(txt[j] != ' ')
			{
				if((int)(txt[j] - 'a') < 26)
					txtmap[j] = map[(int)(txt[j] - 'a')];
				else
					txtmap[j] = map[(int)(txt[j] - 'A')];
			}
			else txtmap[j] = ' ';
		}
		if(k>0)
		txtmap[k-1] = '\0';
		ofile<<"Case #"<<i<<": "<<txtmap<<endl;

	}
	ifile.close();
	ifilemap.close();
	ofile.close();
}