# include<iostream>
# include<fstream>
# include<vector>
# include<algorithm>
# include<set>
using namespace std;
# define FOR(i,a,n) for(int i=a;i<n;++i)
# define REP(i,n) FOR(i,0,n)
ifstream fin("B-large.in");
ofstream fout("out.txt");
typedef long long LL;
char ar[100][100];
bool opp[100][100];
int main()
{
	int tc;
	fin>>tc;
	int cnt=0;
	while(tc--)
	{
		++cnt;
		int c;
		fin>>c;
		REP(i,100) REP(j,100) ar[i][j]='.';
		memset(opp,false,sizeof(opp));
		REP(i,c)
		{
			char p,q,r;
			fin>>p>>q>>r;
			ar[p-'A'][q-'A']=r;
			ar[q-'A'][p-'A']=r;
		}
		int d;
		fin>>d;
		REP(i,d)
		{
			char p,q;
			fin>>p>>q;
			opp[p-'A'][q-'A']=1;
			opp[q-'A'][p-'A']=1;
		}
		vector<char> v;
		int n;
		fin>>n;
		int si=0;
		REP(i,n)
		{
			char p;
			fin>>p;
			if(!si) 
			{
				v.push_back(p);
				++si;
			}
			else
			{
				char ch=ar[p-'A'][v[si-1]-'A'];
				if(ch!='.')
				{
					v.pop_back();
					v.push_back(ch);
				}
				else
				{
					v.push_back(p);
					++si;
				}
				if(ch=='.') ch=p;
				bool ok=true;
				REP(j,si) 
				if(opp[ch-'A'][v[j]-'A'])
				{
					ok=false;
					break;
				}
				if(!ok)
				{
					while(si) 
					{
						v.pop_back();
						--si;
					}
				}
			}
		}
		fout<<"Case #"<<cnt<<": [";
		if(si)
		{
			REP(i,si-1) fout<<v[i]<<", ";
			fout<<v[si-1];
		}
		fout<<"]"<<endl;
	}
}
			
	
	
	

