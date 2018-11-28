#include<iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void fileIO()
{
    freopen("dancing-input1.txt","r",stdin);
    freopen("output.txt","w",stdout);
}

void load(int triplet[][3][4],int sum,int i,int j,int k,int l)
{
	triplet[sum][triplet[sum][0][0]+1][0]=l;
	triplet[sum][triplet[sum][0][0]+1][1]=i;
	triplet[sum][triplet[sum][0][0]+1][2]=j;
	triplet[sum][triplet[sum][0][0]+1][3]=k;
	triplet[sum][0][0]++;	
}
main()
{
	int t,n,s,p,sum,total[100][2]={};
	int triplets[31][3][4]={},i,j,k,count,sur;
	fileIO();

	cin >> t;
	
	for(i=0;i<=8;i++)
	{
		sum=3*i;
		load(triplets,sum,i,i,i,0);
		load(triplets,sum+1,i,i,i+1,0);
		load(triplets,sum+2,i,i+1,i+1,0);
		load(triplets,sum+2,i,i,i+2,1);
		load(triplets,sum+3,i,i+1,i+2,1);
		load(triplets,sum+4,i,i+2,i+2,1);
	}
	load(triplets,27,9,9,9,0);
	load(triplets,28,9,9,10,0);
	load(triplets,29,9,10,10,0);
	load(triplets,30,10,10,10,0);

//	for(i=0;i<31;i++)
//		for(j=1;j<=triplets[i][0][0];j++)
//			cout << i<< " " << triplets[i][j][0] << triplets[i][j][1] << triplets[i][j][2] << triplets[i][j][3] << "\n";

	for(i=0;i<t;i++)
	{
		cin >> n >> s >> p;
		count=0;
		sur=0;
		for(j=0;j<n;j++)
		{
			cin >> total[j][0];
			if(total[j][0]>1&&total[j][0]<29)
			{
				if(triplets[total[j][0]][1][3]>=p && triplets[total[j][0]][2][3]>=p)
				{
					count++;
					total[j][1]=2;
				}
				else if(triplets[total[j][0]][1][3]<p && triplets[total[j][0]][2][3]<p)
					total[j][1]=2;
			}
			else
				if(triplets[total[j][0]][1][3]>=p)
				{
					count++;
					total[j][1]=1;
				}
			
			
			
		}
		for(j=0;j<n;j++)
		{	
			if(total[j][1]==0)
				if((triplets[total[j][0]][1][0]==1 && triplets[total[j][0]][1][3]>=p)||(triplets[total[j][0]][2][0]==1 && triplets[total[j][0]][2][3]>=p))
					sur++;
		}
		if(sur>s)
			sur=s;
				
		count=count+sur;

		cout << "Case #" << i+1 << ": " << count << "\n";
		for(j=0;j<n;j++)
			total[j][0]=total[j][1]=0;
		
	}
	
}

