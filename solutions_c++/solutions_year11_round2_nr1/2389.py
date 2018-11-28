#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(void)
{
	int test_cases, n, arr_use[10][10], count_win[10], count_total[10];
	char arr[10][10];
	double wp[10], owp[10], oowp[10], rpi[10], total_wp_count, total_owp_count;
	ifstream in("inp.txt", ios::in);
	ofstream out("out.txt", ios::out);
	in>>test_cases;
	cout<<fixed<<setprecision(7);
	//double ll=double(2)/double(3);
	//cout<<"ll isd:: "<<ll<<endl;
	for(int i=1; i<=test_cases; ++i)
	{
		in>>n;
	//	cout<<"n is: "<<n<<endl;
		for(int j=0; j<n; ++j)
		{
			for(int k=0; k<n; ++k)
			{in>>arr[j][k];}
		}
		//finding answer
		for(int j=0; j<n; ++j)
		{
			for(int k=0; k<n; ++k)
			{
				if(arr[j][k]=='.')
				{arr_use[j][k]=-1;}
				else
				{arr_use[j][k]=arr[j][k]-'0';}
			}
		}
		for(int j=0; j<n; ++j)
		{
			count_win[j]=0;
			count_total[j]=0;
			for(int k=0; k<n; ++k)
			{
				if(arr_use[j][k]==-1)
				{continue;}
				else if(arr_use[j][k]==1)
				{++count_win[j];}
				++count_total[j];
			}
			if(count_total[j]==0)
			{wp[j]=0;}
			else
			{wp[j]=(double)(count_win[j])/(double)(count_total[j]);}
		}
		//printing winning percentage
		/*for(int j=0; j<n; ++j)
		{
			cout<<count_win[j]<<"\t";
		}
		cout<<endl;
		for(int j=0; j<n; ++j)
		{
			cout<<count_total[j]<<"\t";
		}*/
		//cout<<endl;
		//cout<<"winning percentage:\n";
		//for(int j=0; j<n; ++j)
		//{
		//	cout<<wp[j]<<"\t";
			
		//}
		//cout<<endl;
		//d
		//opponent winning percentager
		for(int j=0; j<n; ++j)
		{
			//cout<<"count_win[j]:: "<<count_win[j]<<endl;
			//cout<<"count_total[j]:: "<<count_total[j]<<endl;
			total_wp_count=0.0;
			total_owp_count=0.0;
			for(int k=0; k<n; ++k)
			{
				//cout<<"k is:: "<<k<<endl;
				if(arr_use[j][k]==-1)
				{continue;}
				else if(arr_use[j][k]==1)
				{total_wp_count+= ((double)(count_win[k])/(double)((count_total[k])-1));}
				else
				{
					if(count_win[k]!=0)
					{
					//	cout<<"in here"<<endl;
						total_wp_count+= ((double)(count_win[k]-1)/(double)(count_total[k]-1));
					}
				}
				//total_owp_count+=wp[k];
				//cout<<"total_wp_count:: "<<total_wp_count<<endl;
			//cout<<"total_owp_count:: "<<total_owp_count<<" gh"<<wp[k]<<endl;
			}
			if(count_total==0)
			{
				//oowp[j]=0;
				owp[j]=0;
			}
			else
			{
				owp[j]= total_wp_count/(double)count_total[j];
				//oowp[j]= total_owp_count/(double)count_total[j];
			}
			//cout<<"change\n";
		}
		
		for(int j=0; j<n; ++j)
		{
			total_owp_count=0;
			for(int k=0; k<n; ++k)
			{
			//	cout<<"k is:: "<<k<<endl;
				if(arr_use[j][k]==-1)
				{continue;}
				else
				{
					total_owp_count+=owp[k];
				}
				//cout<<"total_owp_count:: "<<total_owp_count<<" gh"<<owp[k]<<endl;
			}
			oowp[j]= (double)total_owp_count/(double)count_total[j];
			//cout<<"change\n";
		}
		//cout<<"opponents winning percentage:\n";
		/*for(int j=0; j<n; ++j)
		{
			cout<<owp[j]<<"\t";
		}
		cout<<endl;
		//cout<<"opponents opponents winning percentage:\n";
		for(int j=0; j<n; ++j)
		{
			cout<<oowp[j]<<"\t";
		}
		cout<<endl;
		*/
		//rpi
		for(int j=0; j<n; ++j)
		{
			rpi[j]= 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j];
		}
		out<<"Case #"<<i<<":\n";
		for(int j=0; j<n; ++j)
		{
			out<<rpi[j]<<"\n";
		}
	}
	
	return 0;
}
