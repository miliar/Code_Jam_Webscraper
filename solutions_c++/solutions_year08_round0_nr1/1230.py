#include<iostream>
#include<string>
#include<map>

using namespace std;

int S,Q,ans,cnt;
map<string,int> T;
string tmp;
int P[100 + 5];

int main()
{
	freopen("output.txt","w",stdout);
	int ntest;
	cin>>ntest;
	for(int test=1;test<=ntest;test++)
	{
		T.clear();
		cin>>S; getline(cin,tmp);
		for(int i=0;i<S;i++)
		{
			getline(cin,tmp);
			T[tmp]=i;
		}
		cin>>Q; getline(cin,tmp);
		ans=0; cnt=0;
		memset(P,0,sizeof(P));
		for(int i=0;i<Q;i++)
		{
			getline(cin,tmp);
			if(T.find(tmp)==T.end()) continue;
			if(++P[T[tmp]]==1) cnt++;
			if(cnt==S)
			{
				cnt=0;
				ans++;
				memset(P,0,sizeof(P));
				P[T[tmp]]=1; cnt++;
			}
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
