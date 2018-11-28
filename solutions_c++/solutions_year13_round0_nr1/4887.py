#include<stdio.h>
#include<iostream>

int main()
{
	int T,Ai,j,k;
	
	
	std::cin>>T;
	for(Ai=0;Ai<T;Ai++)
	{
	std::cout<<"Case #"<<Ai+1<<": ";
	bool incomplete=false;	
	char arr[4][4];
	char emptyline;
	char status='U';
		for(j=0;j<4;j++)
		{
			bool flag=false;
			
			bool fx=false,fo=false,fd=false,ft=false;
			for(int k=0;k<4;k++)
			{
				
				std::cin>>arr[j][k];
				switch(arr[j][k])
				{
					case 'X':fx=true;
							break;
					case 'O':fo=true;
							break;
					case '.':fd=true;
							incomplete=true;
							break;
					case 'T':ft=true;
							break;

				}
	
			}
			if(!fo && !fd)
				status='X';
			else if(!fd && !fx)
				status='O';

			
		}
	for(j=0;j<4;j++)
	{
		bool flag=true;
		
		bool fx=false,fo=false,fd=false,ft=false;
		for(k=0;k<4;k++)
		{
				switch(arr[k][j])
				{
					case 'X':fx=true;
							break;
					case 'O':fo=true;
							break;
					case '.':fd=true;
							break;
					case 'T':ft=true;
							break;

				}
		}
		
			if(!fo && !fd)
				status='X';
			else if(!fd && !fx)
				status='O';

		
	}
	bool afx=false,afo=false,afd=false,aft=false;
		
	for(int i=0;i<4;i++)
	{
				switch(arr[i][i])
				{
					case 'X':afx=true;
							break;
					case 'O':afo=true;
							break;
					case '.':afd=true;
							break;
					case 'T':aft=true;
							break;

				}
	}
			if(!afo && !afd)
				status='X';
			else if(!afd && !afx)
				status='O';	
			afx=false,afo=false,afd=false,aft=false;
for(int i=0;i<4;i++)
	{
				switch(arr[i][3-i])
				{
					case 'X':afx=true;
							break;
					case 'O':afo=true;
							break;
					case '.':afd=true;
							break;
					case 'T':aft=true;
							break;

				}
	}
			if(!afo && !afd)
				status='X';
			else if(!afd && !afx)
				status='O';	
switch(status)
	{
	case 'X': std::cout<<"X won\n";
		break;
	case 'O': std::cout<<"O won\n";
		break;
	default:
		if(!incomplete)
			std::cout<<"Draw\n";
		else if(incomplete)
			std::cout<<"Game has not completed\n";
		break;
	}

	
	}
	return (0);
}