#include<iostream>
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
}