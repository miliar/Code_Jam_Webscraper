#include <cstdio>
#include <vector>
#include <string>

using namespace std;

vector<pair<pair<char,char>,char> > base;
vector<pair<char,char> > opposed;
string message;

void Input()
{
	base.clear();
	opposed.clear();
	int C,D;
	char buf[1000];
	scanf("%d",&C);
	for (int i=0; i<C; i++)
	{
		scanf("%s", buf);
		base.push_back(make_pair(make_pair(buf[0],buf[1]),buf[2]));
	}
	scanf("%d",&D);
	for (int i=0; i<D; i++)
	{
		scanf("%s", buf);
		string s;
		opposed.push_back(make_pair(buf[0],buf[1]));
	}
	scanf("%d", &D);
	scanf("%s", buf);
	message = buf;
}

string DoBase(int pos, int indexBase)
{
	string res = message.substr(0,pos);
	res.push_back(base[indexBase].second);
	res += message.substr(pos+2,message.length()-(pos+2));
	return res;
}

string DoOpposide(int start, int end)
{
	string res = message.substr(end+1,message.length()-(end+1));
	return res;
}

void Solve()
{
	while(true)
	{
		bool did = false;
		for (int i=1; i<message.size() && did == false; i++)
		{
			for (int j=0; j<base.size() && did == false; j++)
			{
				if (message[i] == base[j].first.first)
				{
					if (message[i-1] == base[j].first.second)
					{
						message = DoBase(i-1,j);
						did = true;
						break;
					}
				}
				if(message[i] == base[j].first.second)
				{
					if (message[i-1] == base[j].first.first)
					{
						message = DoBase(i-1,j);
						did = true;
						break;
					}
				}
			}
			
			for (int j=0; j<opposed.size() && did == false; j++)
			{
				if (message[i] == opposed[j].first)
				{
					for (int k=0; k<i && did == false; k++)
					{
						if (message[k] == opposed[j].second)
						{
							message = DoOpposide(k,i);
							did = true;
							break;
						}
					}
				}
				if (did)
					break;
				if(message[i] == opposed[j].second)
				{
					for (int k=0; k<i && did == false; k++)
					{
						if (message[k] == opposed[j].first)
						{
							message = DoOpposide(k,i);
							did = true;
							break;
						}
					}
				}
			}
		}
		if (did == false)
			break;
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		Input();
		Solve();
		printf("Case #%d: [", t);
		for (int i=0; i<message.size(); i++)
		{
			if (i != 0)
				printf(", ");
			printf("%c", message[i]);
		}
		printf("]\n");
	}
	return 0;
}