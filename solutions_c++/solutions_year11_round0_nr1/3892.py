#include<cstdio>

int R=0;

int last_pos[2] = { 1, 1};
int time = 0;
int cur_pos;

int T, N;
char robot, last;

inline int rob(char r)
{
   if(r=='O') return 0;
   else return 1;   
}


inline int abs(int a)
{
 if (a>0) return a; 
 else return (-1)*a;     
}



int main()
{
    scanf("%d", &T);
    for(int i=0;i<T;i++)
    {
           
            scanf("%d", &N);
            time = 0;
            last_pos[0]=last_pos[1]=1;
            R=0;
            
            for(int j=0;j<N;j++)
            {
                    scanf(" %c %d", &robot, &cur_pos);
                    if(j==0) last=robot;
                    
                    if(last == robot)
                    {
                           time+=abs(last_pos[rob(robot)] - cur_pos) + 1;
                           R+=abs(last_pos[rob(robot)] - cur_pos) + 1;
                    }      
                    else
                    {
                            if(R>=abs(last_pos[rob(robot)] - cur_pos))
                            {
                                             time++;      
                                             R=1;                                                                    
                            }     
                            else
                            {
                                             time+=abs(last_pos[rob(robot)] - cur_pos) - R + 1;
                                             R=abs(last_pos[rob(robot)] - cur_pos) - R + 1;
                            }
                            

                            
                    }
                   // printf("Time: %d, j: %d, robot: %c, cur_pos: %d, R: %d \n", time, j, robot, cur_pos, R);

                    
                    last = robot;
                    last_pos[rob(robot)] = cur_pos; 
                    
             }
            
            printf("Case #%d: %d\n", i+1, time);        
    }
    
   // scanf(" %c", &robot);
    return 0;
}
