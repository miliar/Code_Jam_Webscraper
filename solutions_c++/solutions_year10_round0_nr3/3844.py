#include <stdio.h>

int main (int argc, char* argv[])
{
    unsigned int GroupsAmount[1000];
    char infilename[] = "C-small-attempt0.in";
    char outfilename[] ="C-small.out";
    FILE* infile = fopen(infilename,"r");
    FILE* outfile = fopen(outfilename,"w");
    int NumberOfCases=0;
    fscanf(infile,"%d",&NumberOfCases);
    unsigned int Rides;
    unsigned Capacitance;
    int GroupCount;
    for (int i=0; i<NumberOfCases; i++)
    {
        
        fscanf(infile,"%d",&Rides);
        fscanf(infile,"%d",&Capacitance);
        fscanf(infile,"%d",&GroupCount);
       
        for (int I=0; I<GroupCount; I++)
        {
            int tmp;
            fscanf(infile,"%d",&tmp);
            GroupsAmount[I] = tmp;
        }

        int GlobalIndex = 0;
        double TotalAmount = 0.0;

        for (unsigned int j=0; j<Rides;j++)
        {
            unsigned int AmountInCurrentRide=GroupsAmount[GlobalIndex];
            int CurrentIndex = (GlobalIndex+1) % GroupCount;
            
            while (((AmountInCurrentRide+GroupsAmount[CurrentIndex])<=Capacitance) && (CurrentIndex!=GlobalIndex))
            {
                AmountInCurrentRide+=GroupsAmount[CurrentIndex];
                ++CurrentIndex;
                CurrentIndex = CurrentIndex % GroupCount;
            }
            TotalAmount+=AmountInCurrentRide;
     
            GlobalIndex = (CurrentIndex % GroupCount);
        }

        fprintf(outfile,"Case #%d: %.0f\n",(i+1), TotalAmount);
    }
    
  
    fclose(infile);
    fclose(outfile);
    return 0;
}