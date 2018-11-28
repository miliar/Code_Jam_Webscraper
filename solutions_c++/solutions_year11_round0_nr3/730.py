#include <iostream>
using namespace std;
#define M 1100
int n;
int data[M];

void read_data()
{
	cin >> n;
	int i;
	for (i=1;i<=n;i++) cin >> data[i];
}

int work_ans()
{
	int temp = 0;
	int i;
	for (i=1;i<=n;i++) temp = temp ^ data[i];
	if (temp != 0) return -1;
	int sum = 0;
	temp = 0x7fffffff;
	for (i=1;i<=n;i++)
	{
		sum += data[i];
		if (temp > data[i]) temp = data[i];
	}
	return sum - temp;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int ans,t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		read_data();
		ans = work_ans();
		if (ans != -1) printf("%d\n",ans); else printf("NO\n");
	}
	return 0;
}
