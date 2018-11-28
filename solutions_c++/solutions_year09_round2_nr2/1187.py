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

string solve(string A)
{
    int size_A;
    size_A=A.size();
    int j;
    j=size_A -1;
    while(A[j]<=A[j-1] && j>=1)
	{
	    j=j-1;
	}
    if(j==0)
	{ 
	    string C="                        ";
	    int k=size_A-1;
	    while(A[k]=='0')
		{
		    k=k-1;
		}
	    int top;
	    top=k;
	    /* cout << A[top] << endl; */
	    C[0]=A[top];
	    A[top]='0';	    
	    for(int k = 1; k<size_A+1;k++)
		{
		    C[k]=A[size_A - k];
		}
	    return C;
	}

    int pivot;
    pivot = j-1;
    /* cout << A[pivot] << endl; */


    int remp;
    j=size_A - 1;
    while(A[j]<=A[pivot])
	{
	    j=j-1;
	}
    remp=j;
    /* cout << A[remp] << endl; */

    string B="                           ";
    for(int k=0; k<pivot;k++)
	{
	    B[k]=A[k];
	}
    B[pivot]= A[remp];
    /*cout << B << endl;*/
    A[remp]= A[pivot];
    
    int l=pivot+1;
    for(j=size_A-1;j>pivot;j=j-1)
	{
	    
	    B[l]=A[j];
	    l++;
	}


    return B;   
}


int main()
{   
    cin >> N;
    for(int i=1; i<=N; i++)
	{
	    string a;
	    cin >> a;
	    cout << "Case #" << i << ": " << solve(a) << endl;
	    
	}
}
