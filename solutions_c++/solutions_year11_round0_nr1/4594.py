
#include<fstream>
#include<string>
#include<iostream>
#include<queue>
#include<algorithm>
#include<cmath>
#include<math.h>
using namespace std;

ofstream outfile;
int T;
int N;
queue<int> way1;
queue<int> way2;
queue<int> seq;
int main()
{
freopen("A-small.in","r",stdin);
freopen("sub.out","w",stdout);
int index=1,i;
cin>>T;
while(index <=T)
{
        cin>>N;
        char data1;
        int data2,tmp1,tmp2,seqtmp,now1=1,now2=1,dist1,dist2;
        int res=0;
        for(i=0;i<N;i++)
        {
            cin>>data1>>data2;
            if(data1 =='O')
            {
                way1.push(data2);
                seq.push(0);
                
            }else
            {
                way2.push(data2);
                seq.push(1);
            }
        }
        while(!seq.empty())
        {
            if(!way1.empty())
            tmp1=way1.front();
            if(!way2.empty())
            tmp2=way2.front();
            seqtmp=seq.front();
            seq.pop();
            if(seqtmp == 0)
            {
                way1.pop();
                dist1=abs(tmp1-now1)+1;
                res+=dist1;
                now1=tmp1;
                dist2=abs(tmp2-now2);
                if(dist2 <= dist1)
                    now2=tmp2;
                else
                {
                    if(tmp2>now2)
                    now2+=dist1;
                    else
                    now2-=dist1;
                    
                }
                
            }
            else 
            {
                way2.pop();
                dist2=abs(tmp2-now2)+1;
                res+=dist2;
                now2=tmp2;
                dist1=abs(tmp1-now1);
                if(dist1 <= dist2)
                    now1=tmp1;
                else
                {
                    if(tmp1>now1)
                    now1+=dist2;
                    else
                    now1-=dist2;
                    
                }
            
            }
            
            
            
        }
        
 cout<< "Case #"<<index++<<": "<<res<<endl; 
      
    
}



return 0;

}
