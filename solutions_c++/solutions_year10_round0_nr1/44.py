#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;
const int inf=0x3f3f3f3f;
const double ERR=1e-9;
class snapperchain
{
	private:
		int n,k;
		bool ison;
	public:
		snapperchain() {}
		void input()
		{
			scanf("%d%d",&n,&k);
		}
		bool solve()
		{
			int vn=(1<<n);
			return k%vn==vn-1;
		}
};
int main(void)
{
	int znj;
	scanf("%d",&znj);
	for(int i=0;i<znj;++i)
	{
		snapperchain task;
		task.input();
		printf("Case #%d: %s\n",i+1,task.solve()?"ON":"OFF");
	}
	return 0;
}
