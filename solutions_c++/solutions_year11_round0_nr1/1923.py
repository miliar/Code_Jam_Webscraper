#include <iostream>
#include <string>

using namespace std;
long int cas=1,n,k,i,j;
//long int bp=1,op=1,bpos=300,opos=300,s,s1,pushd=1;
//long int tmc=0;
//struct xyz{long int n;long int r;}mas[200];
//char tmp;

void casen()
{
cout<<"Case #"<<cas<<": ";
cas++;
}

int main()
{
	   freopen("A-large.in","r",stdin);
   freopen("output.txt","w",stdout);
	cin>>n;
	for(j=0;j<n;j++)
	{
		//long int cas=1,n,k,i,j;
long int bp=1,op=1,bpos=300,opos=300,s=0,s1=0,pushd=1;
long long tmc=0;
struct xyz{long int n;long int r;}mas[200];
char tmp;

	cin>>k;
	for(i=0;i<k;i++)
	{
	cin>>tmp>>mas[i].n;
	if(tmp=='O')mas[i].r=0;else mas[i].r=1;
	if(tmp=='O'&&s1==0){opos=i;s1=1;}
	if(tmp=='B'&&s==0){bpos=i;s=1;}
	}
	mas[k].r=2;
	
	while(1)
	{
	//cout<<bpos<<" - "<<bp<<"  "<<opos<<" - "<<op<<"  "<<tmc<<endl;
	//system("PAUSE");
	pushd=1;
		if(s){
	if(mas[bpos].n!=bp) {if(mas[bpos].n>bp)bp++;else bp--;}
	else {if(bpos<opos&&pushd){pushd=0;do{bpos++;}while(mas[bpos].r==0);if(mas[bpos].r==2)s=0;}}}
		
	if(s1){
		if(mas[opos].n!=op) {if(mas[opos].n>op)op++;else op--;}
	else {if(bpos>opos&&pushd){pushd=0;do{opos++;}while(mas[opos].r==1);if(mas[opos].r==2)s1=0;}}}
	
	if(s==0&&s1==0)break;
	tmc++;
	}
	
	casen();
	cout<<tmc+1<<endl;
	tmc=0;bpos=300;opos=300;
	}
		
	return 0;
}