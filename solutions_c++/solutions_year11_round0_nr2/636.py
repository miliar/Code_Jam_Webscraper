#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<sstream>
#include<stack>
#include<vector>
#include<list>

#define Max(x,y) (x>y?x:y)
#define Min(x,y) (x<y?x:y)

using namespace std;
int T;

int c,d,n;

char form[50][50];
char oppose[50][50];

char str[2000];

void solve()
{
	cin>>c;
	for(int i = 0;i < c;i++)
	{
		scanf("%s",str);
		form[str[0]-'A'][str[1]-'A'] = form[str[1]-'A'][str[0]-'A'] = str[2];
	}
	cin>>d;
	for(int i = 0;i < d;i++)
	{
		scanf("%s",str);
		oppose[str[0]-'A'][str[1]-'A'] = oppose[str[1]-'A'][str[0]-'A'] = 1;
	}
	cin>>n;
	scanf("%s",str);

	vector<char> vec;
	for(int i = 0;i < n;i++)
	{
		char ch = str[i],cc;
		if(vec.empty())
		{
			vec.push_back(ch);
			continue;
		}

		cc = form[ ch-'A' ][ vec.back() - 'A' ];
		while(!vec.empty() && form[ ch-'A' ][ vec.back() - 'A' ])
		{
			ch = cc = form[ ch-'A' ][ vec.back() - 'A' ];
			vec.pop_back();
		}
		vec.push_back(ch);
		for(int j = 0;j < vec.size()-1;j++)
		{
			if(oppose[ vec[j]-'A' ][ch-'A'])
			{
				vec.clear();
				break;
			}
		}
	}
	if(vec.empty())
	{
		cout<<"[]"<<endl;
		return;
	}
	cout<<"["<<vec[0];
	for(int i = 1;i < vec.size();i++)
		printf(", %c",vec[i]);
	cout<<"]"<<endl;
}

int main()
{
	freopen("f:\\GJ\\in.txt","r",stdin);
	freopen("f:\\GJ\\out.txt","w",stdout);

////////////////////////////////////////////////////////////////////

	cin>>T;
	int cases;
	for(cases = 1;cases <= T;cases++)
	{
		printf("Case #%d: ",cases);
		memset(form,0,sizeof(form));
		memset(oppose,0,sizeof(oppose));
		solve();
	}

////////////////////////////////////////////////////////////////////

	fclose(stdout);	
	return 0;
}