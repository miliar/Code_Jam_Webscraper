#include <cstdlib>
#include <iostream>

using namespace std;


int main(int argc, char *argv[])
{
    
    freopen("C-large.in", "r", stdin);
    freopen("Solution.txt", "w", stdout);
    
    
    int num_testcases;
    //Store the group sizes
    int group_sizes[1000];
    
    scanf("%d ", &num_testcases);
    
    int cap, num_rounds, num_groups;
    
    
    for(int  i = 1; i <= num_testcases; i++)
    {
             
             scanf("%d %d %d ", &num_rounds, &cap, &num_groups);
             
             //Scan groups
             for(int j = 0; j <num_groups; j++)
             {
                     scanf("%d ", &group_sizes[j]);
             }
             
             
             //Precalculation
             //This matrix stores the maximum number of persons
             //which can take the next ride, and the number of the
             //group to be the first afterwards 
             int next_group[1000][2];
             bool calc[1000];
             for(int j = 0; j < 1000; j++) calc[j] = false;
             
             int j = 0;
             while(calc[j] == false)
             {
                     //At least on group fits always
                     int sum = group_sizes[j];
                     //Starting point
                     int count = j;
                     //Check, whether the next group fits into the rollercoaster
                     while((sum + group_sizes[(count + 1)% num_groups]) <= cap && (count + 1)% num_groups != j)
                     {
                                //This group fits into the rollercoaster
                                sum += group_sizes[(count + 1)% num_groups];
                                //One more group
                                count++;
                     } 
                     
                     //How many Euros
                     next_group[j][0] = sum;
                     //Next group to be the first one
                     next_group[j][1] = (count + 1) % num_groups;
                     calc[j] = true;
                     j = (count + 1) % num_groups;
             }
             
             
             //After at most num_groups rounds everything starts again
             bool before[1000];
             for(j = 0; j < 1000; j++) before[j] = false;
             
             int last_count[1000];
             long long euros = 0;
             int rcount = 1;
             int pos;
             pos = 0;
             
             while(rcount <= num_rounds){
             
                          //Circle found
                          if(before[pos] == true)
                          {
                           
                           int dif = rcount - last_count[pos];
                           int times = (num_rounds - rcount + 1) / dif;
                           int resid = (num_rounds - rcount + 1) % dif;
                           
                           euros += times * next_group[pos][0];
                           //Deal with the remaining rounds
                           for(j = 0; j < resid; j++)
                           {
                              //Euros gained in this round
                              euros += next_group[pos][0];
                              //Next skip
                              pos = next_group[pos][1];   
                           }
                           
                           
                           //Finish it
                             break;                
                          }
                          
                          //No we have had this situation
                          before[pos] == true;
                          //To remember the difference
                          last_count[pos] = rcount;
                          //Euros gained in this round
                          euros += next_group[pos][0];
                          //Next skip
                          pos = next_group[pos][1]; 
                                           
                          //Next round
                          rcount += 1;         
             }
             
             printf("Case #%d: %lld\n", i, euros);
             
    }
    return 0;
}
