/*#include<iostream>
#include<string.h>
using namespace std;
char a[1000] = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvzq";
char b[1000] = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupqz";
void solve()
{

}
int main()
{
	char G[1000];
	char c;
	int testcase;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	scanf("%d",&testcase);
	cin.getline(G, 1000);
	for(int i = 1;i <= testcase;i++)
	{
		cin.getline(G, 1000);
		cout<<"Case #"<<i<<": ";
		for(int j = 0;j < strlen(G);j++)
		{
			if(G[j] == ' ')
			{
				cout<<' ';
				continue;
			}
			for(int k = 0;;k++)
			{
				if(a[k] == G[j])
				{
					cout<<b[k];
					break;

				}
			}

		}
		cout<<endl;
	}
	return 0;
}*/

#include<iostream>
using namespace std;
int s,p,t[200], N;

int main()
{
	int testcase;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d",&testcase);
	for(int i = 1;i <= testcase;i++)
	{
		scanf("%d%d%d", &N, &s, &p);
		cout<<"Case #"<<i<<": ";
		//cout<<N<<' '<<s<<' '<<p<<' ';
		int count = 0;
		int total = N;
		for(int j = 0;j < N;j++)
		{
			scanf("%d", &t[j]);
			//cout<<t[j]<<' ';
			if(t[j] >= 3*(p-1)+1)
			{
				count++;
			}
			if(t[j] < 3 * p - 5 || t[j] < p)total --;
		}
		int left = total - count;
		if(left >= s)
		{
			cout<<s + count<<endl;
		}
		else
		{
			cout<<total<<endl;
		}
	}
}