#include<iostream>
#include<vector>

std::vector<std::pair<int,int>> vines;
int N,D;
bool foo(int pt,int len)
{
	if(vines[pt].first+len >= D) return true;
	int next = 1;
	for(;;next++)
	{
		if(pt+next==vines.size())
		{
			next--;
			break;
		}
		if(vines[pt+next].first > vines[pt].first+len)
		{
			next--;
			break;
		}
	}
	if(next<1) return false;
	int nextlen;
	while(next>0)
	{
		if(vines[pt+next].first-vines[pt].first>vines[pt+next].second) nextlen = vines[pt+next].second;
		else nextlen = vines[pt+next].first-vines[pt].first;
		if(foo(pt+next,nextlen)) return true;
		next--;
	}
	return false;
}
int main()
{
	int T;
	std::cin>>T;

	for(int t=1;t<=T;t++)
	{
		std::cin>>N;
		vines.clear();
		int td,tl;
		for(int i=0;i<N;i++)
		{
			std::cin>>td>>tl;
			vines.push_back(std::pair<int,int>(td,tl));
		}
		std::cin>>D;
		if(foo(0,vines[0].first))std::cout<<"Case #"<<t<<": YES"<<std::endl;
		else std::cout<<"Case #"<<t<<": NO"<<std::endl;
	}
	return 0;
}