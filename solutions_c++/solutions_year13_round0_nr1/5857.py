#include<iostream.h>

using namespace std;

int main()
{
	int t,i,j,n=0;
	cin>>t;
	int countx,counto,countt,count;
	
	while(n++<t)
	{
       	char in[4][4];
		for(i=0;i<4;i++)
		cin>>in[i];
		count = 0;
		int flag = 0;
		
		for(i=0;i<4;i++)
		{
            countx = 0;
            counto = 0;
            countt = 0;
            for(j=0;j<4;j++)
            if(in[i][j]=='X')
            countx++;
            else if(in[i][j]=='O')
            counto++;
            else if(in[i][j]=='T')
            countt++;
            else
            count++;
            
            if(countx==4||(countx==3&&countt==1)||(counto==4)||(counto==3&&countt==1))
            {
                flag =1;
                break;
            }
         }
         
         if(flag==0)
 	     for(i=0;i<4;i++)
		{
            countx = 0;
            counto = 0;
            countt = 0;
            for(j=0;j<4;j++)
            if(in[j][i]=='X')
            countx++;
            else if(in[j][i]=='O')
            counto++;
            else if(in[j][i]=='T')
            countt++;
            else
            count++;
            
            if(countx==4||(countx==3&&countt==1)||(counto==4)||(counto==3&&countt==1))
            {
                flag =1;
                break;
            }
         }
         
         if(flag==0)
         {    
            countx = 0;
            counto = 0;
            countt = 0;
 	     for(i=0;i<4;i++)
            if(in[i][i]=='X')
            countx++;
            else if(in[i][i]=='O')
            counto++;
            else if(in[i][i]=='T')
            countt++;
            else
            count++;
            
            if(countx==4||(countx==3&&countt==1)||(counto==4)||(counto==3&&countt==1))
                flag =1;
         }
         
         if(flag==0)
         {     
            countx = 0;
            counto = 0;
            countt = 0;
 	     for(i=3;i>=0;i--)
            if(in[3-i][i]=='X')
            countx++;
            else if(in[3-i][i]=='O')
            counto++;
            else if(in[3-i][i]=='T')
            countt++;
            else
            count++;
            if(countx==4||(countx==3&&countt==1)||(counto==4)||(counto==3&&countt==1))
                flag =1;
         } 
			if(flag==1)
			{
				if(countx==4||(countx==3&&countt==1))
				cout<<"Case #"<<n<<": X won\n";
				else
				cout<<"Case #"<<n<<": O won\n";
			}
			else if(count==0)
			cout<<"Case #"<<n<<": Draw\n";
			else
			cout<<"Case #"<<n<<": Game has not completed\n";
			
	}
	
    return 0;
}
