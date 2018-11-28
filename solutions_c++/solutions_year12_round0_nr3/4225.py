#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<math.h>
void main(){

clrscr();
//int* N=new int[T];

ofstream output;
output.open("output.txt");
ifstream input;
input.open("input.txt");


int T;
input>>T;


for(int k=0;k<T;k++)
{
int A,B,count=0;
input>>A>>B;
int length=0;
int temp=A;
while(temp!=0){
length++;
temp=temp/10;
}
for(int i=A;i<B;i++){

temp=i;
int l=0;
while(temp!=0){
l++;
int nn=0;
int* numbers=new int[length];
temp=temp/10;
int n=(i%(int)pow(10,l))*pow(10,length-l)+temp;

int flag=0;
for(int x=0;x<nn;x++)
{
if(n==numbers[x])
{flag=1;

break;
}}

if(flag==0&&n>i&&n<=B){
numbers[nn]=n;
nn++;
count++;
}
}

}


output<<"Case #"<<k+1<<": "<<count<<endl;
}
output.close();
getch();

}