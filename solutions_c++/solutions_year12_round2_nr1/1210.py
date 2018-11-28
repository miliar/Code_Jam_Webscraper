#include <fstream>

using namespace std;

ifstream fin("safe.in");
ofstream fout("safe.out");

#define MAX_N 202

int main()
{
    int num_of_cases;
	int n;
	int s[MAX_N];
	int id[MAX_N];
	int partial_sum[MAX_N];
	double ans[MAX_N];
	double real_ans[MAX_N];

	fin>>num_of_cases;
	
	for (int i=1;i<=num_of_cases;i++)
	{
		fin>>n;
		int j,Y=0;
		for (j=0;j<n;j++) 
			{
				fin>>s[j];
				Y +=s[j];
				id[j]=j;
		     }

		int k;
		int temp;

		for (j=n-2;j>=0;j--)
		  for (k=0;k<=j;k++)
			if (s[k]>s[k+1])
			{
		       temp=s[k];
			   s[k]=s[k+1];
			   s[k+1]=temp;
			   temp=id[k];
			   id[k]=id[k+1];
			   id[k+1]=temp;
			}

        partial_sum[0]=s[0];
		for (j=1;j<n;j++) partial_sum[j]=partial_sum[j-1]+s[j];
		int sum_others,p,score_next;
		double ave;

		for (j=0;j<n;j++)
		{
			for (k=0;k<n;k++)
			{
				if (k<j) {sum_others=partial_sum[k]; p=k+2;} else {sum_others=partial_sum[k]-s[j]; p=k+1;}
				ave=(sum_others*1.0+s[j]+Y)/p/1.0;
				if (k>=n-1 || k>=n-2 && j==n-1) score_next=1000;
				else if (j==k+1) score_next=s[k+2];
				else score_next=s[k+1];
                if (ave<=s[j]) 
				{
						ans[j]=0;
						break;
				}
				else if (ave<=score_next)
				{
					ans[j]=(ave-s[j])/Y;
					break;
				}
				
			}
		}

		for (j=0;j<n;j++)
			real_ans[id[j]]=ans[j]*100;
		fout<<"Case #"<<i<<":";
		for (j=0;j<n;j++)
			fout<<" "<<real_ans[j];
		fout<<endl;
	}
	return 0;
}