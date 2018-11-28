#include <fstream>
using namespace std;
ifstream fin("input.txt");
ofstream fout("output.txt");

int n,m;
int a[200][2], b[200][2];
int i, j;
int pos1, pos2;

bool process()
{
	if(i == n && j == m)
		return false;
	if(i == n)
	{
		if(pos2 == b[j][0])
			++j;
		else if(pos2 < b[j][0])
			++pos2;
		else
			--pos2;

		return true;
	}

	if( j == m )
	{
		if(pos1 == a[i][0])
			++i;
		else if(pos1 < a[i][0])
			++pos1;
		else
			--pos1;

		return true;
	}

	if(a[i][1] < b[j][1])
	{
		if(pos1 == a[i][0])
			++i;
		else if(pos1 < a[i][0])
			++pos1;
		else
			--pos1;

		if(pos2 < b[j][0])
			++pos2;
		else if(pos2 > b[j][0])
			--pos2;

		return true;
	}

	if(pos1 < a[i][0])
		++pos1;
	else if(pos1 > a[i][0])
		--pos1;

	if(pos2 == b[j][0])
		++j;
	else if(pos2 < b[j][0])
		++pos2;
	else 
		--pos2;

	return true;
}

int main()
{
	char ch;
	int k,l;
	int t,caseN;
	fin>>t;


	for(caseN = 1; caseN <=t; ++caseN)
	{
		n=0;
		m=0;
		fin>>k;
		for(l=1; l<=k; ++l)
		{
			fin>>ch;
			if(ch == 'O')
			{
				fin>>a[n][0];
				a[n][1]=l;
				++n;
			}
			else
			{
				fin>>b[m][0];
				b[m][1]=l;
				++m;
			}
		}
		
		int ans=0;
		i = j = 0;
		pos1 = pos2 = 1;
		while(process())
			++ans;
		fout<<"Case #"<<caseN<<": "<<ans<<endl;
	}

	return 0;
}