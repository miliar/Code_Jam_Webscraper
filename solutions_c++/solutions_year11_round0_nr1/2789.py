#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int j=0; j<T; ++j)
	{
		vector<int> O, B, seq;
		int n;
		cin >> n;
		int op=1, bp=1;
		for(int i=0; i<n; ++i)
		{
			string s;
			int pos;
			cin >> s >> pos;
			if(s=="O")
			{
				O.push_back(pos);
				seq.push_back(1);
			}else{
				B.push_back(pos);
				seq.push_back(2);
			}
		}	
		int ans=0;
		int ol=0, bl=0;
		int Oto=0;
		if(O.size()>0) Oto=O[ol++];
		int Bto=0;
		if(B.size()>0) Bto=B[bl++];
		for(int i=0; i<n; ++i)
		{
			int hod=seq[i];
			int step=0;
			if(hod==1)
			{
				step=abs(op-Oto)+1;
				op=Oto;
				if(ol<O.size())Oto=O[ol++];
				if(bp<Bto) bp+=min(step,abs(bp-Bto));
				else bp-=min(step,abs(bp-Bto));
			}else{
				step=abs(bp-Bto)+1;
				bp=Bto;
				if(bl<B.size())Bto=B[bl++];				
				if(op<Oto) op+=min(step,abs(op-Oto));
				else op-=min(step,abs(op-Oto));
			}
			//printf("%d %d %d %d\n",hod,step,bp,Bto);
			ans+=step;
		}
		printf("Case #%d: %d\n",j+1,ans);
	}
	
	return 0;
}
