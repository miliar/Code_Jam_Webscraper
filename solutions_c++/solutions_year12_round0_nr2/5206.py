#include<iostream.h>
#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<math.h>

void main()

{
	freopen("g:/sairam/codejam/B-small-attempt4.in","r",stdin);
	freopen("g:/sairam/codejam/Sai_B-small.out","w",stdout);
	int i,j,n,no,st,th,score[100],q,r,op;
	//clrscr();
	cin>>n;

	for(i=0;i<n;i++)
	{
			cin>>no>>st>>th;
			op=0;
			for(j=0;j<no;j++)
				cin>>score[j];
			for(j=0;j<no;j++)
			{

				q=score[j]/3;
				r=score[j]%3;
				if(q>=th)
					op++;
				else if(r!=0 && q+1>=th)
					op++;
				else if(st!=0&& r!=1&&score[j]>=2 && q+2>=th)
				{
					op++;
					st--;
				}
			}



			cout<<"Case #"<<i+1<<": "<<op<<endl;

	}


}