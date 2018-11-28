#include<iostream>
using namespace std;
string poss[11] = {"OOOO","OOOT","OOTO","OTOO","TOOO","TXXX","XTXX","XXTX","XXXT","XXXX"};
int main()
{
    int T;
    char temp[4];
    int I=1;
    int d,e;
    int i,j,k,m;
    string a[4];
    int flag,t;
    cin>>T;
    while(T--)
    {
              int Y=T;
               flag=0;
               t=11;
               T=Y;
             for(i=0;i<4;i++)
                             cin>>a[i];
             cout<<"Case #"<<I<<": ";
             I++;
              T=Y;
              for(i=0;i<4;i++)
              {    
                               T=Y;
                         t=11;
                              for(m=0;m<10;m++)
                              {
                                               if(a[i]==poss[m])
                                               {
												t=m;
												}
							}
							 T=Y;
                              if((t>=0)&&(t<=4))
							  {
								cout<<"O won";
								 T=Y;
								goto A;
								}
                              else if((t>4)&&(t<=9))
							{
								cout<<"X won";
                                 T=Y;goto A;
								}
                                
                                                       
              }
              
              
                      T=Y;
            for(j=0;j<4;j++)
            {
				for(k=0;k<4;k++)
					temp[k]=a[k][j];
				temp[4]='\0';
                t=11;
				for(m=0;m<10;m++)
				{
					if(temp==poss[m])
					{
						t=m;
					}
				}
				if((t>=0)&&(t<=4))
				{
					cout<<"O won";
					 T=Y;
					goto A;
				}
				else if((t>4)&&(t<=9))
				{
					cout<<"X won";
					 T=Y;
					goto A;
				}                                      

			}  
			temp[0]=a[0][0];
            temp[1]=a[1][1];
			temp[2]=a[2][2];
			temp[3]=a[3][3];
			temp[4]='\0';
			t=11;
			for(m=0;m<10;m++)
			{
				if(temp==poss[m])
				{
					t=m;
				}
			}
			if((t>=0)&&(t<=4))
			{
				cout<<"O won";
				 T=Y;
				goto A;
			}
			else if((t>4)&&(t<=9))
			{
				cout<<"X won";
				 T=Y;
				goto A;
			}
			temp[0]=a[0][3];
			temp[1]=a[1][2];
			temp[2]=a[2][1];
			temp[3]=a[3][0];
			temp[4]='\0';
			t=11;
			for(int m=0;m<10;m++)
			{
				if(temp==poss[m])
				{
					t=m;
				}
			}
			if((t>=0)&&(t<=4))
			{
				cout<<"O won";
				
				 T=Y;
				goto A;
			}
			else if((t>4)&&(t<=9))
			{
				cout<<"X won";
				 T=Y;
				goto A;
			}
			for(d=0;d<4;d++)
				for(e=0;e<4;e++)
				{
					if(a[d][e]=='.')
					{
						flag=1;
					}
				}
			if(flag==1)
			{
				cout<<"Game has not completed";
				T=Y;
			}
			else
			{
				cout<<"Draw";
				T=Y;
			}             
             
             
         A: cout<<endl;
         T=Y;
             
    }
   
    return 0;
}

                                     
                                   
