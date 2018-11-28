#include <iostream>
#include <fstream>

using namespace std;
int main()
{
	ifstream fin("inputl.in");
	ofstream fout("output.txt");
	int l,d,n;
	fin >> l >> d >> n;
	char c[10];
	fin.getline(c,10);
	char words[5010][20]={};
	int let[15][30];
	for(int i=0;i<d;i++)
			fin.getline(words[i],20);
	char s[450]={};
	for(int cases=0;cases<n;cases++)
	{
		fin.getline(s,450);
		int count=0;
		for(int i=0;i<d;i++)
		{
			int k=0;
			bool can=true;
			for(int j=0;j<l;j++)
			{
				if ((s[k]!='(')&&(s[k]!=words[i][j]))
					{
						can=false;
						break;
					}
				else
					if (s[k]=='(')
					{
						bool is=false;
						while (s[k]!=')')
						{
							k++;
							if(s[k]==words[i][j])
							{
								is=true;
							}
						}
						k++;
						can=is;
					}else
						k++;
				if (!can)
					break;
			}	
			if (can)
				count++;
		}
		fout << "Case #" << cases+1 << ": " << count << "\n";
	}
	fin.close();
	fout.close();
	return 0;
}
