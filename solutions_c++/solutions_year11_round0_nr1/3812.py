#include <stdio.h>
#include <vector>
#include <math.h>
using namespace std;

int cs,n;
char op[5];
int on,bn;
vector<int> or,bl;
struct node
{
	node(char a,int b):op(a),cur(b) {};
	char op;
	int cur;
};
vector<node> vn;
int curo,curb;

int cn = 1;

int main()
{
	int i,j,x;
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&cs);
	while(cs--)
	{
		vn.clear();
		or.clear();
		bl.clear();
		int ans = 0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s%d",op,&x);
			if(op[0] == 'O')
			{
				or.push_back(x);
			}
			else
			{
				bl.push_back(x);
			}
			vn.push_back(node(op[0],x));
		}
		on = bn = 0;
		curo = curb = 1;

		for(i=0;i<vn.size();i++)
		{
			if(vn[i].op == 'O')
			{
				int time = abs(curo-vn[i].cur)+1;
				curo = vn[i].cur;
				on++;
				if(bn < bl.size())
				{
					int t = abs(bl[bn] - curb);
					if(time >= t)
					{
						curb = bl[bn];
					}
					else
					{
						if(bl[bn] > curb) curb += time;
						else curb -= time;
					}
				}
				ans += time;
			}
			else
			{
				int time = abs(curb-vn[i].cur)+1;
				curb = vn[i].cur;
				bn++;
				if(on < or.size())
				{
					int t = abs(or[on] - curo);
					if(time >= t)
					{
						curo = or[on];
					}
					else
					{
						if(or[on] > curo) curo += time;
						else curo -= time;
					}
				}
				ans += time;
			}
		}

		printf("Case #%d: %d\n",cn++,ans);
	}
	return 0;
}
