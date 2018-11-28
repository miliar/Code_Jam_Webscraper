#include <iostream>
#include <fstream>

int main(int argc, char *argv[])
{
  if (argc==2)
  {
    std::ifstream input_file(argv[1]);
    std::ofstream output_file;
    output_file.open("C_output.out");
    if (input_file.is_open())
    {
      int caseCount; //number of inputs
      int A, B;
      input_file>>caseCount; //Number of cases
      for (int i=0;i<caseCount;i++)
      {
	input_file>>A; //Number of 
	input_file>>B; //Number of 
	int repliCount = 0;
	int tmp;
	for(int j=A;j<B;j++)
	{
	  int n=1;
	  while(j/n>0)
	    n*=10;
	  if(j%10!=0)
	  {
	    tmp = j/10 + (j%10)*n/10;
	    if((tmp>j)&&(tmp<=B)&&(tmp>=A))
	      repliCount++;
	  }
	  if((j>100)&&(((100*j)/n)%10!=0))
	  {
	    tmp = j%(n/10)*10 + (j)/(n/10);
	    if((tmp>j)&&(tmp<=B)&&(tmp>=A))
	      repliCount++;
	  }
	  if((j>1000)&&(j%100>=10))
	  {
	    tmp = j/100 + (j%100)*100;
	    if((tmp>j)&&(tmp<=B)&&(tmp>=A))
	      repliCount++;
 	  }
	}
	output_file<<"Case #"<<i+1<<": "<<repliCount<<std::endl;
      }
    }
    output_file.close();
    return 0;
  }
}