#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	int caseNum=1;
	ifstream fin("A-small-attempt2.in");
	ofstream fout("A-small.out");
	int cnt;
	fin >> cnt;//////////
	while(cnt-- > 0)
	{
		int N,pd,pg;
		fin >> N >> pd >> pg;
		string s;
		if(pg==100 && pd!=100)
			s="Broken";
		else if(pg==0 && pd!=0)
			s="Broken";
		else
		{
			if(N>=100 || pd==0 || pd==100)
				s="Possible";
			else
			{
				for(int i=1;i<=N;i++)
				{
					int d;
					d=pd*i%100;
					if(d==0)
					{
						s="Possible";
						break;
					}
					else
						s="Broken";
				}
			}
		}
		fout << "Case #" << caseNum++ << ": " << s << endl;
	}
} 