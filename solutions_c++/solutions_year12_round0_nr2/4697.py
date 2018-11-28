#include<iostream>
using namespace std;

int tot_points[150];

int check_lev1 (int tot_score, int min_score)
{
    if(((tot_score + 2)/3) >= min_score)
        return 1;
    else
        return 0;
}

int check_lev2 (int tot_score, int min_score)
{
    if(tot_score == 29 || tot_score == 30) return 0;
    if(tot_score == 0 || tot_score == 1) return 0;
    
    if(((tot_score + 4)/3) >= min_score)
        return 1;
    else
        return 0;
}


int main()
{    
    int num_cases;
    int cur_case = 1;
    
    int num_g;
    int num_s;
    int best_min;
    
    cin>>num_cases;
    
    while(cur_case <= num_cases)
    {
        int max_g = 0;
        
        cin>>num_g;
        cin>>num_s;
        cin>>best_min;
        
        int i;
        for(i=0;i<num_g;++i)
        {
            int tot_points;
            cin>>tot_points;
            
            if(check_lev1 (tot_points, best_min))max_g++;
            else
            {
                if(num_s>0)
                {
                    if(check_lev2(tot_points, best_min))
                    {
                        max_g++;
                        num_s--;
                    }
                }
            }
        }
        
        cout<<"Case #"<<cur_case<<": "<<max_g<<"\n";

        cur_case++;
    }
    return 0;
}
