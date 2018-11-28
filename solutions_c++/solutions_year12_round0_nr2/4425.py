#include<stdio.h>
#include<vector>
typedef struct{
	int small;
	int middle;
	int big;
	bool suprise;
	bool satisfy;
	int remain;
}Dancer;

void process(Dancer &dancer,int least)
{
	if(dancer.remain==0)
	{		
		if(dancer.big+1>=least && dancer.satisfy!=0)
		{
			dancer.big++;
			dancer.small--;
			dancer.suprise=true;
			dancer.satisfy=true;
		}
		else if(dancer.big>=least)
		{
			dancer.suprise=false;
			dancer.satisfy=true;
		}
		else
		{
			dancer.suprise=false;
			dancer.satisfy=false;
		}
	}
	else if(dancer.remain==1)
	{
		dancer.big++;
		dancer.remain=0;
		if(dancer.big>=least)
		{
			dancer.suprise=false;
			dancer.satisfy=true;				
		}
		else
		{
			dancer.suprise=false;
			dancer.satisfy=false;
		}
	}
	else if(dancer.remain==2)
	{
		if(dancer.small>=least)
		{
			dancer.big++;
			dancer.middle++;
			dancer.remain=0;
			dancer.satisfy=true;
			dancer.suprise=false;
		}
		else if(dancer.big+2>=least)
		{
			dancer.big+=2;
			dancer.remain=0;
			dancer.satisfy=true;
			dancer.suprise=true;
		}
		else
		{
			dancer.big++;
			dancer.middle++;
			dancer.remain=0;
			dancer.satisfy=false;
			dancer.suprise=false;
		}

	}
	
}

void main()
{
	FILE* file,*output;
	file=fopen("data\\B-small-attempt2.in","rb");
	output=fopen("data\\B-small-attempt2.in.output","wt+");
	int n_case,n_person,n_suprise,n_least;
	Dancer* dancers;
	fscanf(file,"%d",&n_case);
	for(int i=0;i<n_case;i++)
	{
		fscanf(file,"%d",&n_person);
		fscanf(file,"%d",&n_suprise);
		fscanf(file,"%d",&n_least);
		dancers=new Dancer[n_person];
		std::vector<Dancer*> list_satisfy;
		std::vector<Dancer*> list_unsatisfy;
		std::vector<Dancer*> list_suprise;
		std::vector<Dancer*> list_unsuprise;
		for(int j=0;j<n_person;j++)
		{
			int temp;
			fscanf(file,"%d",&temp);
			dancers[j].small=dancers[j].middle=dancers[j].big=temp/3;
			dancers[j].remain=temp%3;
			dancers[j].satisfy=false;
			dancers[j].suprise=false;
			process(dancers[j],n_least);
			if(dancers[j].satisfy)
				list_satisfy.push_back(&dancers[j]);
			else
				list_unsatisfy.push_back(&dancers[j]);
			if(dancers[j].suprise)
				list_suprise.push_back(&dancers[j]);
			else
				list_unsuprise.push_back(&dancers[j]);
		}
		int n_num=list_suprise.size()-n_suprise;
		if(n_num>0)
		{
			std::vector<Dancer*>::iterator itr=list_suprise.begin();
			while(itr!=list_suprise.end())
			{
				bool flag=false;
				if((*itr)->satisfy)
				{
					if((*itr)->big-1>=n_least)
					{
						(*itr)->big--;
						(*itr)->small++;
						(*itr)->suprise=false;
						list_unsuprise.push_back(*itr);
						itr=list_suprise.erase(itr);
						
						flag=true;									
						n_num--;
						if(n_num==0)
							break;
					}
				}
				
				if(!flag)
					itr++;
				else 
					itr;
			}
			itr=list_suprise.begin();
			
			while(itr!=list_suprise.end() && n_num!=0)
			{
				bool flag=false;
				(*itr)->big--;
				(*itr)->small++;
				(*itr)->suprise=false;
				list_unsuprise.push_back(*itr);
				
				
				if((*(itr))->satisfy)
				{
					(*itr)->satisfy=false;
					list_unsatisfy.push_back(*itr);	
					std::vector<Dancer*>::iterator itrtmp;
					for(itrtmp=list_satisfy.begin();itrtmp!=list_satisfy.end();itrtmp++)
						if((*itrtmp)==(*itr))
						{	itrtmp=list_satisfy.erase(itrtmp);
							break;
						}

					
				}
				itr=list_suprise.erase(itr);
				flag=true;
				n_num--;
				if(n_num==0)
					break;
				if(!flag)
					itr++;
				else
					itr;
			}		
		}
		else if(n_num<0)
		{
			std::vector<Dancer*>::iterator itr=list_unsuprise.begin();
			while(itr!=list_unsuprise.end())
			{
				bool flag=false;
				if((*itr)->big == (*itr)->middle && (*itr)->big!=0)
				{
					(*itr)->middle--;
					(*itr)->big++;
					(*itr)->suprise=true;
					list_suprise.push_back(*itr);
					if((*itr)->big>=n_least && (*itr)->satisfy==false)
					{
						(*itr)->satisfy=true;
						list_satisfy.push_back(*itr);
						std::vector<Dancer*>::iterator itrtmp;
						for(itrtmp=list_unsatisfy.begin();itrtmp!=list_unsatisfy.end();itrtmp++)
							if((*itrtmp)==(*itr))
							{	
								itrtmp=list_unsatisfy.erase(itrtmp);
								break;
							}
					}
						itr=list_unsuprise.erase(itr);
					n_num++;
					if(n_num==0)
						break;
					flag=true;
				}
				if(!flag)
					itr++;
			}
		}
		fprintf(output,"Case #%d: %d",i+1,list_satisfy.size());
		fprintf(output,"\n");
		list_satisfy.clear();
		list_unsatisfy.clear();
	}
	fclose(file);
	fclose(output);
	
}