#include<iostream>
#include<set>
using namespace std;
int A,B, num;

int ten[10] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

inline int solve(int n)
{
	int tmp = n;
	int count = 0;
	int pre = -1;
	set<int> Set;
	Set.clear();
	int top = -1;
	for(int i = 1;i < num;i++)
	{
		tmp = n;

		int res = tmp % ten[i];
		tmp /= ten[i];
		tmp += res * ten[num - i];
		//if(tmp == pre)continue;
		///pre = tmp;
		if(Set.find(tmp) != Set.end())continue;
		if(n == 223)
		{
			//cout<<"error"<<endl;
		}
		if(tmp >= A & tmp <= B && tmp > n)
		{
			Set.insert(tmp);
			//cout<<n<<' '<<tmp<<' ';
			count++;

		}
	}
	//if(count>0)cout<<endl;
	return count;


}
int main()
{
	int testcase;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d",&testcase); 
	for(int i = 1;i <= testcase;i++)
	{
		scanf("%d%d", &A, &B);
		//cout<<A<<' '<<B<<' ';
		long long count = 0;
		int tmp = A;
		num = 0;
		while(tmp > 0)
		{
			num++;
			tmp /= 10;
		}
		for(int j = A;j <= B;j++)
		{
			count+=solve(j);
		}
		cout<<"Case #"<<i<<": ";
		cout<<count<<endl;;
		
	}
}