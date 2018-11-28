#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <sstream>
#include <map>
#include <algorithm>
#include <fstream>
using namespace std;
ifstream in("B-small.in");
ofstream out("B-small.out");
#define cout out

int n,t,na,nb;

const int N = 130;

struct Node
{
	int be;
	int ed;
};
bool cmp(const Node & n1,const Node &n2)
{
	if(n1.be < n2.be)
		return true;
	if(n1.be > n2.be)
		return false;
	return n1.ed < n2.ed;
	
	//return n1.be < n2.be;
}


Node a[N];
Node b[N];

bool fa[N];
bool fb[N];

int sizea;
int sizeb;


int main()
{
	cin >> n;
	for(int i =0;i < n;i ++)
	{
		cin >> t;
		cin >> na >> nb;
		memset(fa,false,sizeof(fa));
		memset(fb,false,sizeof(fb));


		for(int j = 0;j < na;j ++)
		{
			string s1,s2;
			cin >> s1 >> s2;
			int sum = 0;
			sum = ((s1[0] - 48) * 10 + s1[1] - 48 ) * 60 + (s1[3] - 48) * 10 + (s1[4] - 48);
			a[j].be = sum;
			sum = 0;
			sum = ((s2[0] - 48) * 10 + s2[1] - 48 ) * 60 + (s2[3] - 48) * 10 + (s2[4] - 48);
			a[j].ed = sum;
		}
		for(int j = 0;j < nb;j ++)
		{
			string s1,s2;
			cin >> s1 >> s2;
			int sum = 0;
			sum = ((s1[0] - 48) * 10 + s1[1] - 48 ) * 60 + (s1[3] - 48) * 10 + (s1[4] - 48);
			b[j].be = sum;
			sum = 0;
			sum = ((s2[0] - 48) * 10 + s2[1] - 48 ) * 60 + (s2[3] - 48) * 10 + (s2[4] - 48);
			b[j].ed = sum;
		}
		sort(a,a + na,cmp);
		sort(b,b + nb,cmp);

		int sizea = na;
		int sizeb = nb;

		int ansa = 0;
		int ansb = 0;

		while(sizea > 0 && sizeb > 0)
		{
			int posa,posb;
			int mmina = 10000000;
			int mminb = 10000000;
			for(int j = 0;j < na;j ++)
			{
				if(!fa[j])
				{
					mmina = a[j].be;
					posa = j;
					break;
				}
			}
			for(int j = 0;j < nb;j ++)
			{
				if(!fb[j])
				{
					mminb = b[j].be;
					posb = j;
					break;
				}
			}

			if(mmina < mminb || (mmina == mminb &&  a[posa].ed < b[posb].ed))
			{
				ansa ++;

				sizea --;
				fa[posa] = true;
				int tag = 1;
				int time = a[posa].ed + t;

				int aa = 0;
				int bb = 0;

				while(1)
				{
					if(tag == 1)
					{
						for(;bb < nb;bb ++)
						{
							if(!fb[bb] && b[bb].be >= time)
							{
								fb[bb] = true;
								sizeb --;
								time = b[bb].ed + t;
								tag = 0;
								break;
							}
						}
						if(bb >= nb)
						{
							break;
						}
					}
					if(tag == 0)
					{
						for(;aa < na;aa ++)
						{
							if(!fa[aa] && a[aa].be >= time)
							{
								fa[aa] = true;
								sizea --;
								time = a[aa].ed + t;
								tag = 1;
								break;
							}
						}
						if(aa >= na)
						{
							break;
						}
					}
				}
			}
			else
			{
				ansb ++;

				sizeb --;
				fb[posb] = true;
				int tag = 0;
				int time = b[posb].ed + t;

				int aa = 0;
				int bb = 0;

				while(1)
				{
					if(tag == 1)
					{
						for(;bb < nb;bb ++)
						{
							if(!fb[bb] && b[bb].be >= time)
							{
								fb[bb] = true;
								sizeb --;
								time = b[bb].ed + t;
								tag = 0;
								break;
							}
						}
						if(bb >= nb)
						{
							break;
						}
					}
					if(tag == 0)
					{
						for(;aa < na;aa ++)
						{
							if(!fa[aa] && a[aa].be >= time)
							{
								fa[aa] = true;
								sizea --;
								time = a[aa].ed + t;
								tag = 1;
								break;
							}
						}
						if(aa >= na)
						{
							break;
						}
					}
				}
			}
		}
		cout << "Case #"<<i + 1<<": ";
		cout << ansa  + sizea<< " " << ansb + sizeb << endl;
	}



	return 0;
}