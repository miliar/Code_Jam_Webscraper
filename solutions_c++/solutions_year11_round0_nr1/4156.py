#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	int t;
	cin >> t;
	int k;
	int i;
	ofstream outf;
	outf.open("1.out",ios::out);
	for (k = 1;k <= t;k++)
	{
		int n;
		int otarget[100];
		int orank[100];
		int omark[100];//0表示还未到达，1表示已到达还未按钮，2表示已按钮，3代表终点
		int btarget[100];
		int brank[100];
		int bmark[100];
		cin >> n;
		char tmp1;
		int tmp2;
		int ocnt = 0;
		int bcnt = 0;
		int sec;
		for (i = 0;i < 100;i++)
		{
			orank[i] = brank[i] = 999;
			omark[i] = bmark[i] = 3;
		}
		for (i = 0;i < n;i++)
		{
			cin >> tmp1 >> tmp2;
			if (tmp1 == 'O')
			{
				otarget[ocnt] = tmp2;
				orank[ocnt] = i;
				omark[ocnt] = 0;
				ocnt++;
			}
			else
			{
				btarget[bcnt] = tmp2;
				brank[bcnt] = i;
				bmark[bcnt] = 0;
				bcnt++;
			}
		}
		int o = 0;
		int b = 0;
		int opos = 1;
		int bpos = 1;
		if (ocnt > 0 && otarget[0] == 1)
			omark[0] = 1;
		if (bcnt > 0 && btarget[0] == 1)
			bmark[0] = 1;
		for (sec = 1;;sec++)
		{
			if ((ocnt == 0 ||( ocnt > 0 && omark[o] == 3)) && (bcnt == 0 ||( bcnt > 0 && bmark[b] == 3)))
				break;
			if (orank[o] < brank[b])
			{
				if (bmark[b] == 0)
				{
					bpos += (bpos < btarget[b] ? 1 : -1);
					if (bpos == btarget[b])
						bmark[b] = 1;
				}

				if (omark[o] == 1)
				{
					omark[o] = 2;
					if (o == ocnt - 1)
					{
						omark[o] = 3;
						orank[o] = 999;
					}
					else
					{
						o++;
						if (opos == otarget[o])
							omark[o] = 1;
					}
				}
				else
				{
					if (omark[o] == 0)
					{
						opos += (opos < otarget[o] ? 1 : -1);
						if (opos == otarget[o])
							omark[o] = 1;
					}
				}
			}
			else
			{
				if (omark[o] == 0)
				{
					opos += (opos < otarget[o] ? 1 : -1);
					if (opos == otarget[o])
						omark[o] = 1;
				}

				if (bmark[b] == 1)
				{
					bmark[b] = 2;
					if (b == bcnt - 1)
					{
						bmark[b] = 3;
						brank[b] = 999;
					}
					else
					{
						b++;
						if (bpos == btarget[b])
							bmark[b] = 1;
					}
				}					
				else
				{
					if (bmark[b] == 0)
					{
						bpos += (bpos < btarget[b] ? 1 : -1);
						if (bpos == btarget[b])
							bmark[b] = 1;
					}
				}
			}
		}
		outf <<"Case #"<<k<<": "<<sec-1 << endl;
	}
	return 0;
}