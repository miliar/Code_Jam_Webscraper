//Google Jam 2010 - Problem 3 - Qualification Roun

#include <iostream> 
#include <cmath> 
#include <vector> 
#include <string> 
#include <map> 
#include <iomanip>
#include <queue>

using namespace std;

queue<int> groups;

int main()
{
    int T, R, k, n, m;
    cin>>T;
    int next;
    for(int i = 0; i < T; i++)
    {
        cin>>R>>k>>n;
        for(int j = 0; j < n; j++)
        {
            cin>>m;
            groups.push(m);   
        }
        
        int total = 0;
        
        //printf("%i %i %i", R, k, n);
        
        int size = 0; //How many groups are already in the roller
        
        for(int j = 0; j < R; j++)
        {
            int leave = k;
            size = 0;
            for(;;)
            {
                next = groups.front();
                if( (leave - next) >= 0 && size < groups.size())
                {
                    leave -= next;
                    groups.pop();
                    groups.push(next);
                    size++;
                }
                else
                    break;
            }
            
            total += k - leave;
        }
        
        while(!groups.empty())
        {
            groups.pop();   
        }
        
        cout<<"Case #"<<i+1<<": "<<total<<endl;
    }
}
