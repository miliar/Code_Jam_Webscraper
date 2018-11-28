#include <cstdio>
#include <cstdlib>
#include <queue>

using namespace std;


int t,k,r,n,tmp;
unsigned long long sum,sumr;
int main()
{
    scanf("%d", &t);
    
    for(int i = 0; i < t; ++i)
    {
        queue<int> line;
        queue<int> roll;
        scanf("%d %d %d",&r,&k,&n);
        for(int _ = 0; _<n;++_)
        {
            scanf("%d",&tmp);
            line.push(tmp);
            
        }   
        sum = 0;
        sumr = 0;
        for(int _=0;_<r;++_)
        {

            while((sumr+line.front() <= k)&&(!line.empty()))
            {
                
                roll.push(line.front());
                sumr+=line.front();
                line.pop();                  
            }
            sum += sumr;
            sumr = 0;
            while(!roll.empty())
            {
                line.push(roll.front()); 
                roll.pop();                 
            }
            
        }
        printf("Case #%d: %d\n",i+1,sum);
        
        
    }
    
    
    return 0;
}
