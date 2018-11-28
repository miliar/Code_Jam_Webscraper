#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main(){

clrscr();
//int* N=new int[T];

ofstream outfile;
outfile.open("output.txt");
ifstream input;
input.open("input.txt");


int T;
input>>T;


for(int i=0;i<T;i++)
{
int N;
input>>N;

int clock=0,oclock=0,bclock=0,opos=1,bpos=1,distance,move;


for(int j=0;j<N;j++)
{
char rob;
int pos;
input>>rob>>pos;
if(rob=='O')
{

distance=pos-opos;
if(distance<0)
distance=-distance;

move=distance-(clock-oclock) ;
if(move>0)
{
clock+=(move+1);
}
else{
clock+=1;
}
oclock=clock;
opos=pos;



}
else
{

distance=pos-bpos;
if(distance<0)
distance=-distance;

int move=distance-(clock-bclock) ;
if(move>0)
{
clock+=(move+1);
}
else{
clock+=1;
}
bclock=clock;
bpos=pos;


}

}


outfile<<"Case #"<<i+1<<": "<<clock<<endl;
cout<<"Case #"<<i<<": "<<clock<<endl;

}
outfile.close();
getch();

}