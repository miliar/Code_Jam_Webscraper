#include <iostream> 
#include <fstream>
using namespace std; 

int main() { 
 int T;
 char R[100];
 int P[100];
 int tests;
 ifstream input("A-large.in");
 ofstream output("A-large.out");
 input >> tests;
 
 for (int j=0;j<tests;j++)
 {
 
 input >> T;
 for (int i=0;i<T;i++)
 {
	input >> R[i];
	input >> P[i];
 }
 
 int O_current=1;
 int B_current=1;
 int B_target;
 int O_target;
 int time=0;
 int task=0;
 
 while(task<T)
 {
	 for (int i=task;i<T;i++)
	{
		if (R[i]=='O')
		{
			O_target=P[i];
			break;
		}
	}
	for (int i=task;i<T;i++)
	{
		if (R[i]=='B')
		{
			B_target=P[i];
			break;
		}
	}
	
	if (R[task]=='O')
	{
		if (O_target>O_current)
			O_current++;
		else if (O_target<O_current)
			O_current--;
		else
			task++;
		
		if (B_target>B_current)
			B_current++;
		else if (B_target<B_current)
			B_current--;
	}
	else
	{
		if (B_target>B_current)
			B_current++;
		else if (B_target<B_current)
			B_current--;
		else
			task++;
			
		if (O_target>O_current)
			O_current++;
		else if (O_target<O_current)
			O_current--;
	}
	time++;
 }
 
 
 


 output << "Case #" << (j+1) << ": " << time  << "\n"; 
}

 return 0; 
}
