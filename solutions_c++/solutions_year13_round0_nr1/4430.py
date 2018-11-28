#include<fstream>
#define n 4
using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int main()
{
	int T;
	in >> T;
	for(int t=0;t<T;t++)
	{
		char Data[5][5]={0,};
		int i,j;
		for(i=0;i<n;i++)
			in>>Data[i];

		int remain=0;
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(Data[i][j] == '.')
					remain++;

		int X_cnt=0;
		int O_cnt=0;
		int T_cnt=0;
		for(i=0;i<n;i++)
		{
			if(Data[i][i] == 'X')
				X_cnt++;
			if(Data[i][i] == 'O')
				O_cnt++;
			if(Data[i][i] == 'T')
				T_cnt++;
		}
		if((X_cnt == 4 && T_cnt == 0) || (X_cnt==3 && T_cnt==1))
		{
			out << "Case #" << t+1 << ": X won" << endl;
			continue;
		}
		if((O_cnt == 4 && T_cnt == 0) || (O_cnt==3 && T_cnt==1))
		{
			out << "Case #" << t+1 << ": O won" << endl;
			continue;
		}
		X_cnt=0;
		O_cnt=0;
		T_cnt=0;
		for(i=0;i<n;i++)
		{
			if(Data[i][3-i] == 'X')
				X_cnt++;
			if(Data[i][3-i] == 'O')
				O_cnt++;
			if(Data[i][3-i] == 'T')
				T_cnt++;
		}
		if((X_cnt == 4 && T_cnt == 0) || (X_cnt==3 && T_cnt==1))
		{
			out << "Case #" << t+1 << ": X won" << endl;
			continue;
		}
		if((O_cnt == 4 && T_cnt == 0) || (O_cnt==3 && T_cnt==1))
		{
			out << "Case #" << t+1 << ": O won" << endl;
			continue;
		}
		int ans=0;
		for(i=0;i<n;i++)
		{
			X_cnt=0;
			O_cnt=0;
			T_cnt=0;
			for(j=0;j<n;j++)
			{
				if(Data[i][j] == 'X')
					X_cnt++;
				if(Data[i][j] == 'O')
					O_cnt++;
				if(Data[i][j] == 'T')
					T_cnt++;
			}
			if((X_cnt == 4 && T_cnt == 0) || (X_cnt==3 && T_cnt==1))
			{
				out << "Case #" << t+1 << ": X won" << endl;
				ans=1;
				break;
			}
			if((O_cnt == 4 && T_cnt == 0) || (O_cnt==3 && T_cnt==1))
			{
				out << "Case #" << t+1 << ": O won" << endl;
				ans=1;break;
			}

			X_cnt=0;
			O_cnt=0;
			T_cnt=0;
			for(j=0;j<n;j++)
			{
				if(Data[j][i] == 'X')
					X_cnt++;
				if(Data[j][i] == 'O')
					O_cnt++;
				if(Data[j][i] == 'T')
					T_cnt++;
			}
			if((X_cnt == 4 && T_cnt == 0) || (X_cnt==3 && T_cnt==1))
			{
				out << "Case #" << t+1 << ": X won" << endl;
				ans=1;
				break;
			}
			if((O_cnt == 4 && T_cnt == 0) || (O_cnt==3 && T_cnt==1))
			{
				out << "Case #" << t+1 << ": O won" << endl;
				ans=1;break;
			}
		}
		if(ans==1)continue;

		if(remain == 0)
			out << "Case #" << t+1 << ": Draw" << endl;
		else
			out << "Case #" << t+1 << ": Game has not completed" << endl;
	}
	return 0;
}