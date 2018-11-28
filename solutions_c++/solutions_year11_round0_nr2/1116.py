/*5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
t c d n
*/
#include<iostream>
#include<fstream>
using namespace std;
void read(char comb[][5],char dis[][5],char invoke[],int& c,int& d,int& n);
void process(char comb[][5],char dis[][5],char invoke[],int& c,int& d,int& n);
void deleteChar(char str[],int index);
void insertChar(char str[],char aim,int index);
void  strCut(char str[],int index,int end);
int main()
{
	int t,ii,c,d,n;
	cin>>t;
	ofstream out("outfile.out",ios::out);
	for(ii=0;ii<t;ii++)
	{char comb[40][5]={0};
	  char dis[40][5]={0};
	  char invoke[100]={0};		
	  read(comb,dis,invoke,c,d,n);
	  process(comb,dis,invoke,c,d,n);
	  int i;
	  out<<"Case #"<<ii+1<<": [";
	  for(i=0;i<strlen(invoke);i++)
		  if(i!=strlen(invoke)-1)out<<invoke[i]<<", ";
	  else out<<invoke[i];
        out<<"]"<<endl;
	}
	


	return 0;
}
void read(char comb[][5],char dis[][5],char invoke[],int& c,int& d,int& n)
{
	cin>>c;
	int i,j;
	for(i=0;i<c;i++)cin>>comb[i];
	cin>>d;
    for(i=0;i<d;i++)cin>>dis[i];
	cin>>n;
	cin>>invoke;
}
void process(char comb[][5],char dis[][5],char invoke[],int& c,int& d,int& n)
{
	int pointer=1,i,j,l;
   while(pointer!=strlen(invoke))
   {
	bool flag1=1;
	for(i=0;i<c;i++)
	{
		if(pointer>0)
    	{
		if(comb[i][0]==invoke[pointer]&&comb[i][1]==invoke[pointer-1])
		{
			deleteChar(invoke,pointer);
			deleteChar(invoke,pointer-1);
			insertChar(invoke,comb[i][2],pointer-1);
			i=0;pointer--;flag1=0;
		}
		else if(comb[i][0]==invoke[pointer-1]&&comb[i][1]==invoke[pointer])
		{
			deleteChar(invoke,pointer);
			deleteChar(invoke,pointer-1);
			insertChar(invoke,comb[i][2],pointer-1);
			i=0;pointer--;flag1=0;
		}

	}
	
	else break;

		

		
	}
	if(flag1)
	for(i=0;i<d;i++)
		
	{bool flag=1;
		for(j=pointer-1;j>=0;j--)
		{
			if((invoke[j]==dis[i][0])&&(invoke[pointer]==dis[i][1])||
				(invoke[j]==dis[i][1])&&(invoke[pointer]==dis[i][0]))
			{
			// strCut(invoke,j,pointer);
			// pointer=j-1;
					 strCut(invoke,0,pointer);
			          pointer=-1;
			 flag=0;
			 break;
			}
			if(!flag)break;

		}
	}
	pointer++;

   }
}
void deleteChar(char str[],int index)
{
	int i;
	for(i=index;i<strlen(str);i++)
		str[i]=str[i+1];
}
void insertChar(char str[],char aim,int index)
{int i;
	for(i=strlen(str);i>index;i--)
		str[i]=str[i-1];
	str[index]=aim;
}
void  strCut(char str[],int index,int end)
{

 int i;
 for(i=index;i<=end;i++)
 {
	 deleteChar(str,index);
 }

}
