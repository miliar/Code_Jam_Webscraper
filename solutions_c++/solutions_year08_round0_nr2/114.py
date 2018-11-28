#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
#define MIN(a,b) ( (a) < (b) ? (a) : (b) )
#define MAX(a,b) ( (a) > (b) ? (a) : (b) )
int vA[2000], vB[2000], pA[2000], pB[2000];
int TtoM(string s)
{
	int h=10*(s[0]-'0')+s[1]-'0';
	int m=10*(s[3]-'0')+s[4]-'0';
	return 60*h+m;
}
int main()
{
	int N;
	
	int ind=0;
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin>>N;
	while(N)
	{
		N--;
		ind++;
		memset(vA,0,sizeof(vA));
		memset(vB,0,sizeof(vB));
		memset(pA,0,sizeof(pA));
		memset(pB,0,sizeof(pB));
		int T;
		cin>>T;
		int nA,nB;
		cin>>nA>>nB;
		int i;
		for(i=0;i<nA;i++)
		{
			string s1,s2;
			cin>>s1>>s2;
			int tmp=TtoM(s1);
			vA[tmp]++;
			tmp=TtoM(s2);
			pB[tmp+T]++;
		}
		for(i=0;i<nB;i++)
		{
			string s1,s2;
			cin>>s1>>s2;
			int tmp=TtoM(s1);
			vB[tmp]++;
			tmp=TtoM(s2);
			pA[tmp+T]++;
		}
		int mA=0,mB=0;
		int potA=0,potB=0;
		for(i=0;i<1440;i++)
		{
			potA-=pA[i];
			potB-=pB[i];
			potA+=vA[i];
			potB+=vB[i];
			mA=MAX(mA,potA);
			mB=MAX(mB,potB);
		}
		cout<<"Case #"<<ind<<": "<<mA<<" "<<mB<<endl;
	}
	return 0;
}