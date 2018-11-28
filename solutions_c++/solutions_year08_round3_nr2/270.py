#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int main1(void)
{
	string str;
	std::size_t size;
	std::size_t array[210][50];
	std::size_t mods[50][50];
	
	for(std::size_t i=0;i<210;i++)
		for(std::size_t j=0;j<50;j++)
			array[i][j]=0;

	for(std::size_t i=0;i<50;i++)
		for(std::size_t j=0;j<50;j++)
			mods[i][j]=0;

	std::cin>>str;
	size=str.size();
	
	//std::cout<<"size:"<<size<<std::endl;
	
	for(std::size_t i=0;i<size;i++)
	{
		for(std::size_t j=0;j<i;j++)
			 mods[i][j]=(mods[i-1][j]*10+str[i]-'0')%210;
			
		mods[i][i]=str[i]-'0';
		//std::cout<<"here "<<mods[0][i]<<" "<<std::endl;
	}
	
	
	for(std::size_t i=0;i<size;i++)
	{
		
		for(std::size_t j=0;j<=i;j++)
		{
			std::size_t sub_mod=mods[i][j];
			if(j==0) 
			{
				array[(sub_mod)%210][i]+=1;
				continue;
			}

			for(std::size_t k=0;k<210;k++)
			{
				array[(k+sub_mod)%210][i]+=array[k][j-1];
				array[(k-sub_mod+210)%210][i]+=array[k][j-1];
			}
		}
	}
	
	//for(std::size_t i=0;i<size;i++)
	//{
		//for(std::size_t j=0;j<210;j++)
			//std::cout<<array[j][i]<<" ";
		//std::cout<<" :"<<std::endl;
		
	//}
	
	std::size_t sum=0;
	for(std::size_t i=0;i<210;i++)
	{
		if(i%2==0 || i%3==0 || i%5==0 || i%7==0 )
		{
			sum+=array[i][size-1];
			//std::cout<<sum<<std::endl;
		}
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
