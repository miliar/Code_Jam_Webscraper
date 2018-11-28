#include <stdio.h>
#define SIZE 102
#define abs(x) ((x)>(-1*(x))?(x):(-1*(x)))

int task[SIZE],n,curPos[2],tolTime,next[2][SIZE],ONum,BNum;
int oid,bid;
void Init()
{
     curPos[0]=1;//Orange
     curPos[1]=1;//Blue
     tolTime=0;
     ONum=0;
     BNum=0;
     oid=0;
     bid=0;
}
int GetNext(int id)
{
     //printf("GetNext(%d)\n",id);
	 //printf("%d,%d,%d,%d\n",oid,ONum,bid,BNum);
	 if(id) 
	 {
		 if(bid > BNum) bid--;
		 else return next[1][bid];
	 }
     else 
	 {
		 if(oid == ONum) oid--;
		 else return next[0][oid]; 
	 }
}
int GetPos(int cur,int will,int delta)
{
     //printf("GetPos(%d,%d,%d)\n",cur,will,delta);
	 if(will>cur) return cur+delta;
	 else if(will == cur) return cur;
     return cur-delta;   
}
void aStepJob(int i)
{
     //printf("task:%d\n",i);
	 int id=(task[i]>0)?1:0;
     int tCost=abs(abs(task[i])-curPos[id])+1;
     int id2=(task[i]<0)?1:0;
     int NextTask=GetNext(id2);
	 //printf("Nexttask=%d\n",NextTask);
     int tCost2=abs(abs(task[NextTask])-curPos[id2]);
	 //printf("tCost=%d,tCost2=%d\n",tCost,tCost2);
     if(tCost>=tCost2)
     {
          curPos[id2]=abs(task[NextTask]);                
     }
     else curPos[id2]=GetPos(curPos[id2],abs(task[NextTask]),tCost);
     tolTime+=tCost;
	 //printf("task[%d],%d\n",i,tCost);
	 curPos[id]=abs(task[i]);
	 //printf("orange=%d,Blue=%d\n",curPos[0],curPos[1]);
     if(id) bid++;
	 else oid++;
}
int main()
{
     int test,i,t_id=1;
     char robot;
    // freopen("A-small.out", "w", stdout);
   // freopen("A-small.in","r",stdin);
    freopen("A-large.in","r",stdin);
	freopen("A-large.out", "w", stdout);
     scanf("%d",&test);
     while(test--)
     {
          scanf("%d%*c",&n);
         // printf("n=%d\n",n);
          Init();
          for(i=0;i<n;++i)
          {
              scanf("%c%d%*c",&robot,task+i);
             // printf("%c,%d\n",robot,task[i]);
              if(robot=='O')  
              {
                    task[i]*=-1;//Orange对应任务设为负
                    next[0][ONum++]=i; 
              } 
              else next[1][BNum++]=i;              
          }
          for(i=0;i<n;++i)
              aStepJob(i);
          printf("Case #%d: %d\n",t_id++,tolTime);             
     }    
	 fclose(stdout);
	 fclose(stdin);
     //scanf("%d",&test);
     return 0;
}
