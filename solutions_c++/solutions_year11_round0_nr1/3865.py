#include <fstream>
#include <cstdio>
#include <vector>
#define ms(a) memset(a,0,sizeof(a))
#define fori(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
vector<int> ovec;
vector<int> bvec;
int m[101][3];
int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int T,N,k,res,oprpos,bprpos,action,opurpose,bpurpose;
	in>>T;
	char c;
	fori(i,1,T)
	{
		
		in>>N;
		ms(m);
		res=0;
		fori(g,1,N)
		{
			in>>c;
			in>>k;
			if(c=='O')
				m[g][1]=k,ovec.push_back(k);
			else
				m[g][2]=k,bvec.push_back(k);
		}
		ovec.push_back(0);
		bvec.push_back(0);
		oprpos=1;
		bprpos=1;
		opurpose=ovec[0];
		bpurpose=bvec[0];
		int op=0;
		int bp=0;
		fori(g,1,N)
		{
			action=0;
			if(m[g][1])
			{
				if(m[g][1]>=oprpos)
					action=m[g][1]-oprpos+1;
				else
					action=oprpos-m[g][1]+1;
				oprpos=opurpose;
				opurpose=ovec[++op];
				if(bpurpose && bpurpose-bprpos)
				{
					if(bpurpose>bprpos)
					{
						if(bpurpose-bprpos>=action)
							bprpos+=action;
						else
							bprpos=bpurpose;
					}
					else
					{
						if(bprpos-bpurpose>=action)
							bprpos-=action;
						else
							bprpos=bpurpose;
					}
				
				}
				res+=action;
			}
			else
			{
				if(m[g][2]>=bprpos)
					action=m[g][2]-bprpos+1;
				else
					action=bprpos-m[g][2]+1;
				bprpos=bpurpose;
				bpurpose=bvec[++bp];
				if(opurpose && opurpose-oprpos)
				{
					if(opurpose>oprpos)
					{
						if(opurpose-oprpos>=action)
							oprpos+=action;
						else
							oprpos=opurpose;
					}
					else
					{
						if(oprpos-opurpose>=action)
							oprpos-=action;
						else
							oprpos=opurpose;
					}
				
				}
				res+=action;
			}
			
		}
		out<<"Case #"<<i<<": "<<res<<endl;
			ovec.clear();
			bvec.clear();
	}
	return 0;
}