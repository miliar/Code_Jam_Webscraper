#include<iostream>
#include<cstring>
#include<cmath>

using namespace std;

#define FOR(i,N) for(int i=0; i<(N); ++i)

bool ispresent(char*,char,int);

int main()
  {

    char s[70];int h;

    int T,c,cnt,K,j,k,l;
    
    int N[300];

    long long int ans;

    cin>>T;
	int arr[61];
    FOR(i,T)
      {
	cin>>s;
	
	cnt=0;
	FOR(j,strlen(s)) if(!ispresent(s,s[j],j)) cnt++;
	
	int base=cnt;
if(base==1) base=2;
	//int arr[61];
	for (j=0;j<61;j++) arr[j]=-1;
	int temp=2,p=0;
	char c1=s[0],c2;arr[0]=1;
	for (j=1;j<strlen(s);j++) if(s[j]!=s[0]){ c2=s[j];break;}
	
	for (j=0;j<strlen(s);j++)
	{
		if (s[j]==c1) {arr[j]=1;s[j]='$';}
		if(s[j]==c2) {arr[j]=0;s[j]='$';}
	}
	//cout<<"  b4 ";for (j=0;j<strlen(s);j++) cout<<" "<<arr[j]; cout<<"  ";

	//temp=2
	for (j=0;j<strlen(s);j++)
	{
		if (s[j]!='$')
		{
			char c3=s[j];
			for (h=j;h<strlen(s);h++) if (s[j]==c3) {s[j]='$';arr[j]=temp;}
			temp++;
		}
	}
	//for (j=0;j<strlen(s);j++) cout<<" "<<arr[j]<<" ";
	int sum=0,y=0;//base hai
	for (j=strlen(s)-1;j>=0;j--)
	{
		sum+=(arr[j]*pow(base,y));y++;
	}
	//for (j=0;j<strlen(s);j++) cout<<" "<<arr[j]<<"  ";
	cout<<"Case #"<<i+1<<": "<<sum<<"\n";
	sum=0;
//cout<<endl;

	
   }//end of test cases
		
	//for (j=0;j<strlen(s);j++) cout<<" "<<arr[j]<<" ";
return 0;
}//end of main

bool ispresent(char*s,char c,int j)
  {

    FOR(i,j)
      {
	if(s[i]==c)
	  return(true);
      }
    return(false);
  }
