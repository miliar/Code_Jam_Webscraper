#include<stdio.h>
#include<fstream>
using std::ofstream;
using std::ifstream;
using std::ios;
int main()
{
	int cases_no,Googlers_no,Surprising,min_score,triplet_Score,counter,max_index;
	int judges[3];
	int min,max;
	ifstream in("B-large.in",ios::in);
	ofstream out("output.txt",ios::out);
	if ( ! in ) 
		printf("error in openning ip file");
	if ( ! out ) 
		printf("error in openning op file");

	in>>cases_no;
	
	for(int i=0;i<cases_no;i++)
	{
		counter=0;
		in>>Googlers_no>>Surprising>>min_score;
		for(int j=0;j<Googlers_no;j++)
		{
			in>>triplet_Score;
			judges[0]=triplet_Score/3;
			judges[1]=(triplet_Score-judges[0])/2;
			judges[2]=(triplet_Score-judges[0]-judges[1]);

			//check surprising or not
			min=judges[0];
			max=judges[0];
			max_index=0;
			
			for(int k=1;k<3;k++)
			{
				if(judges[k]<min)
				{
					min=judges[k];
				}
				if(judges[k]>max)
				{
					max=judges[k];
					max_index=k;
				}
			}
			
			if((max-min)>2)
			{
				printf("error in score %d+%d+%d=%d\n",judges[0],judges[1],judges[2],triplet_Score);
			}
			else if((max-min)==2)
			{
				if(Surprising>0)
					Surprising--;
				else
					printf("error in no of surprising score %d+%d+%d=%d\n",judges[0],judges[1],judges[2],triplet_Score);
			}
			//check any combination for min score
			if(max<min_score)
			{
				if(Surprising>0)
				{
					if((max-min)==0 && (min_score-max)==1 && max!=0)
					{
						counter++;
						Surprising--;
					}
					else if((max-min)==1 && (min_score-max)==1)
					{
						if(max_index==0 && (judges[max_index]==judges[1] ||judges[max_index]==judges[2] ))
						{
							counter++;
							Surprising--;
						}
						else if(max_index==1 && (judges[max_index]==judges[0] ||judges[max_index]==judges[2] ))
						{
							counter++;
							Surprising--;
						}
						else if(max_index==2 && (judges[max_index]==judges[0] ||judges[max_index]==judges[1]))
						{
							counter++;
							Surprising--;
						}
						
					}
				}
			
			}
			else
				counter++;

		}

		out<<"Case #"<<i+1<<": "<<counter<<'\n';
	}
	return(0);
}