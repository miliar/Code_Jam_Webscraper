#include<iostream>
#include<fstream>
#include<memory>
#include<cmath>
using namespace std;
int T;
int R,N;
double k;
int g[1001];
int t[1001];//t[i]����t[i]�ֺ�i��λ�ڶ���;
int pos[1001];//pos[i]����i�ֺ󣬵�pos[i]��λ�ڶ���
double money[1001];//money[i]��i�ֺ����Ǯ��;
int flag[1001];//0����δ��������;1������������
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
	int num=0;//����
	int period=0;//period��һѭ��;
	double money_period;//һ��ѭ����׬��Ǯ;
	double money_now=0;//��ǰǮ��
	i=1;//�ӵ�һ�ӿ�ʼ
	while(num<R)//g[i]��δ��������
	{
		int sum=0;//������һ���ܹ��ϳ�������
		if(flag[i]==1)
		{
			period=num-t[i];
			money_period=money_now-money[t[i]];
			break;
		}
		flag[i]=1;
		t[i]=num;
		pos[num]=i;//num�ֺ�,i��λ�ڶ���,ֻ��¼��������N+1��;
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
		money[num]=money_now;//��num�ֺ��Ǯ
	}
	//num�ֺ�money_now;
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