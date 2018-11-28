#include <iostream>
#include <fstream>
#include <cstring>
#include <deque>

__int64 theme_park(__int64 r /*No of trips*/, __int64 k /*Number of people*/, __int64 n /*number of groups*/, std::deque<__int64> * v_int)
{
	__int64 total_vector_sum=0;
	__int64 vector_sum=0;
	while(r>0)
	{
		vector_sum=0;
		int i=0;
		while(vector_sum<k && i< n)
		{
			 vector_sum+=v_int->at(i++);

			 if(vector_sum==k)
			 {
				 for(int j=0;j<i;j++)
				 {
					 __int64 val=v_int->at(0);
					 v_int->pop_front();
					 v_int->push_back(val);
				 }
				 break;
			 }

			 else if(vector_sum>k)
			 {
				 i=i-1;
	 			 vector_sum-=v_int->at(i);
				 
				 for(int j=0;j<i;j++)
				 {
					 __int64 val=v_int->at(0);
					 v_int->pop_front();
					 v_int->push_back(val);
				 }
				 break;
			 }
		}
		r--;
		total_vector_sum+=vector_sum;
	}
	return total_vector_sum;
}

int main()
{
	char * line1=new char(50);
	char * line1_part1=new char(25);
	char * line1_part2=new char(25);
	char * line1_part3=new char(25);
	
	char * line2=new char(10);

	std::fstream fileOp("C-small-attempt0.in",std::ios::in);
	std::fstream output("C-small-attempt0.out",std::ios::out);
	fileOp.getline(line1,50);
	int numofInputs=atoi(line1);

	for(int i=1;i<=numofInputs;i++)
	{
		std::deque<__int64> v_int;
		memset(line1,0,49);
		fileOp.getline(line1,100);
		int ctr=0;
		int len=strlen(line1);
				
		memset(line1_part1,0,24);

		while(*(line1+ctr) != ' ')
		{
			*(line1_part1+ctr)=*(line1+ctr);
			ctr++;
		}

		ctr++;
		int ctr1=0;
		memset(line1_part2,0,24);
		
		while(*(line1+ctr) != ' ')
		{
			*(line1_part2+ctr1)=*(line1+ctr);
			ctr++;
			ctr1++;
		}
		
		ctr++;
		ctr1=0;

		memset(line1_part3,0,24);

		while(ctr<len)
		{
			*(line1_part3+ctr1)=*(line1+ctr);
			ctr++;
			ctr1++;
		}

		__int64 r=atoi(line1_part1);
		__int64 k=atoi(line1_part2);
		__int64 n=atoi(line1_part3);

		int cnt=0;
		__int64 _n=n;
		while( _n>0)
		{
			memset(line2,0,9);

			while( (*(line2+cnt++)=fileOp.get()) != ' ' && (fileOp.peek() != '\n') && (fileOp.peek() != EOF) )
			{
				//deliberate empty statement
			}

			*(line2+cnt)='\0';
			int len1=strlen(line2);

			v_int.push_back(atoi(line2));

			cnt=0;
			_n--;
		}
		fileOp.get();
		__int64 amount=theme_park(r,k,n, &v_int);

		output<<"Case #"<<i<<": "<<amount<<'\n';

	}
	fileOp.close();
	output.close();
	system("PAUSE");
}