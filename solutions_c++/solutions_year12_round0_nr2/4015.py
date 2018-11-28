#include<fstream>
#include<cstring>
using namespace std;
ifstream fin("b.in");
ofstream fout("b.out");
int score[101],n,s,p,ans;
void work()
{
	fin >> n >> s >> p;
	for (int i=1;i<=n;++i) fin >> score[i];
	if (p==0) {ans=n;return;}
	for (int i=1;i<=n;++i)
	{
		if (score[i]==0) continue;
		else if (p*3<=score[i]+2) ++ans;
		else if (p*3<=score[i]+4 && s>0) {++ans;--s;}
	}
	return;
}
int main()
{
	int T;
	fin >> T;
	for (int cnt=1;cnt<=T;++cnt)
	{
		ans=0;
		memset(score,0,sizeof(score));
		work();
		fout << "Case #"<<cnt<<": "<<ans<<endl;
	}
	return 0;
}
