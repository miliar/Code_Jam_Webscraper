/*normal
x+x+x=3x
x,x+1,x+1=3x+2
x,x,x+1=3x+1


surprised:

x,x,x+2=3x+2
x,x+1,x+2=3x+3
x,x+2,x+2=3x+4
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(){

int test,t=0;
scanf("%d",&test);

while(t<test){
int N,S,P, a[102],i,count=0,x,y;
scanf("%d%d%d",&N,&S,&P);
for(i=0;i<N;i++)
{
scanf("%d",&a[i]);
}


for(i=0;i<N;i++)

{
if(a[i]%3==0){

	if(a[i]/3>=P)
	{
		count++;
		continue;
	}
}

if((a[i]-2)%3==0&&a[i]-2>=0){

	if(((a[i]-2)/3)+1>=P)
	{
		count++;
		continue;
	}
}
if((a[i]-1)%3==0&&a[i]-1>=0){

	if(((a[i]-1)/3)+1>=P)
	{
		count++;
		continue;
	}
}
if((a[i]-2)%3==0&&a[i]-2>=0&&S){

	if(((a[i]-2)/3)+2>=P)
	{
		count++;
		S--;
		continue;
	}
}

if((a[i]-3)%3==0&&a[i]-3>=0&&S){

	if(((a[i]-3)/3)+2>=P)
	{
		count++;
		S--;
		continue;
	}
}
if((a[i]-4)%3==0&&a[i]-4>=0&&S){

	if(((a[i]-4)/3)+2>=P)
	{
		count++;
		S--;
		continue;
	}
}
}
cout<<"Case #"<<t+1<<": "<<count<<"\n";
t++;
}
return 0;
}
