#include<iostream>
#include<string>
using namespace std;
string koki[1001];
string int2str(int x)
{
	string str = "";
	while(x)
	{
		str += (x%10)+'0';
		x/=10;
	}
	reverse(str.begin(),str.end());
	return str;
}

int pre[1001][1001];
bool isOk(int a,int b)
{
	if(pre[a][b] != -1)
		return pre[a][b];
	string A = koki[a];
	string B = koki[b];
	if(A.size() != B.size())
		return pre[a][b] = pre[b][a] = false;
	for(int i=0;i<A.size();i++)
	{
		bool ok = true;
		for(int j=0;j<A.size();j++)
		{
			if(A[j] != B[(i+j)%A.size()])
			{
				ok = false;
				break;
			}
		}
		if(ok)
			return pre[a][b] = pre[b][a] = true;
	}
	return pre[a][b] = pre[b][a] = false;
}


int main()
{
	for(int i=0;i<=1000;i++)
		koki[i] = int2str(i);
	memset(pre,-1,sizeof(pre));
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int CN;
	cin >> CN;
	
	
	for(int k=1;k<=CN;k++)
	{
		int A,B;
		cin >> A >> B;
		int res = 0;
		for(int i=A;i<=B;i++)
		{
			for(int j=i+1;j<=B;j++)
			{
				res += isOk(i,j);
			}
		}
		printf("Case #%d: %d\n",k,res);
	}
	return 0;
}