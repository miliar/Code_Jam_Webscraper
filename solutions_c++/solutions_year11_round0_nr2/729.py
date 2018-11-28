#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int C,D,n;
vector<string> cmb, op;
vector<char> ans;
string data;
void read_data()
{
	cmb.clear();  op.clear();
	cin >> C;
	int i;
	string temp;
	for (i=1;i<=C;i++)
	{
		cin >> temp;
		cmb.push_back(temp);
	}
	cin >> D;
	for (i=1;i<=D;i++)
	{
		cin >> temp;
		op.push_back(temp);
	}
	cin >> n;
	cin >> data;
}

char test_cmb(char a,char b)
{
	int i;
	for (i=0;i<cmb.size();i++)
	{
		if (cmb[i][0] == a && cmb[i][1] == b) return cmb[i][2];
		if (cmb[i][0] == b && cmb[i][1] == a) return cmb[i][2];
	}
	return -1;
}

bool test_op(char a,char b)
{
	int i;
	for (i=0;i<op.size();i++)
	{
		if (op[i][0] == a && op[i][1] == b) return true;
		if (op[i][0] == b && op[i][1] == a) return true;
	}
	return false;
}
void work_ans()
{
	ans.clear();
	int i,j;
	char temp;
	for (i=0;i<n;i++)
	{
		ans.push_back(data[i]);
		if (ans.size() < 2) continue;
		temp = test_cmb(ans[ans.size() - 1],ans[ans.size() - 2]);
		if (temp != -1)
		{
			ans.pop_back();  ans.pop_back();
			ans.push_back(temp);
		}
		for (j=0;j<ans.size();j++) if (test_op(ans[j],ans[ans.size() - 1]))
		{
			ans.clear();
			break;
		}
	}
}

void show_ans()
{
	if (ans.size() == 0)
	{
		printf("[]\n");
		return;
	}

	printf("[%c",ans[0]);
	int i;
	for (i=1;i<ans.size();i++) printf(", %c",ans[i]);
	printf("]\n");
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		read_data();
		work_ans();
		show_ans();
	}
	return 0;
}