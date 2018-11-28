#include<iostream>
#include<vector>

#include<algorithm>

struct pair
{
	char name;
	int value;
	bool operator==(pair t)
	{
		if(t.name==name)return true;
		return false;
	}
};

int main()
{
	

typedef std::vector<pair>::iterator I;
 pair tempO,tempB;
 tempB.name='B';
 tempO.name='O';
	int n;
	std::cin>>n;
	for(int k=0;k<n;++k)
	{
	int s;
	std::cin>>s;
	std::vector<pair>pv(s);
	
	char c=0;
	int v =0;
	

	for(int i=0;i<s;++i)
	{
		std::cin>>c;
		std::cin>>v;
		pv[i].name=c;
		pv[i].value=v;
	}
		
	int time=0;
	int posO=1;
	int posB=1;
	
	size_t i=0;
	while(i<pv.size())
	{
		if(pv[i].name=='O')
		{
			if(posO<pv[i].value)
			{
				posO++;

			}
				else 
					if(posO>pv[i].value)
						{
							posO--;
						}
						else
						{
							++i;
							
							
						}
					
					I pp=std::find(pv.begin()+i,pv.end(),tempB);
					if(pp==pv.end())
					{
						time++;
					continue;
					}
			else
			{
				if((*pp).value>posB)
					posB++;
				else if((*pp).value<posB)
					posB--;

			}
					time++;
					continue;
		}
		
		if(pv[i].name=='B')
		{
			if(posB<pv[i].value)
			{
				posB++;

			}
			else if(posB>pv[i].value)
			{
				posB--;
			}
			else
			{
				++i;
			
			}
			I pp=std::find(pv.begin()+i,pv.end(),tempO);
			if(pp==pv.end())
			{	time++;
				continue;
				
			}
			else
			{
				if((*pp).value>posO)
					posO++;
				else if((*pp).value<posO)
					posO--;

			}



		}

	time++;
	}
	
			
	std::cout<<"Case #"<<k+1<<": "<<time<<std::endl;	
	
}
	return 0;
}