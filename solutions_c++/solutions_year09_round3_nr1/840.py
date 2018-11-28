#include <iostream>
#include <string>

using namespace std;

/* 

const char text[] = "welcome to code jam"; 

string codejam = text;

int lstr;
lstr = s.size();

string str;
getline(cin, str);

cin >> N;
string lost;
getline(cin,lost);

*/



int N;

unsigned long long solve(string A)
{
    int base;
    int size_A;
    char acc[70];
    int cnt;
    size_A=A.size();
    cnt=1;
    acc[0]=A[0];

    for(int i=1;i<size_A;i++)
	{
	    int j=0;
	    while(j<cnt && acc[j] !=A[i])
		{j++;}
	    if(j==cnt)
		{
		    cnt++;
		    acc[cnt-1]=A[i];
		}	    
	}
   
    if(cnt==1)
	{
	    base = 2;
	}
    else
	{
	    base=cnt; 
	}
   

    int nmb[size_A-1];
    for(int j=0; j< size_A;j++)
	{
	    nmb[j]=100;
	}

    nmb[0]=1;
    for(int k=0; k< size_A;k++)
	{
	    if(A[k]==A[0])
		{
		    nmb[k]=1;
		}
	}
    int l=1;  
    while(l<size_A && nmb[l]==1)
	{l++;	    
	}
 

 for(int k=l; k< size_A;k++)
     {
	    if(A[k]==A[l])
		{
		    nmb[k]=0;
		}
	}

 int s=2;

 for(int j=l+1; j< size_A;j++)
     {
	 if(nmb[j]==100)
	     {
		 nmb[j]=s;
		 s++;
		 for(int k=j; k< size_A;k++)
		     {
			 if(A[k]==A[j])
			     {
				 nmb[k]=nmb[j];
			     }
		     }
	     }
     }

 

 unsigned long long ans=0;
 
 unsigned long long pow[size_A];
 pow[size_A-1]=1;
 for(int j=1;j<size_A;j++)
     {
	 unsigned long long accu=base;
	 pow[size_A-1-j]=1;
	 for(int k=1; k<=j;k++)
	     {
		 pow[size_A-1-j]=pow[size_A-1-j] * accu;
	     }
     }
 
 for(int j=0;j<size_A;j++)
     {
	 unsigned long long tmp;
	 tmp = nmb[j] * pow[j];
	 ans = ans + tmp;
     }
 
    return ans;   
}


int main()
{   
    cin >> N;
    for(int i=1; i<=N; i++)
	{
	    string str;
	    cin >> str;
	    cout << "Case #" << i << ": " << solve(str) << endl;	    
	}
}
