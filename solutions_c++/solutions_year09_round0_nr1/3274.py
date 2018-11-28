#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

int main()
{

	int L,D,N;
	FILE* stream = fopen("output.out", "w");
	char str[1024];
	int i,j;
	vector<string> vec;
	set<string> cp;

	scanf("%d %d %d",&L,&D,&N);
	for(i=0;i < D;i++)
	{
		scanf("%s",str);
		vec.push_back(str);
	}
				

	for(i=1;i<= N; i++)
	{
		scanf("%s",str);
		string s = str;
		int pos=0;
		cp.clear();
		while(pos < L)
		{
			if(s[0] == '(')
			{
				int rpos = s.find_first_of(")");
				string tmp = s.substr(1,rpos-1);
				for(j=0; j < vec.size();j++)
				{
					if(tmp.find(vec[j].substr(pos,1).c_str()) == string::npos)
						cp.insert(vec[j]);
				}
				s = s.substr(rpos+1,s.size()-1);
			}
			else
			{
				for(j=0; j < vec.size();j++)
					if(vec[j].substr(pos,1).compare(s.substr(0,1)) != 0)
						cp.insert(vec[j]);
				s = s.substr(1,s.size()-1);
			}

			pos++;
		}

		fseek(stream,0L,SEEK_END);
		fprintf(stream,"Case #%d: %d\n",i,vec.size()-cp.size());

	}

	fclose(stream);

	return 0;
}