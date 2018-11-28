#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <queue>
#include <iostream>
#include <algorithm>


using namespace std;
struct node 
{
	int RED,BLUE;
	int point;
	//node(){point=1;}
};
struct data
{
	string clr;
	int B;
};
//printf(">> R %d B %d P %d (%d)\n",temp.RED,temp.BLUE,temp.point,cnt+1);
#define NOTVIS vis[temp.RED][temp.BLUE][temp.point]==false
#define VISANDPUSH vis[temp.RED][temp.BLUE][temp.point]=true; 	waitQ.push(temp);  if(temp.point==Q+1){found=1;break;}
#define VALID temp.RED>=1 && temp.RED<=100 && temp.BLUE>=1 && temp.BLUE<=100
int main()
{
	//freopen("in","r",stdin);
   //freopen("out","w",stdout);
	int T,kas=0;
	cin>>T;
	while(T--)
	{
		vector<data>VW;
		int Q;
		cin>>Q;
		data dtemp;
		VW.push_back(dtemp);
		for(int i=1;i<=Q;i++)
		{
			string S;
			int val;
			
			cin>>S>>val;
			//cout<<i<<">>>"<<S<<" "<<val<<endl;
			dtemp.clr=S; dtemp.B=val;
			VW.push_back(dtemp);
		}
		
		queue<node>actQ,waitQ;
		node temp;
		bool vis[101][101][101];
		memset(vis,0,sizeof(vis));
		temp.RED=1; temp.BLUE=1; temp.point=1;	
		vis[1][1][1]=true;
		actQ.push(temp);
		int found=0;
		int cnt=0;
	 while(1)
	 {
		while(!actQ.empty())
		{
			node top=actQ.front(); actQ.pop();
			
			///both wait,RED trying to do the next work if possible
			temp.RED=top.RED; temp.BLUE=top.BLUE; temp.point=top.point;
			if(VW[temp.point].clr=="O" and VW[temp.point].B==temp.RED)
			{
				temp.point++;
			    if(NOTVIS){	VISANDPUSH;}
			}
			///both wait,BLUE trying to do the next work if possible		
			temp.RED=top.RED; temp.BLUE=top.BLUE; temp.point=top.point;
			if(VW[temp.point].clr=="B" and VW[temp.point].B==temp.BLUE)
			{
				temp.point++;
			    if(NOTVIS){	VISANDPUSH;}
			}
		      
		    
		    ///Blue moves forward,RED try
		    temp.RED=top.RED; temp.BLUE=top.BLUE+1; temp.point=top.point;
		    if(VALID)
		    {
				if(VW[temp.point].clr=="O" and VW[temp.point].B==temp.RED) temp.point++;
				if(NOTVIS){	VISANDPUSH;}
			}
		    ///Blue moves back,RED try
		    temp.RED=top.RED; temp.BLUE=top.BLUE-1; temp.point=top.point;
		    if(VALID)
		    {
				if(VW[temp.point].clr=="O" and VW[temp.point].B==temp.RED) temp.point++;
				if(NOTVIS){	VISANDPUSH;}
			}
		    ///Red moves forward,Blue try
		    temp.RED=top.RED+1; temp.BLUE=top.BLUE; temp.point=top.point;
		    if(VALID)
		    {
				if(VW[temp.point].clr=="B" and VW[temp.point].B==temp.BLUE) temp.point++;
				if(NOTVIS){	VISANDPUSH;}
			}
		    
		    ///red moves back,Blue try
			temp.RED=top.RED-1; temp.BLUE=top.BLUE; temp.point=top.point;
		    if(VALID)
		    {
				if(VW[temp.point].clr=="B" and VW[temp.point].B==temp.BLUE) temp.point++;
				if(NOTVIS){	VISANDPUSH;}
			}
						
			///Blue ++ red --
			temp.RED=top.RED-1; temp.BLUE=top.BLUE+1; temp.point=top.point;
		    if(VALID)   {if(NOTVIS){	VISANDPUSH;}}
			
			///Blue ++ red ++
			temp.RED=top.RED+1; temp.BLUE=top.BLUE+1; temp.point=top.point;
			if(VALID)   {if(NOTVIS){	VISANDPUSH;}}
			
			///Blue -- red ++
			temp.RED=top.RED+1; temp.BLUE=top.BLUE-1; temp.point=top.point;
			if(VALID)   {if(NOTVIS){	VISANDPUSH;}}
			
			///Blue -- red --
			temp.RED=top.RED-1; temp.BLUE=top.BLUE-1; temp.point=top.point;
			if(VALID)   {if(NOTVIS){	VISANDPUSH;}}
		
		}
		cnt++;
	//	puts("============");
		if(found) break;
		if(waitQ.empty()) break;
		while(!waitQ.empty())
		{
			actQ.push(waitQ.front());
			waitQ.pop();
		}
		
	}
		if(found)
		printf("Case #%d: %d\n",++kas,cnt);
		else puts("VULLL");
		
	}
	
	
	return 0;
}

