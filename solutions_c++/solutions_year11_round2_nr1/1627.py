#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	long long int n;
	int pd, pg;
	int case_num;
	//ifstream ifile("A-small-attempt0.in");
	//ofstream ofile("A-small-attempt0.out");
	ifstream ifile("A-large.in");
	ofstream ofile("A-large.out");
	//ifstream ifile("q.txt");
	//ofstream ofile("a.txt");
	ifile >> case_num;
	for(int i=0;i<case_num;++i)
	{
		int n;
		ifile >> n;
		vector< vector<char> > schedule;
		for(int j=0;j<n;++j)
		{
			vector<char> row;
			for(int k=0;k<n;++k)
			{
				char tmp;
				ifile >> tmp;
				row.push_back(tmp);
			}
			schedule.push_back(row);
		}
		vector<int> win;
		vector<int> t_cnt;
		vector<double> wp;
		for(int j=0;j<n;++j)
		{
			int win_cnt=0, cnt=0;
			for(int k=0;k<n;++k)
			{
				if(schedule[j][k] == '0')
					cnt++;
				else if(schedule[j][k] == '1')
				{
					cnt++;
					win_cnt++;
				}
			}
			win.push_back(win_cnt);
			t_cnt.push_back(cnt);
			wp.push_back((double)win_cnt / cnt);
		}
		vector<double> owp;
		for(int j=0;j<n;++j)
		{
			int cnt=0;
			double wp_cnt=0;
			for(int k=0;k<n;++k)
			{
				if(schedule[j][k] == '.')
					continue;
				if(schedule[j][k] == '0')
					wp_cnt += (double)(win[k] - 1) / (t_cnt[k] -1);
				else
					wp_cnt += (double)win[k] / (t_cnt[k] -1);
				cnt++;
			}
			owp.push_back(wp_cnt / cnt);
		}
		vector<double> oowp;
		for(int j=0;j<n;++j)
		{
			int cnt=0;
			double oowp_tmp=0;
			for(int k=0;k<n;++k)
			{
				if(schedule[j][k] == '.')
					continue;
				oowp_tmp += owp[k];
				cnt++;
			}
			oowp.push_back(oowp_tmp / cnt);
		}
		ofile << "Case #" << i+1 << ":\n";
		for(int j=0;j<n;++j)
		{
			//cout << 0.25 * win[j]/t_cnt[j] + 0.5 * owp[j] + 0.25 * oowp[j] << endl;
			
			ofile << 0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j] << endl;
		}
	}
	ifile.close();
	ofile.close();
	system("pause");
	return 0;
}

