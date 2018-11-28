#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
	fstream fin;
	fstream fout;
	fin.open("a.in");
	fout.open("a.out", ios_base::app);
	//
    int l,d,n;
	fin >> l;
	fin >> d;
    fin >> n;
	vector<string> dir;
	vector<string> word;

	for(int i=0; i<d; i++)
	{
		string w;
		fin >> w;
		dir.push_back(w);
	}

    for(int i=0; i<n; i++)
    {
        string now;
		fin >> now;
		int res=0;
		for(int k=0; k<d; k++)
		{
			int token=0;
			int j=0;
			bool ok=1;
			while(j<now.length())
			{
				if(now[j]=='(')
				{
					int end;
					end=now.find(')', j+1);
					string ss;
					ss=now.substr(j,end-j);
					size_t found;
					found=ss.find(dir[k][token]);
					if(found==string::npos)
					{
						ok=0;
						break;
					}
					j=end+1;
				}
				else
				{
					if(dir[k][token]!=now[j])
					{
						ok=0;
						break;
					}
					j++;
				}
				token++;
			}
			if(ok)
				res++;
		}
        fout << "Case #" << i+1 << ": " << res << endl;
    }
	//
    fin.close();
	fout.close();
    return 0;
}
