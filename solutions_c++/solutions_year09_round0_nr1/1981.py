#include <fstream>
#include <vector>
#include <cstring>

using namespace std;

int main()
{
	ifstream dat("a-small.in");
	ofstream sol("a-small.out");
	int l,d,n,i,j;
	dat >> l >> d >> n;
	char words[5001][16]={0};
	for(i=0;i<d;i++)
	{
		dat >> words[i];
	}
	char a,line[10000]={0};
	for(int t=0;t<n;t++)
	{
		dat >> line;
		vector < vector <char> > let;
		let.clear();
		int cur=-1;
		for(i=0;i<strlen(line);i++)
		{
			if (line[i]=='(')
			{
				cur=let.size();
				let.push_back(vector<char>());
				continue;
			}	
			if (line[i]==')')
			{
				cur=-1;
				continue;
			}
			if (cur==-1)
			{
				let.push_back(vector <char>());
				let[let.size()-1].push_back(line[i]);	
			}
			else
			{
				let[cur].push_back(line[i]);
			}	
		}
		bool possible[5001]={0};
		for(i=0;i<d;i++)
		{
			for(j=0;j<l;j++)
			{
				bool fdg=true;
				for(int jj=0;jj<let[j].size();jj++)
				{
					if (let[j][jj]==words[i][j]) fdg=false;
				}
				if (fdg) possible[i]=true;
			}
		}
		int ans=0;
		for(i=0;i<d;i++)
		{
			if (!possible[i]) ans++;
		}	
		sol << "Case #" << t+1 << ": " << ans << endl;
	}
	return 0;
}