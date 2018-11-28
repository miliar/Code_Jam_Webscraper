#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	int n;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>n;
	for(int i=0; i<n; i++)
	{
		string b[4];
		string ans="";
		for(int j=0; j<4; j++)
		{
			cin>>b[j];
		}
		bool win=false;
		for(int j=0; j<4; j++)
		{
			int c=0;
			char ch;
			if(b[j][0]=='T') ch=b[j][1];
			else ch=b[j][0];
			for(int z=0; z<4; z++)
			{
				if(ch!='.'&&b[j][z]==ch||b[j][z]=='T')
					c++;
			}
			if(c==4) { ans+=ch; ans+=" won"; win=true; break;}
			c=0;
			if(b[0][j]=='T') ch=b[1][j];
			else ch=b[0][j];
			for(int z=0; z<4; z++)
			{
				if(ch!='.'&&b[z][j]==ch||b[z][j]=='T')
					c++;
			}
			if(c==4) { ans+=ch; ans+=" won"; win=true; break;}
		}
		if(!win)
		{
			int c=0;
			char ch;
			if(b[0][0]=='T') ch=b[1][1];
			else ch=b[0][0];
			for(int j=0; j<4; j++)
			{
				if(ch!='.'&&b[j][j]==ch||b[j][j]=='T')
					c++;
			}
			if(c==4) { ans+=ch; ans+=" won"; win=true;}
			if(!win)
			{
				c=0;
				if(b[0][3]=='T') ch=b[1][2];
				else ch=b[0][3];
				for(int j=0; j<4; j++)
				{
					if(ch!='.'&&b[j][3-j]==ch||b[j][3-j]=='T')
						c++;
				}
				if(c==4) { ans+=ch; ans+=" won"; win=true;}
				if(!win)
				{
					bool dr=true;
					for(int j=0; j<4; j++)
					{
						for(int z=0; z<4; z++)
							if(b[j][z]=='.')
								dr=false;
					}
					if(dr)
						ans="Draw";
					else
						ans="Game has not completed";
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
}