#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int find_max_sum(const vector<int> &to_check)
{
	int sum = 0;
	int xor_tot = 0;
	
	for(size_t cnt = 0; cnt < to_check.size(); cnt++)
		xor_tot ^= to_check[cnt];
		
	if(!xor_tot)
		for(size_t cnt = 1; cnt < to_check.size(); cnt++)
			sum += to_check[cnt];
		
	return sum;
}

int main(int argc, char *argv[])
{
	FILE *fp = fopen(argv[1],"r");
	
	int tot_cases;
	fscanf(fp,"%d",&tot_cases);
	
	for(int outcnt = 1; outcnt <= tot_cases ; outcnt++)
	{
		int tot_num;
					
		fgetc(fp);
		fscanf(fp,"%d",&tot_num);
		
		vector<int> tempv(tot_num,0);
		
		for(int cnt = 0; cnt < tot_num; cnt++)
		{
			fgetc(fp);
			fscanf(fp,"%d",&tempv[cnt]);
		}
		
		int sum = 0;
		sort(tempv.begin(),tempv.end());
		sum = find_max_sum(tempv);
		
		cout<<"Case #"<<outcnt<<": ";
		sum?cout<<sum:cout<<"NO";
		cout<<endl;
	}
	
	fclose(fp);

	return 0;
}
