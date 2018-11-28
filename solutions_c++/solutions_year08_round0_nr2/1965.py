#include<iostream>
#include<fstream>

#include<string>
using namespace std;
struct time
{
int depart_hour;
int depart_min;
int arrive_hour;
int arrive_min;

};
int available(time* array,int consume,int size,int hour,int min)
{
int value=0;
int addhour=consume/60;
int addmin=consume%60;
int actualhour=0;
int actualmin=0;
for(int i=0;i<size;i++)
{
actualhour=array[i].arrive_hour+(consume+array[i].arrive_min)/60;
actualmin=(consume+array[i].arrive_min)%60;
if(actualhour==hour && actualmin==min)
value++;
}

return value;
}
int run(time* array,int size,int hour,int min)
{
int value=0;

for(int i=0;i<size;i++)
{
if(array[i].depart_hour==hour && array[i].depart_min==min)
value++;

}

return value;

}

int main()
{
	int consume;
	int availa=0;
	int availb=0;
	int needa=0;
	int needb=0;
	int hour=0;
	int min=0;
	char dummy;
time    * A,*B;
	int size1,size2;
int temp1,temp2;
ofstream outfile;
outfile.open("output1.txt");
ifstream infile;
infile.open("B-large.in");
int term;
infile>>term;
for(int i=0;i<term;i++)
{
infile>>consume;
	infile>>size1>>size2;


A=new time [size1];
B = new time[size2];
for(int j=0;j<size1;j++)
{
infile>>A[j].depart_hour>>dummy>>A[j].depart_min>>A[j].arrive_hour>>dummy>>A[j].arrive_min;
}
for(int k=0;k<size2;k++)
{

infile>>B[k].depart_hour>>dummy>>B[k].depart_min>>B[k].arrive_hour>>dummy>>B[k].arrive_min;

}
hour=0;
min=0;
availa=0;
availb=0;
needa=0;
needb=0;
while(hour<25)
{
availa=availa+available(B,consume,size2,hour,min);
availb=availb+available(A,consume,size1,hour,min);
temp1=run(A,size1,hour,min);
temp2=run(B,size2,hour,min);
if(availa>=temp1)
availa-=temp1;
else
{
needa+=temp1-availa;
availa=0;
}
if(availb>=temp2)
availb-=temp2;
else
{
needb+=temp2-availb;
availb=0;
}


hour=hour+(min+1)/60;
min=(min+1)%60;
}


outfile<<"Case #"<<i+1<<":"<<"  "<<needa<<" "<<needb<<endl;
}








delete []  A;
delete []  B;
return 0;
}