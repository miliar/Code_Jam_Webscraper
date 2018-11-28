#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int tt,tc;
int num[30],len;

bool checkMax(int pos)
{
	int i;
	for (i=1;i<=pos;i++)
		if (num[i]<num[i-1]) return false;
	return true;
}

bool pred(int i,int j)
{
	return i>j;
}

void solve(int pos)
{
	int i;
	for (i=0;i<pos;i++)
		if (num[i]>num[pos]) 
		{
			swap(num[i],num[pos]);
			break;
		}
	sort(num,num+pos,pred);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out.txt","w",stdout);

	cin>>tc;
	string str;

	int i,j;
	for (tt=1;tt<=tc;tt++)
	{
		printf("Case #%d: ",tt);
		cin>>str;
		len=str.length();

		for (i=0;i<str.length();i++)
			num[len-i-1]=str[i]-'0';

		bool found=false;
		for (i=0;i<len;i++)
			if (!checkMax(i))
			{
				found=true;
				
//				int tmp=num[0];
				
//				for (j=0;j<i;j++)
//					num[j]=num[j+1];
//				num[i]=tmp;
				solve(i);
				for (j=len-1;j>=0;j--)
					cout<<num[j];
				cout<<endl;
				break;
			}
		
		if (!found)
		{
			//add zero
			int cnt[10];
			memset(cnt,0,sizeof(cnt));
			for (i=0;i<len;i++)
				cnt[num[i]]++;
			cnt[0]++;
			for (i=1;i<10;i++)
				if (cnt[i]>0)
				{
					cout<<i;
					cnt[i]--;
					break;
				}
			for (i=1;i<=cnt[0];i++)
				cout<<0;
			for (i=1;i<10;i++)
				for (j=1;j<=cnt[i];j++)
					cout<<i;
			cout<<endl;
		}
	}
}
