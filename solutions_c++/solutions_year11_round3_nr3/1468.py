#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int gcd(int a, int b)
{
        if(b == 0)
        {
                return a;
        }
        else
        {
                return gcd(b, a % b);
        }
}

int LCD(int a,int b) {
int c;
if (b > a) { c=b; b=a; a=c; } // make sure a > b
return a*b/gcd(a,b);
}

void InsertionSort(int num[],int numLength)
{
     int i, j, key;
     for(j = 1; j < numLength; j++)    // Start with 1 (not 0)
    {
           key = num[j];
           for(i = j - 1; (i >= 0) && (num[i] < key); i--)   // Smaller values move up
          {
                 num[i+1] = num[i];
          }
         num[i+1] = key;    //Put key into its proper location
     }
     return;
}




int main(){
int T;
cin >>T;
for(int t=1;t<=T;t++){
int N,L,H;
cin>>N;
cin>>L;
cin>>H;
int note[N];
for(int j=0;j<N;j++){
cin>>note[j];
}
InsertionSort(note,N);
int i;

int high=-1;
for(i=0;i<N;i++)
{
if(note[i]>H) high++;
}

int low= N;
for(i=N-1;i>=0;i--)
{
if(note[i]<L) low--;
}

int g;
bool gfound=false;
for(i=0;i<=high;i++){
if(i==0) {g=note[0]; gfound=true;}
else {
if(g>note[i])g=gcd(g,note[i]);
else g=gcd(note[i],g);}
}
int l=1;
bool lfound=false;
for(i=N-1;i>=low;i--){
lfound=true;
l=LCD(l,note[i]);
}


int number=-1;
for(int i=L;i<=H;i++)
{bool fin=false;
if(gfound&&lfound){
  if(g%i==0&&i%l==0)fin=true;}

if(gfound&&!lfound){
  if(g%i==0)fin=true;}

if(!gfound&&lfound){
  if(i%l==0)fin=true;}
if(!gfound&&!lfound)fin=true; 
    if(fin){
       bool found=true;
	for(int j=high+1;j<=low-1;j++)
	{
		if(note[j]%i!=0&&i%note[j]!=0)
		{
		found=false;
		break;	
		}
	}
	if(found){number=i;break;}
  }
} 

if(number==-1)cout<<"Case #"<<t<<": NO"<<endl;
else cout<<"Case #"<<t<<": "<<number<<endl;
}
}
