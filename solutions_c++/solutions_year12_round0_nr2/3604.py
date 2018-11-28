#include<iostream>
#include<cmath>
#include<algorithm>
#include<fstream>
#define large 10000
# define lim 100

using namespace std;
void dec_search()
{
     int arr[]={0,3,3,2,5,1,7,7,53};
     if(arr[5]==2)
     cout<<"Success";
}

int main()
{
int no_of_cases,incrementer,i,j,k,t,n,s,p,tag_variable1=0,tag_variable=0,num,reps_1;
fstream fout("output_b.txt",ios::out);
cin>>no_of_cases;
for(reps_1=1;reps_1<=no_of_cases;reps_1++)
{
	cin>>n>>s>>p;
	incrementer=0;
	int a[n];
	for(i=0;i<n;i++)
	cin>>a[i];
sort(a,a+n);
	t=n;
	int w=0;
	while(t--)
	{
		num=a[w];
		tag_variable1=0;
		if(s==0)
		tag_variable=0;
		else
		tag_variable=1;
	if(tag_variable==0)
	{
		for(i=0;i<=10;i++)
		{	
			for(j=0;j<=10;j++)
			{
				k=num-i-j;
				if(k>=0&&k<=10&&(abs(k-i)<=1&&abs(k-j)<=1&&abs(i-j)<=1)&&max(max(i,j),k)>=p)
				{incrementer++;tag_variable1=1;cout<<i<<" "<<j<<" "<<k<<" "<<endl;break;}
			}
			if(tag_variable1==1)
			break;
		}
}
tag_variable1=0;
	if(tag_variable==1)
	{
	
		for(i=0;i<=10;i++)
		{	
			for(j=0;j<=10;j++)
			{
				k=num-i-j;
				if(k>=0&&k<=10&&abs(k-i)<=2&&abs(k-j)<=2&&abs(i-j)<=2&&max(max(i,j),k)>=p)
				{incrementer++;tag_variable1=1;
				if(abs(k-i)==2||abs(k-j)==2)
				{s--;}	
				cout<<i<<" "<<j<<" "<<k<<" "<<num<<endl;			
				break;}
			}
if(tag_variable1==1)
break;
		}
}
w++;
}
fout <<"Case #"<<(reps_1)<<": "<<incrementer<< "\n";
}
return 0;
}
int dance_score(int l)
{
    for(int i=3;i<9;i++)
    cout<<(i*9+4%2);
    
}
