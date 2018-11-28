#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main1(void)
{
	vector<std::size_t> nos;
	std::size_t no,nono=0,sum=0;
	std::size_t P,K,L;
	std::cin>>P>>K>>L;
	
	while(nono<L)
	{
		cin>>no;
		nos.push_back(no);
		nono++;
	}
	sort(nos.begin(),nos.end());
	for(std::size_t i=0;i<L;i++)
	{
		sum+=nos[L-i-1] * (i/K+1);
//		std::cout<<nos[L-i-1]<<" "<<(i/K+1)<<std::endl;
	}
	std::cout<<sum<<std::endl;	
	return 0;
}

int main(void)
{
	int N;
	int i=0;
	cin>>N;
	while(i<N)
	{
		i++;
		std::cout<<"Case #"<<i<<": ";
		main1();
	}
}
