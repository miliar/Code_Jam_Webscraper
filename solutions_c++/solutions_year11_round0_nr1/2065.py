#include <iostream> 
#include <cmath> 
#include <string> 
#include <cstring> 
#include <set> 
#include <map> 
#include <vector> 
#include <cstdio> 
using namespace std; 

int main(int argc, char *argv[]) 
{ 
 freopen("A.txt","r",stdin);
freopen("AOUT.txt","w",stdout);
	int tstCs = 1;
	int T = 0;
	cin >> T;
	while (T--)
	{
		int po = 1, pb = 1;
		int n;
		cin >> n;
		int time = 0;
		char c; int bt;
		vector <pair<char,int> > vp, op, bp;
		vp.clear(); op.clear(); bp.clear();
		for (int i = 0; i < n; i++)
		{
			scanf("%c%d", &c, &bt);
		    cin >> c >> bt;
			vp.push_back(make_pair(c,bt));
			if (c == 'O') op.push_back(make_pair(c,bt));
			else if (c == 'B') bp.push_back(make_pair(c,bt));
		}
		//cout << vp.size()<<" -- "<<op.size()<<" -- "<<bp.size()<<endl;
		int d1 = 0, d2 = 0;
		for (int i = 0; i < n; i++)
		{//cout<<"i=="<<i<<endl;
			pair <char,int> pci = vp[i];
			c = pci.first, bt = pci.second;
		//	cout <<"c == "<< c  <<" bt == "<< bt << endl;
			if (c == 'O')
			{
				if (po == op[d1].second)
				{
					d1++;
					if (bp.size()!=0 && pb != bp[d2].second)
						pb < bp[d2].second ? pb++ : pb--;
					time++;
				}
				else
				{
					while (po != op[d1].second)
					{	
						po < op[d1].second ? po++ : po--;
						if (bp.size()!=0 && pb != bp[d2].second)
							pb < bp[d2].second ? pb++ : pb--;
						time++;
					}
					if (bp.size()!=0 && pb != bp[d2].second)
							pb < bp[d2].second ? pb++ : pb--;
					time++;
					d1++;
				}
			}
			else
			{
				if (pb == bp[d2].second)
				{//cout<<"1"<<endl;
					d2++;
					if (op.size()!=0 && po != op[d1].second)
						po < op[d1].second ? po++ : po--;
					time++;
				}
				else
				{//cout<<"2"<<endl;
					while (pb != bp[d2].second)
					{
						pb < bp[d2].second ? pb++ : pb--;//cout<<"3"<<endl;
						if (op.size()!=0 && po != op[d1].second)
							po < op[d1].second ? po++ : po--; //cout<<"4"<<endl;
						time++;
					}
					if (op.size()!=0 && po != op[d1].second)
							po < op[d1].second ? po++ : po--;
					time++;
					d2++;
				}
			}
		}
		cout << "Case #" << tstCs++ << ": " << time << endl;
	}
    return 0; 
}

