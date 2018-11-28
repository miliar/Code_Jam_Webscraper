#include<iostream>
#include<fstream>
#include<algorithm>
#define INF 1000
using namespace std;

int surprises=0,counter=-1;
int t,n,s,p,i,j;
void add(int score)
{
if(score%3==0)
{
if(score/3+1<p)
surprises+=INF;
if(score/3<p)
surprises+=1;
if(score==0&&p>0)
surprises+=INF;
}
if(score%3==1)
{
if(score/3+1<p) 
surprises+=INF;
}
if(score%3==2)
{
if(score/3+2<p)
surprises+=INF;
if(score/3+1<p)
surprises+=1;
}
}

int main()
{
ifstream in("google.in");
ofstream out("google.out");

in >> t;

for(i=1;i<=t;i++)
{
in >> n >> s >> p;
int score[n];
for(j=0;j<n;j++)
{in >> score[j];}
sort(score,score+n);
for(j=0;j<n/2;j++)
{swap(score[j],score[n-j-1]);}
while(surprises<=s&&counter<n)
{
counter++;
add(score[counter]);
}
surprises=0;
out << "Case #" << i << ": " << counter << endl;
counter=-1;
}

in.close(); out.close();    
return 0;    
}
