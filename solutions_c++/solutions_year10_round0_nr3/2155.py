#include<iostream>
#include<fstream>
#include<memory>
#include<cmath>
using namespace std;
int T;
int R,N;
double k;
int g[1001];
int t[1001];//t[i]代表t[i]轮后，i队位于队首;
int pos[1001];//pos[i]代表i轮后，第pos[i]组位于队首
double money[1001];//money[i]第i轮后的总钱数;
int flag[1001];//0代表未做过队首;1代表做过队首
ifstream fin("C-small-attempt1.in");
ofstream fout("ans-small.txt");
double solve()
{
	fin>>R;
	fin>>k;
	fin>>N;
	memset(flag,0,sizeof(flag));
	int i=0;
	for(i=1;i<=N;i++)
		fin>>g[i];
	int num=0;//轮数
	int period=0;//period轮一循环;
	double money_period;//一个循环所赚的钱;
	double money_now=0;//当前钱数
	i=1;//从第一队开始
	while(num<R)//g[i]尚未做过队首
	{
		int sum=0;//代表这一次能够上车的人数
		if(flag[i]==1)
		{
			period=num-t[i];
			money_period=money_now-money[t[i]];
			break;
		}
		flag[i]=1;
		t[i]=num;
		pos[num]=i;//num轮后,i组位于队首,只记录不超过第N+1轮;
		int istart=i;
		while(sum+g[i]<=k)
		{
			sum=sum+g[i];
			i=i+1;
			if (i>N)
				i=i-N;
			if(i==istart)
				break;
		}
		money_now=money_now+sum;
		num++;
		money[num]=money_now;//第num轮后的钱
	}
	//num轮后，money_now;
	if(period==0)
		return money_now;
	else
	{
		int remain;
		remain=R-int((R-num)/period)*period-num;
		return (money_now+int((R-num)/period)*money_period+money[remain+t[i]]-money[t[i]]);
	}

}
int main()
{
	int i;
	fin>>T;
	for(i=1;i<=T;i++)
	{
		fout<<"Case #"<<i<<": ";
		fout<<solve()<<"\n";
	}
	return 0;
}